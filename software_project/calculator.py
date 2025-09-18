import math


def add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error: Invalid input"


def subtract(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        return "Error: Invalid input"


def multiply(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        return "Error: Invalid input"


def divide(a, b):
    try:
        a = float(a)
        b = float(b)
        if (b == 0):
            return "Division by zero error"
        return a / b
    except ValueError:
        return "Error: Invalid input"


def power(a, b):
    try:
        return float(a) ** float(b)
    except ValueError:
        return "Error: Invalid Input"


def square_root(a):
    try:
        a = float(a)
        if (a < 0):
            return "Negative square root error"
        return math.sqrt(a)
    except ValueError:
        return "Error: Invalid input"
