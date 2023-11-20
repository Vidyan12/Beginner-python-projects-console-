# Import the random module to generate random values
import random


# Function to get a random fortune from a predefined list
def get_fortune():
    # List of fortune messages
    fortunes = ["You will have a great day!", "Expect a surprise soon.", "Take risks, they will pay off."]

    # Return a randomly chosen fortune from the list
    return random.choice(fortunes)


# Main program
if __name__ == "__main__":
    # Display a welcome message
    print("Welcome to the Fortune Teller!")

    # Prompt the user to press Enter to reveal their fortune
    input("Press Enter to reveal your fortune...")

    # Call the function to get a random fortune and print it
    print(get_fortune())

