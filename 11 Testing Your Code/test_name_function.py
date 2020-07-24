import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self): # Function has to start with test_ or it will not run.
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):  # It is fine to have long method names. They need to be descriptive
        """Do names like 'Dakota Storm Canchela' work?"""
        formatted_name = get_formatted_name("dakota", "canchela", middle="storm")
        self.assertEqual(formatted_name, "Dakota Storm Canchela")



if __name__ == "__main__":
    unittest.main()


