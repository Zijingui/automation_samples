import datetime
import allure


def ui_exception_record(func):
    def inner(*args, **kwargs):
        driver = args[0].driver

        try:
            return func(*args, **kwargs)

        except Exception:
            now = datetime.datetime.now()
            time_stamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # 截图文件存储路径
            screenshot_path = f'../screenshots/image_{time_stamp}.png'
            # page source文件存储路径
            page_source_path = f"../log/page_source_{time_stamp}.html"

            # 截图
            driver.save_screenshot(screenshot_path)

            # 记录 page_source
            with open(page_source_path, "w", encoding="utf8") as f:
                f.write(driver.page_source)

            # 将截图和page source记录到allure报告中
            allure.attach.file(screenshot_path, name="picture",
                               attachment_type=allure.attachment_type.PNG)

            allure.attach.file(page_source_path, name="page_source",
                               attachment_type=allure.attachment_type.TEXT)

            raise Exception

    return inner
