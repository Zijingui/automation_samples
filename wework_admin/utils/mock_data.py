
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
