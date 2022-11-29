import allure

from pages.login_page import LoginPage
from utils.log_utils import Logger
from utils.mock_data import MyFaker


class TestMembers:
    '''测试成员类'''

    def setup_class(self):
        '''前置操作：初始化index页'''
        self.index = LoginPage().login()
        self.logger = Logger()

    def setup(self):
        # 方法级别 每个测试方法执行前会调用
        # 用例前置操作：回到首页、准备测试数据
        self.index.goto_index_page()
        faker = MyFaker()
        self.username = faker.get_name()
        self.accid = faker.get_id()
        self.tel = faker.get_telephone()
        self.dept_name = self.username

    def teardown(self):
        # 每次用例执行完都回到首页
        self.index.goto_index_page()

    def teardown_class(self):
        '''后置操作：关闭浏览器进程'''
        self.index.close_broswer()

    @allure.feature("成员管理")
    @allure.story("添加成员")
    @allure.title("从首页添加成员")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_mem_from_index(self):
        '''测试从首页添加成员'''
        # 链式调用
        # 用例层只关心业务

        res = self.index.goto_add_mem_page().edit_info( \
            self.username, self.accid, self.tel).get_tips()

        self.logger.debug("断言添加成员")
        assert res == '保存成功'

        self.index.goto_index_page().goto_contact_page().delete_member(self.username)

    @allure.feature("成员管理")
    @allure.story("添加成员")
    @allure.title("从通讯录页添加成员")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_mem_from_contact(self):
        '''测试从通讯录页添加成员'''
        res = self.index.goto_contact_page().goto_add_members().edit_info( \
            self.username, self.accid, self.tel).get_tips()

        self.logger.debug("断言添加成员")
        assert res == "保存成功"

        # 脏数据清理
        self.index.goto_index_page().goto_contact_page().delete_member(self.username)

    @allure.feature("成员管理")
    @allure.story("删除成员")
    @allure.title("单选删除成员")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_member(self):
        '''测试删除成员'''
        # 1. 添加成员
        res = self.index.goto_add_mem_page().edit_info(self.username, self.accid, self.tel)\
            .delete_member(self.username).get_tips()

        self.logger.debug("断言删除成员")
        assert res == "删除成功"
