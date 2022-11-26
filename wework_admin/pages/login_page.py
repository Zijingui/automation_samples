# @FileName  :login_page.py
# @Time      :2022/11/25 21:56
# @Author    :Zijin Gui
import allure
import yaml
from selenium import webdriver

from pages.base_page import BasePage
from pages.index_page import IndexPage


class LoginPage(BasePage):
    '''登录页'''
    __INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame"

    def login(self):
        '''登录方法'''

        with allure.step("使用cookie跳过扫码登录"):
            # 获取cookie并添加
            self.logger.info("植入cookie")
            with open("../data/cookie.yml", encoding="utf-8") as f:
                cookies = yaml.safe_load(f)

            # 植入cookie
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # 进入首页
            self.logger.info("进入首页")
            self.driver.get(self.__INDEX_URL)

        return IndexPage(self.driver)