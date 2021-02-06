import unittest
from models.country import Country

class TestContry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("Spain", "ES")

    def test_for_name(self):
        self.assertEqual("Benicassim", self.festival.name)