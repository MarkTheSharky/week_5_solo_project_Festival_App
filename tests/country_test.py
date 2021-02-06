import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("Spain", "ES")

    def test_for_name(self):
        self.assertEqual("Spain", self.country.name)

    def test_for_country_code(self):
        self.assertEqual("ES", self.country.country_code)