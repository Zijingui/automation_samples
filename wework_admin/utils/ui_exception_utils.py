import time
import allure


# 当传入的方法发生异常时就自动截图和记录page source
def ui_exception_record(func):
    def inner(*args, **kwargs):
        driver = args[0].driver

        try:
            return func(*args, **kwargs)

        except Exception:
            time_stamp = int(time.time())
            screenshot_path = f'../screenshots/image_{time_stamp}.png'
            page_source_path = f"../log/page_source_{time_stamp}.html"

            # 截图
            driver.save_screenshot(screenshot_path)

            # 记录 page_source
            with open(page_source_path, "w", encoding="utf8") as f:
                f.write(driver.page_source)

            # 将截图和page source记录到allure报告中
            allure.attach.file(screenshot_path, name="picture", \
                               attachment_type=allure.attachment_type.PNG)

            allure.attach.file(page_source_path, name="page_source", \
                               attachment_type=allure.attachment_type.TEXT)

            # 为了保证不影响测试用例的结果 需要在记录之后抛出异常 不然该条用例会断言为pass
            raise Exception

    return inner
