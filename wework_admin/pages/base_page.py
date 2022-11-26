# @FileName  :base_page.py
# @Time      :2022/11/25 22:24
# @Author    :Zijin Gui
from selenium import webdriver

from utils.log_utils import Logger


class BasePage:
    '''基类' 存放公共方法 和一些初始化工作'''

    def __init__(self, driver=None):
        # 初始化logger
        self.logger = Logger()

        # 如果传入的有driver了 就直接使用 第一次调用时需要初始化 一个driver
        if driver:
            self.logger.info("复用driver")
            self.driver = driver
        else:
            self.logger.info("初始化driver")
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        # 如果打开的地址url不是以http开头时则打开base url
        if not self.driver.current_url.startswith("http"):
            # 进入首页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def do_find(self, by, value=None):
        '''查找一组元素并返回'''

        # 判断是传入的一个元组locator 还是by 和 value单独传入 如果是传入元组 就需要进行解包
        if value:
            return self.driver.find_element(by, value)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, value):
        '''查找多个元素并返回'''
        if value:
            return self.driver.find_elements(by, value)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, text, by, value=None):
        '''封装send_keys方法'''
        if value:
            ele = self.do_find(by, value)
            ele.clear()
            ele.send_keys(text)
        else:
            ele = self.do_find(*by)
            ele.clear()
            ele.send_keys(text)

    def do_click(self, by, value=None):
        '''点击元素'''
        if value:
            self.do_find(by, value).click()
        else:
            self.do_find(*by).click()

    def close_broswer(self):
        '''关闭浏览器并退出进程'''
        self.driver.quit()