# @FileName  :index_page.py
# @Time      :2022/11/25 21:56
# @Author    :Zijin Gui
# @Author    :Zijin Gui
from selenium.webdriver.common.by import By
from pages.add_mem_page import AddMemPage
from pages.base_page import BasePage
from pages.contact_page import ContactPage


class IndexPage(BasePage):
    __CONTACT_BTN = (By.ID, "menu_contacts")
    __ADDMEM_BTN = (By.CSS_SELECTOR, ".index_service_cnt_item")

    def goto_contact_page(self):
        '''点击 通讯录 跳转至通讯录页面'''
        # 点击通讯录
        self.logger.info("点击通讯录")
        self.do_click(self.__CONTACT_BTN)

        return ContactPage(self.driver)

    def goto_add_mem_page(self):
        '''点击添加成员 跳转至添加成员页面'''
        # 点击添加成员
        self.logger.info("点击添加成员")

        self.do_click(self.__ADDMEM_BTN)

        return AddMemPage(self.driver)