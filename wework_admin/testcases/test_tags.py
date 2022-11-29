import time
import allure
from pages.login_page import LoginPage
from utils.log_utils import Logger
from utils.mock_data import MyFaker


class TestTags:
    '''测试标签类'''

    def setup_class(self):
        self.index = LoginPage().login()
        self.logger = Logger()

    def setup(self):
        faker = MyFaker()
        self.tag_name = faker.get_name()

    def teardown_class(self):
        self.index.close_broswer()

    @allure.feature("标签管理")
    @allure.story("添加标签")
    @allure.title("冒烟测试：正常添加标签")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_tags(self):
        '''测试新建标签'''
        res = self.index.goto_contact_page().goto_add_tag(
        ).edit_tag_info(self.tag_name).get_tips()

        # 断言
        self.logger.debug(f"断言创建标签: {self.tag_name}")
        assert res == "创建成功"

        self.index.goto_contact_page().delete_tag(self.tag_name)

    @allure.feature("标签管理")
    @allure.story("删除标签")
    @allure.title("冒烟测试：正常删除标签")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_tags(self):
        '''测试删除标签'''

        self.index.goto_contact_page().goto_add_tag().edit_tag_info(self.tag_name)

        res = self.index.goto_contact_page().delete_tag(self.tag_name).get_tips()

        self.logger.debug(f"断言删除标签: {self.tag_name}")
        assert res == "删除成功"

    @allure.feature("标签管理")
    @allure.story("更新标签")
    @allure.title("冒烟测试：正常修改标签名")
    def test_update_tag_name(self):
        '''测试修改标签名'''
        new_name = self.tag_name + str(time.time())  # 修改后的标签名
        # 新建
        self.index.goto_contact_page().goto_add_tag().edit_tag_info(self.tag_name)

        # 修改名称
        res = self.index.goto_contact_page().update_tag_name(
            self.tag_name, new_name).get_tips()

        # 断言
        self.logger.debug(f"断言修改标签名：{self.tag_name}")
        assert res == "标签保存成功"

        # 删除脏数据
        self.index.goto_contact_page().delete_tag(new_name)
