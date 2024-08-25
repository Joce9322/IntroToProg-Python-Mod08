# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# JMunoz,8.21.2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person,Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self): #Tests the constructor
        person = Person("Jocelyn","Munoz")
        self.assertEqual(person.first_name, "Jocelyn")
        self.assertEqual(person.last_name, "Munoz")

    def test_person_invalid_name(self): # Test first and last name validation
        with self.assertRaises(ValueError):
            person = Person("123", "Munoz")
        with self.assertRaises(ValueError):
            person = Person("Jocelyn", "123")

    def test_person_str(self): #Tests the __str__() magic method
        person = Person("Jocelyn", "Munoz")
        self.assertEqual(str(person), "Jocelyn,Munoz")

class TestEmployee(unittest.TestCase):

    def test_employee_init(self): #Tests the constructor
        employee = Employee("Jocelyn" , "Munoz", "2024-08-21", 3)
        self.assertEqual(employee.first_name, "Jocelyn")
        self.assertEqual(employee.last_name, "Munoz")
        self.assertEqual(employee.review_date, "2024-08-21")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_invalid_review(self):
        with self.assertRaises(ValueError):
            employee = Employee("Jocelyn","Munoz","invalid_review_date","Invalid review_rating")

    def test_employee_str(self): #Tests the __str__() magic method
        employee = Employee("Jocelyn", "Munoz", "2024-08-21", 3)
        self.assertEqual(str(employee), "Jocelyn,Munoz,2024-08-21,3")

if __name__ == '__main__':
    unittest.main()
