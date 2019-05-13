import nose
from helpers.ui_test_case import UiTests
from helpers.test_assertions import TestAssertions
from utils.utility import Utility

class TestCase1(UiTests, Utility):
    """Sample test case"""

    @classmethod
    def setup_class(cls):
        """Test suite level setup"""
        print ("Class level setup")

    @classmethod
    def teardown_class(cls):
        """Test suite level teardown"""
        print ("Class level teardown")

    def setup(self):
        """Test Case level setup"""
        self.launch_browser()

    def teardown(self):
        """Test Case level teardown"""
        self.close_browser()


    def test_1(self):
        """Test1 - Summary"""
        #self.test_assertion = TestAssertions()
        self.wait(2)
        TestAssertions().assert_equal(1,1)

    def test_2(self):
        """Test2 - Summary"""
        #self.test_assertion = TestAssertions()
        self.wait(1)
        TestAssertions().assert_not_equal(1,2)
