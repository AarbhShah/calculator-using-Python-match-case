print("Simple Calculator")

while True:
    op = input("Enter operation (+, -, *, /, %): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    match op:
        case "+":
            print("Result =", a + b)

        case "-":
            print("Result =", a - b)

        case "*":
            print("Result =", a * b)

        case "/":
            if b != 0:
                print("Result =", a / b)
            else:
                print("Error: Cannot divide by zero")

        case "%":
            print("Result =", a % b)

        case _:
            print("Invalid operation")

    again = input("Do you want to continue? (y/n): ")

    if again.lower() != "y":
        print("Calculator closed")
        break