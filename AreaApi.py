import app


class AreaApi:
    def __init__(self, session):
        self.session = session
        self.list_area_url = app.BASE_URL+"listarea"
        self.add_area_url = app.BASE_URL+"addarea"
        self.modify_area_url = app.BASE_URL+"modifyarea"
        self.remove_area_url = app.BASE_URL+"removearea"

    def list_area(self):
        response = self.session.get(self.list_area_url)
        return response

    # 新增
    def add_area(self, data):
        response = self.session.post(self.add_area_url, data=data)
        return response

    # 修改
    def modify_area(self, json):
        response = self.session.put(self.modify_area_url, json=json)
        return response

    # 删除
    def remove_area(self, params):
        response = self.session.delete(self.remove_area_url, params=params)
        return response
