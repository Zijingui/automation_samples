import allure
import pytest
from api.contact.department import Department
from utils.load_yaml import get_data


class TestDepartment:
    __YAML_FILE = r"../data/department.yaml"  # yaml文件地址

    def setup_class(self):
        '''初始化department对象'''
        self.department = Department()

    # 使用pytest.mark.parametrize进行参数化
    @pytest.mark.parametrize("dept_name, name_en", get_data(__YAML_FILE).get("create"),\
                             ids=["正常部门名称", "名称含空格"])
    @allure.feature("部门管理")
    @allure.story("部门基本流程测试")
    @allure.severity(allure.severity_level.BLOCKER)  # 设置用例优先级级别
    @allure.title("部门基本流程测试")
    def test_department_flow(self, dept_name, name_en):
        '''部门流程测试'''
        with allure.step("新增部门"):
            # 新增部门
            data = {
                "name": dept_name,
                "name_en": name_en,
                "parentid": 1,
                "order": 1,
                "id": 3
            }
            dept_id = self.department.create(data).get('id')
            print(dept_id)

        # 获取部门列表
        with allure.step("获取部门列表"):
            dept_list = self.department.list()

        with allure.step("断言新增成功"):
            # 断言新增部门ID在部门列表中
            assert dept_id in dept_list

        # 更新部门
        with allure.step("更新部门名称"):
            update_data = {
                "name": dept_name + "===修改",
                "id": dept_id
            }
            self.department.update(update_data)

        # 删除部门
        with allure.step(f"删除部门"):
            self.department.delete(dept_id)
            # 再次获取部门ID列表 断言已删除ID不在列表中
            dept_list = self.department.list()
            assert dept_id not in dept_list

    @allure.title("name参数重名, 新建失败")
    @allure.feature("部门管理")
    @allure.story("新增部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_same_name(self):
        data = {
            "name": "test",
            "parentid": 1
        }
        r1 = self.department.create(data)
        r2 = self.department.create(data)

        assert r2.get("errcode") == 60008
        self.department.delete(r1.get("id"))

    @allure.title("参数缺少parent_id，新建失败")
    @allure.feature("部门管理")
    @allure.story("新增部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_no_pid(self):
        data = {
            'name': "ddd"
        }
        re = self.department.create(data)

        assert re.get("errcode") == 60004

    @allure.title("参数name_en重名，新建失败")
    @allure.feature("部门管理")
    @allure.story("新增部门")
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    def test_create_same_en(self):
        data = {
            "name": "测试",
            "name_en": "test",
            "parentid": 1
        }
        data_same = {
            "name": "测试22",
            "name_en": "test",
            "parentid": 1
        }
        r1 = self.department.create(data)
        r2 = self.department.create(data_same)
        assert r2.get("errcode") == 60008

        self.department.delete(r1.get("id"))

    @allure.title("正常查询部门ID列表")
    @allure.feature("部门管理")
    @allure.story("查询部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_list_success(self):
        '''测试查询部门ID列表'''

        # 新增部门
        data = {
            "name": "test",
            "parentid": 1
        }
        r = self.department.create(data)
        # 查询部门列表
        dept_list = self.department.list()

        assert r.get("id") in dept_list

        # 数据清理
        self.department.delete(r.get("id"))

    @allure.title("输入正确参数，更新部门成功")
    @allure.feature("部门管理")
    @allure.story("更新部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_success(self):
        '''测试更新部门信息'''
        create_data = {
            "name": "新增部门测试",
            "parentid": 1
        }
        dept_id = self.department.create(create_data).get("id")

        update_data = {
            "name": "测试修改名字",
            "id": dept_id
        }
        res = self.department.update(update_data)
        assert res.get("errcode") == 0

        # 数据清理
        self.department.delete(dept_id)

    @allure.title("输入正确参数，成功删除部门")
    @allure.feature("部门管理")
    @allure.story("删除部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_success(self):
        '''测试删除部门'''
        # 新增部门
        data = {
            "name": "新增部门测试",
            "parentid": 1,
            "id": 10
        }
        dept_id = self.department.create(data).get("id")
        # 删除部门
        self.department.delete(dept_id)

        # 获取部门ID列表断言
        assert dept_id not in self.department.list()

    @allure.title("输入根部门id，删除部门失败")
    @allure.feature("部门管理")
    @allure.story("删除部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_root(self):
        # 获取根部门id
        root_id = self.department.list()[0]

        res = self.department.delete(root_id)

        assert res.get("errcode") == 60005

    @allure.title("输入含有子部门的部门id，删除部门失败")
    @allure.feature("部门管理")
    @allure.story("删除部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_parent(self):
        # 新增部门
        data = {
            "name": "新增父部门",
            "parentid": 1
        }
        # 获取父部门id
        parent_id = self.department.create(data).get("id")

        # 在父部门下创建子部门
        son_data = {
            "name": "子部门",
            "parentid": parent_id
        }
        # 添加子部门
        son_id = self.department.create(son_data).get("id")

        # 传入parent id 删除父部门
        res = self.department.delete(parent_id)

        # 断言删除父部门失败
        assert res.get("errcode") == 60006

        # 数据清理
        # 删除子部门
        self.department.delete(son_id)
        # 删除父部门
        self.department.delete(parent_id)
