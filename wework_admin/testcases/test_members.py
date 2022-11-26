# @FileName  :test_members.py
# @Time      :2022/11/25 22:07
# @Author    :Zijin Gui
from pages.login_page import LoginPage
from utils.log_utils import Logger
from utils.mock_data import MyFaker


class TestMembers:
    '''测试成员类'''

    def setup_class(self):
        '''前置操作：初始化index页'''
        self.index = LoginPage().login()

    def setup(self):
        # 方法级别 每个测试方法执行前会调用
        # 用例前置操作：回到首页、准备测试数据
        faker = MyFaker()
        self.username = faker.get_name()
        self.accid = faker.get_id()
        self.tel = faker.get_telephone()

    def teardown_class(self):
        '''后置操作：关闭浏览器进程'''
        self.index.close_broswer()

    def test_add_mem_from_index(self):
        '''测试从首页添加成员'''
        # 链式调用
        # 用例层只关心业务

        res = self.index.goto_add_mem_page().edit_info(\
            self.username, self.accid, self.tel).get_tips()

        Logger().debug("断言添加成功")
        assert res == '保存成功'

    def test_add_mem_from_contact(self):
        '''测试从通讯录页添加成员'''
        res = self.index.goto_contact_page().goto_add_members().edit_info(\
            self.username, self.accid,self.tel).get_tips()

        Logger().debug("断言添加成功")
        assert res == "保存成功"
