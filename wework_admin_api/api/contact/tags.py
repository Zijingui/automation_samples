from api.contact.base_api import BaseApi


class Tags(BaseApi):
    '''标签相关接口'''

    def create(self, payload):
        '''创建标签'''
        path = f"tag/create?access_token={self.access_token}"

        re = self.send("post", path, json=payload)
        self.logger.info(f"新建标签，响应信息为：{re}")

        return re

    def update(self, payload):
        '''更新标签名字'''
        path = f"tag/update?access_token={self.access_token}"

        re = self.send('post', path, json=payload)
        self.logger.info(f"更新标签名，响应信息为：{re}")

        return re

    def list(self):
        '''获取标签列表'''
        path = f"tag/list?access_token={self.access_token}"
        re = self.send("get", path)
        tag_list = re.get("taglist")

        self.logger.info(f"获取标签列表，响应信息为：{re}")

        return tag_list

    def delete(self, tagid):
        '''删除标签'''

        path = f"tag/delete?access_token={self.access_token}&tagid={tagid}"
        re = self.send("get", path)
        self.logger.info(f"删除标签，响应信息为：{re}")

        return re
