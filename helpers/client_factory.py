from helpers.ui_client import UIClient
from helpers.api_client import ApiClient

class ClientFactory(object):
    """
    Factory of various automation clients
    """
    @staticmethod
    def get_ui_client(url=None, with_options=None):
        return UIClient(url, with_options)

    @staticmethod
    def get_api_client():
        return ApiClient()

