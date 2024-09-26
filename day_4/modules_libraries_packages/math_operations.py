def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle division by zero
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def exponential(a, b):
    return a ** b