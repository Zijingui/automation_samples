# @FileName  :add_mem_page.py
# @Time      :2022/11/25 21:59
# @Author    :Zijin Gui
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddMemPage(BasePage):
    '''编辑成员信息页'''
    __USERNAME = (By.ID, "username")
    __USER_ACCID = (By.ID, "memberAdd_acctid")
    __USER_TEL = (By.ID, "memberAdd_phone")
    __SAVE_BTN = (By.CSS_SELECTOR, ".js_btn_save")

    def edit_info(self, name, accid, tel):
        '''编辑成员信息 并确定添加'''

        # 输入信息
        with allure.step("输入成员信息"):
            self.logger.info(f"输入成员信息：姓名： {name}、 accid：{accid} 、电话号码：{tel}")
            self.do_send_keys(name, *self.__USERNAME)
            self.do_send_keys(accid, *self.__USER_ACCID)
            self.do_send_keys(tel, *self.__USER_TEL)
        # 点击保存
        with allure.step("点击保存"):
            self.logger.info("点击保存")
            self.do_click(*self.__SAVE_BTN)

        from pages.contact_page import ContactPage
        return ContactPage(self.driver)