import datetime
import logging


def create_logger():

    # 初始化handler
    logger = logging.getLogger("my logger")
    # 设置日志级别
    logger.setLevel(logging.DEBUG)

    # 此处遇到的问题：调用时 日志会重复打印
    # 解决方案一： 判断是否已经存在handler 如果不存在则创建 已存在就直接返回logger对象即可
    # 解决方案二：每次调用后 清空handler，使用     logger.handlers.clear()
    if not logger.handlers:
        # 初始化流处理器
        now = datetime.datetime.now()
        time_stamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        # 日志存放路径
        log_file_path = f'../logs/{time_stamp}_test_wework_log.log'
        handle_stream = logging.StreamHandler()
        handle_file = logging.FileHandler(log_file_path)

        handle_file.setLevel(logging.DEBUG)
        handle_stream.setLevel(logging.DEBUG)

        # 初始化格式器
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 将格式器添加到处理器
        handle_file.setFormatter(formatter)
        handle_stream.setFormatter(formatter)

        # 将处理器添加到记录器
        logger.addHandler(handle_file)
        logger.addHandler(handle_stream)

    return logger
