# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


# Main program
if __name__ == "__main__":
    # Infinite loop to keep prompting the user for input
    while True:
        # Get user input as an integer
        input_number = int(input("Enter a number (type '0' to exit): "))

        # Check if the user wants to exit
        if input_number == 0:
            print("Exiting the program. Goodbye!")

            # Break out of the loop to end the program
            break

        # Call the function to check if the entered number is even or odd
        check_even_odd(input_number)
