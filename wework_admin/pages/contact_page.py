# @FileName  :contact_page.py
# @Time      :2022/11/25 21:58
# @Author    :Zijin Gui
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.add_dept_page import AddDeptPage
from pages.add_mem_page import AddMemPage
from pages.base_page import BasePage
from utils.try_click_element import click_elemenmt


class ContactPage(BasePage):
    '''通讯录页'''
    __TIPS = (By.ID, "js_tips")
    __ADD_BTN = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    __ADD_DEPT = (By.XPATH, "//a[text()='添加部门']")

    def goto_add_members(self):
        '''点击添加成员 进入编辑成员信息页'''
        # 点击添加成员按钮 显示等待 直到在timeout内点击成功
        self.logger.info("点击添加成员")
        WebDriverWait(self.driver, 10).until(click_elemenmt)

        return AddMemPage(self.driver)

    def goto_add_dept(self):
        '''点击添加部门 跳转到添加部门页面'''

        self.logger.info("点击 + ")
        self.do_click(self.__ADD_BTN)
        self.logger.info("点击 添加部门")
        self.do_click(self.__ADD_DEPT)

        return AddDeptPage(self.driver)

    def get_tips(self):
        '''获取tips提示文本信息'''
        self.logger.info("获取tips提示语")
        time.sleep(1)

        return self.do_find(self.__TIPS).text

