# @FileName  :add_dept_page.py
# @Time      :2022/11/25 22:05
# @Author    :Zijin Gui
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddDeptPage(BasePage):
    '''添加部门页面'''

    # 页面元素提取
    __DEPT_NAME = (By.XPATH, "//label[text()='部门名称']/../input")
    __DEPT_LIST = (By.XPATH, "//span[text()='选择所属部门']")
    __DEPT_SELECTED = (By.XPATH, "//div[@class='qui_dialog_body ww_dialog_body']//a[text()='测试部门1']")
    __DEPT_CONFIRM_BTN = (By.XPATH, "//a[text()='确定']")

    def edit_dept_info(self, dept_name):
        '''编辑部门信息 跳转到通讯录页'''
        self.logger.info("输入部门名称")
        self.do_send_keys(dept_name, self.__DEPT_NAME)
        self.logger.info("选择所属部门")
        self.do_click(self.__DEPT_LIST)
        self.do_click(self.__DEPT_SELECTED)
        self.logger.info("点击确定")
        self.do_click(self.__DEPT_CONFIRM_BTN)

        # 解决循环引用的问题 在方法内局部导入
        from pages.contact_page import ContactPage
        return ContactPage(self.driver)