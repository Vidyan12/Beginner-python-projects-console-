import time
import random

def intro():
    """
    Introduction to the adventure game.
    """
    print("Welcome to the Text-Based Adventure Game: Battle for Sri Lanka!")
    print("You are the mighty king of Sri Lanka, leading your army against a formidable enemy.")
    print("Make wise decisions to ensure victory and protect your kingdom.\n")
    time.sleep(2)

def choose_path():
    """
    Function to handle the player's choices and progress the story.
    """
    print("Your army stands ready. As the enemy approaches, you must make a crucial decision:")

    choice = input("Do you want to (1) Confront the enemy head-on or (2) Strategically ambush them? ")

    if choice == "1":
        print("\nYou lead your army into a fierce battle. It's a clash of strength and bravery!")
        time.sleep(2)
        battle_result = random_battle()
        if battle_result:
            print("Victory is yours! The enemy retreats, and your kingdom is safe.")
        else:
            print("Unfortunately, the enemy proves too strong. Your kingdom falls.")
    elif choice == "2":
        print("\nYou choose to use the element of surprise. Your army sets up a strategic ambush!")
        time.sleep(2)
        ambush_result = random_ambush()
        if ambush_result:
            print("The ambush is successful! The enemy is defeated, and your kingdom remains intact.")
            additional_choice = input("As the enemy retreats, do you want to (1) Celebrate or (2) Pursue them further? ")
            if additional_choice == "1":
                print("You celebrate with your people, and your victory becomes a legend throughout the kingdom.")
            elif additional_choice == "2":
                print("You decide to pursue the enemy further, ensuring they won't pose a threat again.")
            else:
                print("Invalid choice. The kingdom celebrates your victory!")
        else:
            print("The enemy detects the ambush, and the battle becomes chaotic. Your kingdom is in peril.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        choose_path()

def random_battle():
    """
    Simulate a random battle outcome.
    Returns:
        bool: True if the player wins, False otherwise.
    """
    return random.choice([True, False])

def random_ambush():
    """
    Simulate a random ambush outcome.
    Returns:
        bool: True if the ambush is successful, False otherwise.
    """
    return random.choice([True, False])

def play_again():
    """
    Ask the user if they want to play the game again.
    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    play_again_choice = input("Do you want to play again? (yes/no): ")
    return play_again_choice.lower() == "yes"

def main():
    """
    Main function to run the text-based adventure game.
    """
    while True:
        intro()
        choose_path()

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

