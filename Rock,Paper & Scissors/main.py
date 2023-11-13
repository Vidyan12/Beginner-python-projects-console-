import random

# Available choices for Rock, Paper, Scissors
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores
cpu_score = 0
player_score = 0

while True:
    # Computer randomly chooses Rock, Paper, or Scissors
    computer = random.choice(choices)

    # Player input
    player = input("Rock, Paper, or Scissors?").capitalize()

    ## Conditions for Rock, Paper, and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    elif player == 'End':
        # Display final scores and exit the loop
        print("Final Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break

# End of the game
