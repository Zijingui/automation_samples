# @FileName  :test_deparements.py
# @Time      :2022/11/26 12:34
# @Author    :Zijin Gui
from pages.login_page import LoginPage
from utils.log_utils import Logger
from utils.mock_data import MyFaker


class TestDepartment:
    def setup_class(self):
        # 前置操作：初始化index 类级别
        self.index = LoginPage().login()

    def setup(self):
        # 用例前操作 方法级别 每条用例执行前被调用
        # 准备测试数据
        faker = MyFaker()
        self.dept_name = faker.get_name()

    def teardown_class(self):
        # 后置操作： 关闭浏览器进程
        self.index.close_broswer()

    def test_add_dept(self):
        '''测试添加部门'''
        res = self.index.goto_contact_page().goto_add_dept().edit_dept_info(self.dept_name).get_tips()

        Logger().debug("断言添加部门成功")
        assert res == "新建部门成功"
