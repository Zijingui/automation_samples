
def click_element(click_ele, presence_ele):
    '''
    显示等待方法：点击元素click_ele后，找到presence_ele返回该元素，未找到返回False
    :param click_ele:
    :param presence_ele:
    :return:
    '''
    def _predicate(driver):
        try:
            driver.find_element(*click_ele).click()
            return driver.find_element(*presence_ele)
        except BaseException:
            return False

    return _predicate
