# @FileName  :mock_data.py
# @Time      :2022/11/26 11:50
# @Author    :Zijin Gui

from faker import Faker


class MyFaker:
    '''mock常用数据'''
    def __init__(self):
        self.faker = Faker(locale="zh_CN")

    def get_name(self):
        return self.faker.name()

    def get_id(self):
        return self.faker.ssn()

    def get_telephone(self):
        return self.faker.phone_number()
