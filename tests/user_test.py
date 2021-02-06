import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User("Mark", "Burns", 33)

    def test_for_first_name(self):
        self.assertEqual("Mark", self.user.first_name)

    def test_for_last_name(self):
        self.assertEqual("Burns", self.user.last_name)

    def test_for_age(self):
        self.assertEqual(33, self.user.age)