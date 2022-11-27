# @FileName  :contact_page.py
# @Time      :2022/11/25 21:58
# @Author    :Zijin Gui
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.add_dept_page import AddDeptPage
from pages.add_mem_page import AddMemPage
from pages.base_page import BasePage
from utils.try_click_element import click_elemenmt


class ContactPage(BasePage):
    '''通讯录页'''
    __TIPS = (By.ID, "js_tips")  # toast提示弹窗
    __ADD_BTN = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")  # 添加部门 + 按钮
    __DELETE_MEM_BTN = (By.CSS_SELECTOR, ".ww_btn.js_delete")  # 删除成员按钮
    __ADD_DEPT_BTN = (By.XPATH, "//a[text()='添加部门']")  # 添加部门按钮
    # 删除部门按钮
    __DELETE_DEPT = (
    By.XPATH, "//ul[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']//a[text()='删除']")
    # 删除部门弹窗确认按钮
    __CONFIRM_DEL_DEPT = (By.XPATH, "//div[@class='qui_dialog_foot ww_dialog_foot']/a[text()='确定']")

    def goto_add_members(self):
        '''点击添加成员 进入编辑成员信息页'''
        # 点击添加成员按钮 显示等待 直到在timeout内点击成功
        with allure.step("点击添加成员"):
            self.logger.info("点击添加成员")
            WebDriverWait(self.driver, 10).until(click_elemenmt)

        return AddMemPage(self.driver)

    def goto_add_dept(self):
        '''点击添加部门 跳转到添加部门页面'''
        with allure.step("点击 +"):
            self.logger.info("点击 + ")
            # 元素需要加显示等待
            self.do_click(*self.__ADD_BTN)
        with allure.step("点击添加部门"):
            self.logger.info("点击 添加部门")
            self.do_click(*self.__ADD_DEPT_BTN)

        return AddDeptPage(self.driver)

    def delete_member(self, username):
        '''删除成员'''
        # 选中要删除的成员
        with allure.step(f"勾选要删除的成员:{username}"):
            self.logger.info(f"勾选要删除的成员: {username}")
            self.do_click(By.XPATH, f"//span[text()='{username}']/../../td[1]")
        # 点击删除按钮
        with allure.step("点击删除"):
            self.logger.info("点击删除")
            self.do_click(By.CSS_SELECTOR, ".ww_btn.js_delete")
        # 点击确定
        with allure.step(f"确认删除{username}"):
            self.logger.info("点击确认")
            self.do_click(By.XPATH, "//a[text()='确认']")

        return self

    def delete_department(self, dept_name):
        '''删除部门'''
        with allure.step(f"鼠标hover{dept_name}"):
            self.logger.info(f"鼠标hover到{dept_name}")
            ele = self.do_find(By.XPATH, f"//ul[@class='jstree-children']//a[text()='{dept_name}']")
            # 鼠标hover到要删除的部门名称上
            ActionChains(self.driver).move_to_element(ele).perform()
        with allure.step("点击【更多】按钮"):
            # 点击更多按钮
            self.logger.info("点击更多按钮")
            self.do_click(By.XPATH, f"//ul[@class='jstree-children']//a[text()='{dept_name}']//span")
        # 点击删除
        with allure.step("点击删除"):
            self.logger.info("点击删除")
            self.do_click(*self.__DELETE_DEPT)
        with allure.step("点击确认"):
            # 点击确定
            self.logger.info("点击确认")
            self.do_click(*self.__CONFIRM_DEL_DEPT)

        return self

    def get_tips(self):
        '''获取tips提示文本信息'''
        self.logger.info("获取tips提示语")
        time.sleep(1)

        return self.do_find(*self.__TIPS).text
