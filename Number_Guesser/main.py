import random


# Function to play the Guess the Number game
def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Display a welcome message
    print("Welcome to Guess the Number!")

    # Main game loop
    while True:
        # Get the user's guess as an integer
        user_guess = int(input("Guess the number (1-100): "))
        attempts += 1

        # Check if the user's guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

            # Break out of the loop to end the game
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


# Main program
if __name__ == "__main__":
    # Call the function to start the Guess the Number game
    guess_the_number()

