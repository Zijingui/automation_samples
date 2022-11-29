# @FileName  :base_api.py
# @Time      :2022/11/12 22:34
# @Author    :Zijin Gui
import os
import requests

from utils.logger_utils import create_logger


class BaseApi:
    __BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"
    __CORPID = "ww2d8e9cb89e2d6989"
    __SECRET = "lbpIQs2pk6TfY01eOktZ2ZCOzeDtT_HbTRW1jy9ELwc"

    def __init__(self):
        '''获取token和logger'''
        self.logger = create_logger()

        path = self.__BASE_URL + f"gettoken?corpid={self.__CORPID}&corpsecret={self.__SECRET}"
        re = requests.get(path)
        self.access_token = re.json().get("access_token")

    def send(self, method, path, **kwargs):
        '''发送请求'''
        re = requests.request(method, self.__BASE_URL + path, **kwargs)
        # 添加log信息
        self.logger.info("=====开始发送请求===")
        self.logger.info(f"请求方法：{method}")
        self.logger.info(f"请求地址：{path}")
        self.logger.info(f"请求参数：{kwargs}")

        return re.json()
