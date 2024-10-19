import unittest
from country_and_city_function import country_and_city

class NameTestCase(unittest.TestCase):
    """Tests for 'country_and_city_function.py'"""
    def test_country_city(self):
        """Do country and city like 'Santiago, Chile' work correctly?"""
        formatted_message = country_and_city('santiago', 'chile')
        self.assertEquals(formatted_message, 'Santiago, Chile')

    def test_country_city_population(self):
        """Do country, city, population like 'Santiago, Chile - population 5000000' work correctly?"""
        formatted_message = country_and_city('santiago', 'chile', 5000000)
        self.assertEquals(formatted_message, "Santiago, Chile - population 5000000")
if __name__ == '__main__':
    unittest.main()