import random
import string
from random import randint


class RandomSupport(object):
    @classmethod
    def generate_number(cls):
        return randint(0, 99999999999999)

    @classmethod
    def generate_string(cls, length=15):
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))