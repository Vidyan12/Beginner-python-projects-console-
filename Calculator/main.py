def add(x, y):
    """
    Function to add two numbers
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers.
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second (non-zero) number.
    """
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero.")
        return None

def calculator():
    """
    The main function to run the calculator.
    """
    print("Welcome to the Beginner's Calculator! I can help you add, subtract, multiply, and divide two numbers.")

    while True:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Get user input for operation
        operation = input("Choose an operation (+, -, *, /) or 'q' to quit: ")

        # Check if the user wants to quit
        if operation.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        # Perform the selected operation
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Error: Invalid operation. Try again.")
            continue

        # Display the result
        print(f"\nThe Result is: {result}")

if __name__ == "__main__":
    calculator()
