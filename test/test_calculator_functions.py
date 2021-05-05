import unittest
from calculator.calculator_functions import add, subtract, multiply, divide


class CalculatorFunctionsTest(unittest.TestCase):
    def test_that_function_can_add_two_numbers(self):
        self.assertEqual(add(4, 5), 9)

    def test_that_add_result_is_int(self):
        self.assertIsInstance(add(9, 5), int)

    def test_that_non_int_cant_be_added_to_int(self):
        with self.assertRaises(TypeError):
            add("9", 3)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_addition_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(add(3, 6, 4), 9)

    def test_that_function_can_subtract_two_numbers(self):
        self.assertEqual(subtract(4, 5), -1)

    def test_that_subtraction_result_is_int(self):
        self.assertIsInstance(subtract(9, 5), int)

    def test_that_non_int_cant_be_subtracted_to_int(self):
        with self.assertRaises(TypeError):
            add("op", 3)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_subtraction_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(add(3, 6, 4), -3)

    def test_that_function_can_multiply_two_numbers(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_that_multiplication_result_is_int(self):
        self.assertIsInstance(subtract(9, 5), int)

    def test_that_non_int_cant_be_multiplied_to_int(self):
        with self.assertRaises(TypeError):
            add("8", 3)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_multiplication_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(add(3, 6, 4), 18)

    def test_that_function_can_divide_two_numbers(self):
        self.assertEqual(divide(4, 5), 0)

    def test_that_division_result_is_int(self):
        self.assertIsInstance(subtract(9, 5), int)

    def test_that_non_int_cant_be_divided_to_int(self):
        with self.assertRaises(TypeError):
            add("d", 3)

    def test_that_illegal_number_of_arguments_cant_be_passed_into_the_division_method(self):
        with self.assertRaises(TypeError):
            self.assertEqual(add(3, 6, 4), 0)