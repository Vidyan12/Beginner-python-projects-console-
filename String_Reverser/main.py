# Function to reverse a string and print the result
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    print(f"Reversed string: {reversed_string}")


# Main program
if __name__ == "__main__":
    # Infinite loop to keep prompting the user for input
    while True:
        # Get user input
        input_str = input("Enter a string (type 'exit' to end): ")

        # Check if the user wants to exit
        if input_str.lower() == 'exit':
            print("Exiting the program. Goodbye!")

            # Break out of the loop to end the program
            break

        # Call the function to reverse and print the entered string
        reverse_string(input_str)
