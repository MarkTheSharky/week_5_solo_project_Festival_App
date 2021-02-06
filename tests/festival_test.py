import unittest
from models.festival import Festival

class TestFestival(unittest.TestCase):
    
    def setUp(self):
        self.festival = Festival("Benicassim")

    def test_for_name(self):
        self.assertEqual("Benicassim", self.festival.name)