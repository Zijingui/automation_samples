
import time
import allure
from pages.login_page import LoginPage
from utils.log_utils import Logger
from utils.mock_data import MyFaker


class TestDepartment:
    def setup_class(self):
        # 前置操作：初始化index 类级别
        self.index = LoginPage().login()
        self.logger = Logger()

    def setup(self):
        # 用例前操作 方法级别 每条用例执行前被调用
        # mock测试数据
        faker = MyFaker()
        self.dept_name = faker.get_name()

    def teardown_class(self):
        # 后置操作： 关闭浏览器进程
        self.index.close_broswer()

    @allure.feature("部门管理")
    @allure.story("添加部门")
    @allure.title("冒烟测试--正常新建一级部门")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_dept(self):
        '''测试添加部门'''
        res = self.index.goto_contact_page().goto_add_dept().edit_dept_info(self.dept_name).get_tips()

        self.logger.debug("断言添加部门")
        assert res == "新建部门成功"

        # 数据清理: 删除新增的脏数据
        self.index.goto_index_page().goto_contact_page().delete_department(self.dept_name)

    @allure.feature("部门管理")
    @allure.story("删除部门")
    @allure.title("冒烟测试---正常删除部门")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_dept(self):
        '''测试删除部门'''
        # 新建部门
        page = self.index.goto_contact_page().goto_add_dept().edit_dept_info(self.dept_name)

        # 删除部门
        res = page.delete_department(self.dept_name).get_tips()
        self.logger.debug("断言删除部门")
        assert res == "删除部门成功"

    @allure.title("更新部门")
    @allure.feature("部门管理")
    @allure.story("更新部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_dept(self):
        '''测试修改部门名称'''
        new_name = self.dept_name + str(time.time())  # 更改后的部门名称

        self.index.goto_contact_page().goto_add_dept().edit_dept_info(self.dept_name)
        # 2.修改第一步中新建部门的名称
        res = self.index.goto_contact_page().update_dept_name(self.dept_name, new_name).get_tips()

        # 3.断言
        self.logger.debug("断言修改名称")
        assert res == "修改名称成功"

        # 4.数据清理
        self.index.goto_index_page().goto_contact_page().delete_department(new_name)
