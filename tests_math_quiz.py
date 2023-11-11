import unittest
from math_quiz import generate_random_number, generate_math_problem, evaluate_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_math_problem(self):
        # Test the generation of math problems
        test_cases = [
            (5, 2, '+', '5 + 2'),
            (8, 3, '*', '8 * 3'),
            (10, 2, '-', '10 - 2'),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem in test_cases:
            generated_problem = generate_math_problem(num1, num2, operator)
            self.assertEqual(generated_problem, expected_problem)

    def test_evaluate_math_problem(self):
        # Test the evaluation of math problems
        test_cases = [
            ('5 + 2', 7),
            ('8 * 3', 24),
            ('10 - 2', 8),
            # Add more test cases as needed
        ]

        for math_problem, expected_answer in test_cases:
            evaluated_answer = evaluate_math_problem(math_problem)
            self.assertEqual(evaluated_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
