# @FileName  :log_utils.py
# @Time      :2022/11/26 11:02
# @Author    :Zijin Gui
import logging
import time


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("wework_admin_logger")
        self.logger.setLevel(logging.DEBUG)
        # 日志文件存放路径
        log_path = f"../log/{int(time.time())}_wework_admin.log"

        # 判断是否已经存在handler 如果有直接使用 解决日志重复打印的问题
        if not self.logger.handlers:
            # 初始化handler
            file_handler = logging.FileHandler(log_path)
            stream_handler = logging.StreamHandler()

            # 设置handler的日志级别
            file_handler.setLevel(logging.DEBUG)
            stream_handler.setLevel(logging.DEBUG)

            # 创建格式器
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # 将格式器添加到handler
            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)

            # 将处理器添加到日志记录器
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)
            # 设置记录器级别
            self.logger.setLevel(logging.DEBUG)

    def debug(self, msg):
        return self.logger.debug(msg)

    def info(self, msg):
        return self.logger.info(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

    def critical(self, msg):
        return self.logger.critical(msg)
