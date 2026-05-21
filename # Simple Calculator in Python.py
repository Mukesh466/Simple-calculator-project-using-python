print("===== Mukesh Kumar's Simple calculator =====")

while True:

    print("\nSelect Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Modulus")
    print("9. Exit")

    choice = input("Enter choice (1-9): ")

    # Exit
    if choice == '9':
        print("Calculator Closed")
        break

    # Square Root
    elif choice == '6':
        num = float(input("Enter number: "))

        if num < 0:
            print("Square root not possible for negative numbers")
        else:
            print("Result:", math.sqrt(num))

    # Factorial
    elif choice == '7':
        num = int(input("Enter number: "))

        if num < 0:
            print("Factorial not possible")
        else:
            print("Result:", math.factorial(num))

    # Other operations
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':

            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", num1 / num2)

        elif choice == '5':
            print("Result:", num1 ** num2)

        elif choice == '8':
            print("Result:", num1 % num2)

        else:
            print("Invalid Choice")