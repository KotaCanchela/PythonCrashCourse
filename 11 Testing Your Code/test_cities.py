# “Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to test).
# Write a method called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string.
# Run test_cities.py, and make sure test_city_country() passes.

import unittest
from city_functions import city_country_formatted


class CityCountryTest(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Tests to see if 'Paris, France' works."""
        city_country_format = city_country_formatted("paris", "france")
        self.assertEqual(city_country_format, "Paris, France")

    def test_city_country_population(self):
        """Tests to see if 'Paris, France -- population 2,148,000' works"""
        city_country_population_format = city_country_formatted(
            "paris", "france", population="2,148,000"
        )
        self.assertEqual(
            city_country_population_format, "Paris, France -- population 2,148,000"
        )


if __name__ == "__main__":
    unittest.main()


# Modify your function so it requires a third parameter, population.
# It should now return a single string of the form City, Country – population xxx,
# such as Santiago, Chile – population 5000000. Run test_cities.py again.
# Make sure test_city_country() fails this time.


# Modify the function so the population parameter is optional.
# Run test_cities.py again, and make sure test_city_country() passes again.

# Write a second test called test_city_country_population() that verifies you
# can call your function with the values 'santiago', 'chile', and
# population=5000000'. Run test_cities.py again, and make sure this new test passes.
