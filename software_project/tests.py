from calculator import add, subtract, multiply, divide, power, square_root

assert add(2, 3) == 5
assert subtract(10, 4) == 6
assert multiply(5, 3) == 15
assert divide(10, 2) == 5
assert square_root(9) == 3
assert power(2, 3) == 8
assert divide(10, 0) == "Division by zero error"
assert square_root(-4) == "Negative square root error"
assert add(3, 'c') == "Error: Invalid Input"

print("All tests passed!")
