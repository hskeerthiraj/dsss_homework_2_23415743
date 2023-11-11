import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_expression

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random integers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test the generation of random operators
        operators = set()
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            operators.add(operator)
            self.assertIn(operator, ['+', '-', '*'])

        # Ensure that all three operators are generated at least once
        self.assertEqual(len(operators), 3)

    def test_calculate_expression(self):
        # Test the calculation of expressions
        test_cases = [
            (5, 2, '+', 7),
            (8, 3, '*', 24),
            (10, 2, '-', 8),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_result in test_cases:
            result = calculate_expression(num1, num2, operator)
            self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
