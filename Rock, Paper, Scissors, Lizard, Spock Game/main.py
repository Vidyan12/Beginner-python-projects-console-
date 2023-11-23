def rpsls():
    # Importing the 'random' module to make random selections
    import random

    # Defining the available choices for the game
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # Randomly selecting the computer's choice from the available options
    computer_choice = random.choice(choices)

    # Prompting the user for their choice
    player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()

    # Validating user input
    while player_choice not in choices:
        print("Invalid choice. Please enter a valid choice.")
        player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()

    # Displaying the computer's choice to the user
    print(f"\nComputer's choice: {computer_choice}")

    # Checking the result of the game based on the user's and computer's choices
    if player_choice == computer_choice:
        # If both choices are the same, it's a tie
        print("It's a tie!")
    elif (
        (player_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or
        (player_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock')) or
        (player_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or
        (player_choice == 'lizard' and (computer_choice == 'spock' or computer_choice == 'paper')) or
        (player_choice == 'spock' and (computer_choice == 'scissors' or computer_choice == 'rock'))
    ):
        # If the user wins based on the choices, display the winning message
        print("You win!")
    else:
        # If the user loses, display the losing message
        print("Computer wins!")

# Calling the function to play the game
rpsls()

