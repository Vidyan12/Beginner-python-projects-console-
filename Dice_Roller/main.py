# Importing the 'random' module for random number generation
import random

# Defining the range of values on a standard six-sided dice
min_val = 1
max_val = 6

# Initializing the variable to control the loop
roll_again = "yes"

# Main loop to keep rolling the dice until the user decides to stop
while roll_again.lower() in ["yes", "y"]:
    print("Rolling The Dice...")

    # Generating and printing the value of the 1st die
    print("Die 1:", random.randint(min_val, max_val))

    # Generating and printing the value of the 2nd die
    print("Die 2:", random.randint(min_val, max_val))

    # Asking the user if they want to roll the dice again
    roll_again = input("Roll the Dice Again? (yes/y to continue, any other input to stop): ")

# End of the program
print("Thanks for playing!")

