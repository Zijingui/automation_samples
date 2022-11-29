import time
import yaml
from selenium import webdriver


class TestCookieLogin:
    # 用来获取cookie和测试cookie登录 绕过企业微信扫码登录的

    def setup_class(self):
        # 前置动作;准备资源 初始化
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def test_get_cookie(self):
        '''获取cookie'''
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 休眠 扫码 手动登录
        time.sleep(20)

        # 登录后 获取cookie信息
        cookies = self.driver.get_cookies()

        # 将cookie存入yaml文件
        with open("../data/cookie.yml", "w", encoding="utf-8") as f:
            yaml.safe_dump(cookies, f)

    def test_cookie_login(self):
        # 访问登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 获取cookie并添加
        with open("../data/cookie.yml", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)

        # 植入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()