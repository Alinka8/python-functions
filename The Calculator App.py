# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2

def calculator():
    num1, num2 = get_user_input()
    print("Addition result:", addition(num1, num2))
    print("Subtraction result:", subtraction(num1, num2))
    print("Multiplication result:", multiplication(num1, num2))
    print("Division result:", division(num1, num2))

calculator()

