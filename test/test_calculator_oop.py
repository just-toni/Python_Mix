import unittest
from calculator.calculator_oop import Calculator


class CalculatorMethodsTest(unittest.TestCase):

    def test_that_method_can_add_two_numbers(self):
        self.assertEqual(5, Calculator.add(2, 3))

    def test_that_add_result_type_is_int(self):
        self.assertEqual(int, type(Calculator.add(2, 3)))
        self.assertIsInstance(Calculator.add(2, 3), int)

    def test_that_non_int_cannot_be_added_to_int(self):
        with self.assertRaises(TypeError):
            Calculator.add("1", 1)

    # what i expect it to be is what i should assert for

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_add_method(self):
        with self.assertRaises(TypeError):
            self.assertEquals(Calculator.add(2, 3, -9), -6)

    def test_that_method_can_subtract_two_numbers(self):
        self.assertEqual(-1, Calculator.subtract(2, 3))

    def test_that_subtract_result_type_is_int(self):
        self.assertEqual(int, type(Calculator.subtract(2, 3)))
        self.assertIsInstance(Calculator.subtract(2, 3), int)

    def test_that_non_int_cannot_be_subtracted_by_int(self):
        with self.assertRaises(TypeError):
            Calculator.subtract("1", 1)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_subtract_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.subtract(2, 3, 4), -1)

    def test_that_method_can_multiply_two_numbers(self):
        self.assertEqual(6, Calculator.multiply(2, 3))

    def test_that_multiply_result_type_is_int(self):
        self.assertEqual(int, type(Calculator.multiply(2, 3)))
        self.assertIsInstance(Calculator.multiply(2, 3), int)

    def test_that_non_int_cannot_be_multiplied_by_int(self):
        with self.assertRaises(TypeError):
            Calculator.multiply("1", 1)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_multiplied_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.multiply(2, 3, 4), 6)

    def test_that_method_can_divide_two_numbers(self):
        self.assertEqual(0, Calculator.divide(2, 3))

    def test_that_divide_result_type_is_int(self):
        self.assertEqual(int, type(Calculator.divide(2, 3)))
        self.assertIsInstance(Calculator.divide(2, 3), int)

    def test_that_non_int_cannot_be_divided_by_int(self):
        with self.assertRaises(TypeError):
            Calculator.divide("1", 1)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_division_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.divide(4, 2, 1), 2)