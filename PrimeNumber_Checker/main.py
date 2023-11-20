# Function to check if a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            # If the number is divisible by any i, it's not prime
            return False

    # If no divisors were found, the number is prime
    return True


# Main program
if __name__ == "__main__":
    # Get user input as an integer
    input_number = int(input("Enter a number: "))

    # Check if the entered number is prime and print the result
    if is_prime(input_number):
        print("It's a prime number!")
    else:
        print("It's not a prime number.")

