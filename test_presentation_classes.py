# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# JMunoz,8.21.2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for student data
        with patch('builtins.input', side_effect=['Jocelyn', 'Munoz', '2024-08-21', '3']):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'Jocelyn')
            self.assertEqual(self.employee_data[0].last_name, 'Munoz')
            self.assertEqual(self.employee_data[0].review_date, '2024-08-21')
            self.assertEqual(self.employee_data[0].review_rating, 3)

        # Simulate invalid review_rating input (not an integer)
        with patch('builtins.input', side_effect=['Jocelyn', 'Munoz', '2024-08-21', 'invalid']):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()