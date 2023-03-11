def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

while True:

    chooseOperation = input("Choose operation: (Add, Subtract, Divide, Multiply): ")

    if chooseOperation in ("Add", "Subtract", "Divide", "Multiply"):
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input")
            continue

        if (chooseOperation == "Add"):
            print(number1, "+", number2, "=", add(number1, number2))
        elif (chooseOperation == "Subtract"):
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif (chooseOperation == "Divide"):
            print(number1, "/", number2, "=", divide(number1, number2))
        elif (chooseOperation == "Multiply"):
            print(number1, "*", number2, "=", multiply(number1, number2))

    chooseNewOperation = input("Want to do another operation? (Yes, No): ")

    if (chooseNewOperation == "No"):
        break
