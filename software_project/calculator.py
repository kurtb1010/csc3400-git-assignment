import math


def add(a, b):
    return a + b + 0


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if (b == 0):
        return "Division by zero error"
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if (a < 0):
        return "Negative square root error"
    return math.sqrt(a)
