# @FileName  :base_page.py
# @Time      :2022/11/25 22:24
# @Author    :Zijin Gui
from selenium import webdriver

from utils.log_utils import Logger
import allure


class BasePage:
    '''基类页面'''

    def __init__(self, driver=None):
        # 初始化logger
        self.logger = Logger()

         # 如果已经存在 直接 复用
        if driver:
            self.logger.info("复用已有的driver")
            self.driver = driver
        else:
            self.logger.info("创建driver")
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        # 如果打开的地址url不是以http开头时则打开base url
        if not self.driver.current_url.startswith("http"):
            # 进入首页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def do_find(self, by, value=None):
        '''查找单个元素并返回'''
        self.logger.info(f"查找元素：{by} {value}")
        # 判断是传入的一个元组locator 还是by 和 value单独传入 如果是传入元组 就解包
        if value:
            return self.driver.find_element(by, value)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, value):
        '''查找多个元素并返回'''
        self.logger.info(f"查找元素：{by} {value}")
        if value:
            return self.driver.find_elements(by, value)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, text, by, value=None):
        '''封装send_keys方法'''
        self.logger.info(f"向元素{by} {value} 输入内容：{text}")
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
        self.logger.info(f"点击元素：{by} {value}")
        if value:
            self.do_find(by, value).click()
        else:
            self.do_find(*by).click()

    def close_broswer(self):
        '''关闭浏览器并退出进程'''
        self.logger.info(f"关闭浏览器进程")
        self.driver.quit()