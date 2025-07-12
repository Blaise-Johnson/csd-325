import unittest

from city_functions import city_country

class TestCityCountryFunction(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Dallas", "United States")
        self.assertEqual(result, "Dallas, United States")

if __name__ == '__main__':
    unittest.main()
