import requests
from AreaApi import AreaApi
from DB_api import DBApi


class TestArea:

    def setup(self):
        self.session = requests.session()
        self.area_api = AreaApi(self.session)

    # 查询
    def test_list_area(self):
        response = self.area_api.list_area()
        print(response.status_code)
        print(response.text)

    # 新增
    def test_add_area(self):
        data = {"areaName": "aaa", "priority": "123"}
        response = self.area_api.add_area(data=data)
        print(response.status_code)
        print(response.text)

    # 修改
    def test_modify_area(self):
        id = DBApi.select_by_area_name("aaa")
        json = {
            "areaId": id,
            "areaName": "bbb",
            "priority": "321"
        }
        response = self.area_api.modify_area(json=json)
        print(response.status_code)
        print(response.text)

    # 删除
    def test_remove_area(self):
        id = DBApi.select_by_area_name("bbb")
        params = {"areaId": id}
        response = self.area_api.remove_area(params=params)
        print(response.status_code)
        print(response.text)
