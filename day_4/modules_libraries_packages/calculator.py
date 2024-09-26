"""Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions.

Create a Python file called calculator.py and complete a viable basic calculator using functions.

MVP (each of these should be in a separate function):

Can add 2 numbers
Can subtract 2 numbers
Can multiply 2 numbers
Can divide 2 numbers
Taking it to the next level:

Implement more complex operations, such as handling parentheses, exponentiation
More advanced operations should continue to be broken into separate functions """
from math_operations import *


print("Welcome to the basic calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose an operation (+, -, *, /, **): ")

# Perform the operation based on user input
match operation:
    case "+":
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    case "-":
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    case "*":
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    case"/":
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    case "**":
        print(f"The result of {num1} ** {num2} is: {exponential(num1, num2)}")
    case _:
        print("Invalid operation selected.")
