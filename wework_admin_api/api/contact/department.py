from api.contact.base_api import BaseApi


class Department(BaseApi):
    '''部门管理接口'''


    def create(self, payload):
        '''新增部门'''

        path = f"department/create?access_token={self.access_token}"

        re = self.send("post", path, json=payload)
        self.logger.info(f"新增部门，响应信息为：{re}")

        return re

    def list(self, **kwargs):
        '''获取部门id列表'''

        path = f"department/simplelist"
        payload = {
            "access_token": self.access_token
        }
        # 如果传入了id 就添加到paylaod
        payload.update(kwargs)
        re = self.send("get", path, params=payload)

        dept_list = []
        for k in re.get("department_id"):
            dept_list.append(k.get("id"))

        self.logger.info(f"查询部门列表，响应信息为：{re}")

        return dept_list  # 返回部门ID列表

    def update(self, payload):
        '''更新部门'''
        path = f"department/update?access_token={self.access_token}"

        re = self.send("post", path, json=payload)
        self.logger.info(f"更新部门信息，响应信息为：{re}")

        return re

    def delete(self, dept_id):
        '''删除部门'''

        path = f"department/delete?access_token={self.access_token}&id={dept_id}"
        re = self.send('get', path)

        self.logger.info(f"删除部门，响应信息为：{re}")

        return re
