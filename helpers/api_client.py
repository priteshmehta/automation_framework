import requests

class ApiClient(object):
    """TBD"""
    def __init__(self, url):
        self.base_url =  url
        self.user_name = ""
        self.user_pwd = ""
        self.token = ""
        self.auth_type = ""

    def set_auth(self):
        pass

    def get_data(self):
        pass

    def post_data(self):
        pass

    def put_data(self):
        pass

    def delete_data(self):
        pass
