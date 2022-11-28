
import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.add_dept_page import AddDeptPage
from pages.add_mem_page import AddMemPage
from pages.add_tag_page import AddTagPage
from pages.base_page import BasePage
from utils.try_click_element import click_element


class ContactPage(BasePage):
    '''通讯录页'''
    # 部门相关
    __ADD_BTN = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")  # 添加部门 + 按钮
    __ADD_DEPT_BTN = (By.XPATH, "//a[text()='添加部门']")  # 添加部门按钮
    # 部门名称输入框
    __DEPT_NAME_INPUT = (By.XPATH, "//label[text()='部门名称']/../input")

    # 成员相关
    __ADD_MEMBER_BTN = (By.LINK_TEXT, "添加成员")  # 添加成员按钮
    __DELETE_MEM_BTN = (By.CSS_SELECTOR, ".ww_btn.js_delete")  # 删除成员按钮

    # 标签相关
    __TAG_TAB = (
        By.XPATH,
        "//ul[@class='ww_btnGroup']//a[text()='标签']")  # 标签tab
    __ADD_TAG_BTN = (
        By.CSS_SELECTOR,
        ".member_colLeft_top_addBtnWrap")  # 添加标签 按钮 （+）
    # 删除标签/部门
    __DELETE_BTN = (
        By.XPATH,
        "//ul[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']//a[text()='删除']")
    # 修改标签名称/部门名称
    __MODIFY_NAME_BTN = (
        By.XPATH,
        "//ul[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']//a[text()='修改名称']")
    # 标签名称输入框
    __TAG_NAME_INPUT = (
        By.XPATH,
        "//div[@class='member_tag_dialog_inputDlg']//input")

    # 其他元素
    # toast弹窗
    __TIPS = (By.ID, "js_tips")  # toast提示弹窗
    # 保存按钮
    __SAVE_BTN = (
        By.XPATH,
        "//div[@class='qui_dialog_foot ww_dialog_foot']/a[text()='保存']")
    # 确认按钮
    __CONFIRM_BTN = (
        By.XPATH,
        "//div[@class='qui_dialog_foot ww_dialog_foot']/a[text()='确定']")

    def goto_add_members(self):
        '''点击添加成员 进入编辑成员信息页'''
        # 点击添加成员按钮 显示等待 直到在timeout内点击成功
        with allure.step("点击添加成员"):
            self.logger.info("点击添加成员")
            WebDriverWait(
                self.driver, 10).until(
                click_element(
                    self.__ADD_MEMBER_BTN, (By.ID, "username")))

        return AddMemPage(self.driver)

    def goto_add_dept(self):
        '''点击添加部门 跳转到添加部门页面'''
        # 点击 +
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
            self.do_click(*self.__DELETE_MEM_BTN)
        # 点击确定
        with allure.step(f"确认删除{username}"):
            self.logger.info("点击确认")
            self.do_click(By.XPATH, "//a[text()='确认']")

        return self

    def delete_department(self, dept_name):
        '''删除部门'''
        with allure.step(f"鼠标hover{dept_name}"):
            self.logger.info(f"鼠标hover到{dept_name}")
            ele = self.do_find(
                By.XPATH, f"//ul[@class='jstree-children']//a[text()='{dept_name}']")
            # 鼠标hover到要删除的部门名称上
            ActionChains(self.driver).move_to_element(ele).perform()
        with allure.step("点击【更多】按钮"):
            # 点击更多按钮
            self.logger.info("点击更多按钮")
            self.do_click(
                By.XPATH,
                f"//ul[@class='jstree-children']//a[text()='{dept_name}']//span")
        # 点击删除
        with allure.step("点击删除"):
            self.logger.info("点击删除")
            self.do_click(*self.__DELETE_BTN)
        with allure.step("点击确认"):
            # 点击确定
            self.logger.info("点击确认")
            self.do_click(*self.__CONFIRM_BTN)

        return self

    def get_tips(self):
        '''获取tips提示文本信息'''
        self.logger.info("获取tips提示语")
        time.sleep(1)

        return self.do_find(*self.__TIPS).text

    def update_dept_name(self, original_name, new_name):
        '''修改部门名称'''

        with allure.step(f"鼠标hover到{original_name}"):
            ele = self.do_find(
                By.XPATH,
                f"//ul[@class='jstree-children']//a[text()='{original_name}']")
            # 鼠标hover到要修改的部门名称上
            ActionChains(self.driver).move_to_element(ele).perform()
            self.do_click(
                By.XPATH,
                f"//ul[@class='jstree-children']//a[text()='{original_name}']//span")
        with allure.step("点击修改名称"):
            self.do_click(*self.__MODIFY_NAME_BTN)
        with allure.step(f"输入部门名称 {new_name}"):
            self.do_send_keys(new_name, self.__DEPT_NAME_INPUT)
        with allure.step("点击保存"):
            self.do_click(*self.__SAVE_BTN)

        return self

    def goto_add_tag(self):
        '''点击添加标签 跳转到添加标签页'''
        with allure.step("点击添加标签"):
            self.logger.info("点击添加标签")
            self.do_click(
                By.XPATH,
                "//ul[@class='ww_btnGroup']//a[text()='标签']")
            WebDriverWait(
                self.driver,
                10).until(
                click_element(
                    self.__ADD_TAG_BTN,
                    (By.XPATH,
                     "//label[text()='标签名称 ']/../..//input")))

        return AddTagPage(self.driver)

    def delete_tag(self, tag_name):
        '''删除标签'''

        with allure.step("点击标签tab"):
            self.logger.info("点击标签tab")
            self.do_click(*self.__TAG_TAB)

        with allure.step(f"选择要删除的标签：{tag_name}"):
            # 鼠标hover到要删除的标签上
            ele = self.do_find(
                By.XPATH, f"//ul[@class='member_tag_list']/li[text()='{tag_name} ']")
            ActionChains(self.driver).move_to_element(ele).perform()
            # 点击 更多按钮
            self.do_click(
                By.XPATH,
                f"//ul[@class='member_tag_list']/li[text()='{tag_name} ']//a")

        with allure.step("点击删除"):
            self.logger.info("点击删除")
            self.do_click(*self.__DELETE_BTN)

        with allure.step("点击确定"):
            self.logger.info("点击确定")
            self.do_click(*self.__CONFIRM_BTN)

        return self

    def update_tag_name(self, original_name, new_name):
        '''修改标签名'''

        with allure.step("点击标签tab"):
            self.do_click(*self.__TAG_TAB)

        with allure.step(f"选择要修改的标签: {original_name}"):
            # 鼠标hover到要修改的标签上
            self.logger.info("鼠标hover")
            ele = self.do_find(
                By.XPATH,
                f"//ul[@class='member_tag_list']//li[text()='{original_name} ']")
            ActionChains(self.driver).move_to_element(ele).perform()

            # 点击 更多按钮
            self.logger.info("点击更多按钮")
            self.do_click(
                By.XPATH,
                f"//ul[@class='member_tag_list']//li[text()='{original_name} ']/a")

            # 点击修改名称
            self.logger.info("点击修改名称")
            self.do_click(*self.__MODIFY_NAME_BTN)

        with allure.step(f"输入标签名: {new_name}"):
            self.do_send_keys(new_name, *self.__TAG_NAME_INPUT)

        with allure.step("点击确定"):
            self.logger.info("点击确定")
            # 点击确定
            self.do_click(*self.__CONFIRM_BTN)

        return self
