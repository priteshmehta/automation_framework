import nose
from helpers.client_factory import ClientFactory

class UiTests(object):
    """UI Test Case Helper class"""
    def __init__(self):
        super(UiTests, self).__init__()

    def launch_browser(self, url=None):
        print("launch_browser")
        self.__browser_driver = ClientFactory.get_ui_client(url)

    def close_browser(self):
        print("close_browser")
        self.__browser_driver.close()

