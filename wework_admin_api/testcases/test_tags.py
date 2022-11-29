import datetime

import allure
import pytest
from api.contact.tags import Tags
from utils.logger_utils import create_logger
from utils.load_yaml import get_data
from utils.mock_data import MyFaker


class TestTags:
    '''测试标签类'''

    __YAML_FILE = f"../data/tag.yml"

    def setup_class(self):
        self.tag = Tags()
        self.logger = create_logger()

    @allure.feature("标签管理")
    @allure.story("新增标签")
    @allure.title("冒烟测试：传入正确参数，成功新增标签")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("tag_name",
                             get_data(__YAML_FILE).get("tag_name").get("add_tag"))
    def test_add_tag(self, tag_name):
        '''测试新增tag'''
        data = {
            "tagname": tag_name
        }
        tag_id = self.tag.create(data).get("tagid")
        tag_ids = []  # 标签id列表
        #  获取标签id列表
        for tag in self.tag.list():
            tag_ids.append(tag.get("tagid"))
        # 断言新增id在id列表中
        assert tag_id in tag_ids

        # 数据清理
        self.tag.delete(tag_id)

    @allure.feature("标签管理")
    @allure.story("删除标签")
    @allure.title("冒烟测试：传入正确参数，成功删除标签")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("tag_name",
                             get_data(__YAML_FILE).get("tag_name").get("delete_tag"))
    def test_delete_tag(self, tag_name):
        '''测试删除tag'''
        # 新增
        self.tag.create({"tagname": tag_name})
        # 查询tagid
        tag_id = None
        for tag in self.tag.list():
            if tag.get("tagname") == tag_name:
                tag_id = tag.get("tagid")
        # 删除
        self.tag.delete(tag_id)

        # 断言
        tag_ids = []
        # 获取标签id列表
        for tag in self.tag.list():
            tag_ids.append(tag.get("tagid"))

        assert tag_id not in tag_ids

    @allure.feature("标签管理")
    @allure.story("更新标签")
    @allure.title("冒烟测试：传入正确参数，成功更新标签名称")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("tag_name",
                             get_data(__YAML_FILE).get("tag_name").get("update_tag"))
    def test_update_tag(self, tag_name):
        '''测试更新标签名'''
        # 新增
        new_name = tag_name + MyFaker().get_name()
        self.tag.create({"tagname": tag_name})
        # 查询tagid
        tag_id = None
        for tag in self.tag.list():
            if tag.get("tagname") == tag_name:
                tag_id = tag.get("tagid")

        # 更新tagname 断言
        data = {
            "tagid": tag_id,
            "tagname": new_name
        }
        res = self.tag.update(data)

        assert res.get("errcode") == 0
        # 数据清理
        self.tag.delete(tag_id)

    @allure.feature("标签管理")
    @allure.story("查询标签列表")
    @allure.title("冒烟测试：传入正确参数，成功查询标签列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("tag_name",
                             get_data(__YAML_FILE).get("tag_name").get("list_tag"))
    def test_list_tag(self, tag_name):
        '''测试查询标签'''
        # 新增标签
        tag_id = self.tag.create({"tagname": tag_name}).get("tagid")
        # 查询列表 并断言新增标签在返回的列表中
        tag_ids = []
        for tag in self.tag.list():
            tag_ids.append(tag.get("tagid"))

        assert tag_id in tag_ids

        # 数据清理
        self.tag.delete(tag_id)
