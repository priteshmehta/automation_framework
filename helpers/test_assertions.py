import unittest

class TestAssertions(unittest.TestCase):
    """Link: https://docs.python.org/2/library/unittest.html """
    def __init__(self):
        super(TestAssertions, self).__init__()

    def assert_equal(self,val1, val2):
        self.assertEquals(val1,val2)

    def assert_not_equal(self, val1, val2):
        self.assertNotEqual(val1, val2)

    def assert_in_list(self, val1, list_val2):
        self.assertIn(val1, list_val2)

