import unittest
from class_employee import Emlpoyee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        employee_first_name = "First name"
        employee_second_name = "Second name"
        employee_year_salary = 5000
        self.employee = Emlpoyee(employee_first_name, employee_second_name, employee_year_salary)
        self.custom_raise = 10000
    
    def test_give_default_raise(self):
        self.assertIn("Your year salary rise is: 5000, your year salary is: 10000", self.employee.give_raise())

    def test_give_custom_raise(self):
        self.assertIn("Your year salary rise is: 10000, your year salary is: 15000", self.employee.give_raise(self.custom_raise))


if __name__ == "__main__":
    unittest.main()