import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddTagPage(BasePage):
    '''添加标签页'''

    # 标签名输入框
    __TAG_NAME_INPUT = (By.XPATH, "//label[text()='标签名称 ']/../..//input")
    # 确定按钮
    __CONFIRM_BTN = (By.XPATH, "//div[@class='qui_dialog_foot ww_dialog_foot']/a[text()='确定']")

    def edit_tag_info(self, tag_name):
        '''编辑标签信息'''

        with allure.step(f"输入标签信息：{tag_name}"):
            self.logger.info(f"输入标签名： {tag_name}")
            # 输入标签名
            self.do_send_keys(tag_name, *self.__TAG_NAME_INPUT)
        with allure.step("点击确定"):
            self.logger.info("点击确定")
            self.do_click(*self.__CONFIRM_BTN)

        from pages.contact_page import ContactPage
        return ContactPage(self.driver)

