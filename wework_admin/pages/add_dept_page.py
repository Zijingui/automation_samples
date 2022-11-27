# @FileName  :add_dept_page.py
# @Time      :2022/11/25 22:05
# @Author    :Zijin Gui
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddDeptPage(BasePage):
    '''添加部门页面'''

    # 页面元素提取
    __DEPT_NAME = (By.XPATH, "//label[text()='部门名称']/../input")  # 部门名称输入框
    __DEPT_LIST = (By.XPATH, "//span[text()='选择所属部门']")  # 选择所属部门下拉框
    # 企业根目录
    #__DEPT_SELECTED = (By.XPATH, "//div[@class='qui_dialog_body ww_dialog_body']//a[text()='测试部门1']")
    __DEPT_SELECTED = (By.XPATH, "//a[text()='测试企业-1']")
    __DEPT_CONFIRM_BTN = (By.XPATH, "//a[text()='确定']")

    def edit_dept_info(self, dept_name):
        '''编辑部门信息 跳转到通讯录页'''
        with allure.step("输入部门信息"):
            self.logger.info("输入部门名称")
            self.do_send_keys(dept_name, *self.__DEPT_NAME)
            self.logger.info("选择所属部门")
            self.do_click(*self.__DEPT_LIST)
            ele = self.do_finds(*self.__DEPT_SELECTED)
            ele[1].click()
            # self.do_click(*self.__DEPT_SELECTED)
        with allure.step("点击 确定"):
            self.logger.info("点击确定")
            self.do_click(*self.__DEPT_CONFIRM_BTN)

        # 解决循环引用的问题 在方法内局部导入
        from pages.contact_page import ContactPage
        return ContactPage(self.driver)