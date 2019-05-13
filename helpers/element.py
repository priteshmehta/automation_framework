from selenium import webdriver
from selenium.common.exceptions import (InvalidElementStateException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class EC():
    def __init__(self):
        self.conditions = []
        self._description = []

    def copy(self):
        ec = EC()
        ec.conditions = list(self.conditions)
        ec._description = list(self._description)
        return ec

class Element(object):

    def __init__(self, driver, by=None, value=None, parent=None, name=None):
        """
        by(BY): the selenium BY
        value(str): query string
        """
        super(Element, self).__init__()
        self.driver = driver
        self.conditions = EC()

    def element_by_id(self, value, name):
        return self._element(By.ID, value, name)

    def element_by_selector(self, value, name):
        return self._element(By.CSS_SELECTOR, value, name)

    def element_by_xpath(self, value, name):
        return self._element(By.XPATH, value, name)

    def element_by_class(self, value, name):
        return self._element(By.CLASS_NAME, value, name)

    def _element(self, by, value, name):
        return Element(self.driver, by=by, value=value, parent=self, name=name)

class Page(Element):
    def __init__(self, driver, url, name):
        super(Page, self).__init__(driver, name=name)
        self.url = url
        self.driver.get(url)
