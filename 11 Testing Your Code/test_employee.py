import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for a class Employee"""

    def setUp(self):
        """Creates a employee and attributes for the employee"""
        self.my_employee = Employee("Kota", "Canchela", salary=1000)

    def test_give_default_raise(self):
        """Tests that the employee is given the default raise of 5000"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 6000)

    def test_give_custom_raise(self):
        """Tests that the employee is given the custom raise of 7000"""
        self.my_employee.give_raise(7000)
        self.assertEqual(self.my_employee.salary, 8000)


if __name__ == "__main__":
    unittest.main()

