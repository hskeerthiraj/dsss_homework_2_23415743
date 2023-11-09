import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value, inclusive.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random arithmetic operator (+, -, or *) as a string.
    """
    return random.choice(['+', '-', '*'])

def calculate_expression(n1, n2, operator):
    """
    Calculate the result of the expression based on two numbers and an operator.
    """
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    else:
        return n1 * n2

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        expression = f"{num1} {operator} {num2}"
        correct_answer = calculate_expression(num1, num2, operator)

        print(f"\nQuestion: {expression}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Skip the rest of the loop and move to the next question.

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
