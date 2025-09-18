from calculator import add, subtract, multiply, divide, power, square_root


def main():
    print("Welcome to the calculator!")

    while True:
        print("")
        print("Select an operation using the numbers:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if (choice == "7"):
            print("Goodbye!")
            break

        if (choice == "6"):
            num = float(input("Enter a number: "))
            result = square_root(num)
        else:

            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))

            if (choice == "1"):
                result = add(num1, num2)
            elif (choice == "2"):
                result = subtract(num1, num2)
            elif (choice == "3"):
                result = multiply(num1, num2)
            elif (choice == "4"):
                result = divide(num1, num2)
            elif (choice == "5"):
                result = power(num1, num2)
            else:
                result = "You inputted an invalid choice"
        print("Result: " + result)
