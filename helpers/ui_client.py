from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from config import config
import time

TIMEOUT = config["ui_test_timeout"]
URL = "https://www.ultimateqa.com/automation/"
#chrome_options = ['--ignore-certificate-errors', '--test-type']

class UIClient(object):
    """Class to encapsulate all UI actions"""

    def __init__(self, url=None, with_options=None):
        if config["browser"].lower() == "chrome":
            self.driver = webdriver.Chrome()
            if with_options:
                options = webdriver.ChromeOptions()
                for item in with_options:
                    options.add_argument(item)

                self.driver = webdriver.Chrome(chrome_options=options)
        elif config["browser"].lower() == "firefox":
            self.driver = webdriver.Firefox()
        else:
             raise ("Browser :{} not supported".format(config["browser"]))

        if url:
            self.navigate(url)
        else:
            self.navigate(URL)

    def navigate(self, url):
        if isinstance(url, str):
            self.driver.get(url)
        else:
            raise TypeError("URL must be a string.")

    def get_browser_cookies(self):
        self.driver.get_cookies()

    def set_implicit_wait(self,wait_time):
        self.driver.implicitly_wait(wait_time)

    def take_screenshot(self):
        if config["save_screenshot"]:
            timestamp =  time.time()
            self.driver.save_screenshot("screenshot{}.png".format(timestamp))

    def close(self):
        self.driver.close()

    def execute_script(self, script_string):
        return self.driver.execute_script(script_string)

    def save_page(self, file_name):
        """Save html page"""
        page = self.driver.page_source
        file_ = open(file_name, 'wb')
        file_.write(page.encode('utf8'))
        file_.close()