# @FileName  :try_click_element.py
# @Time      :2022/11/26 10:37
# @Author    :Zijin Gui
from selenium.webdriver.common.by import By


def click_elemenmt(driver):
    '''
    点击添加成员 判断是否点击成功
    显示等待会在timeout时间内反复执行该方法
    :param: driver  用于接收WebDirverWait 传入的 driver
    '''
    # 1. 点击添加成员按钮
    try:
        driver.find_element(By.LINK_TEXT, "添加成员").click()
    # 2. 判断是否跳转到下一个页面，是否存在用户名输入框
        return driver.find_element(By.ID, "username")
    except:
        return False