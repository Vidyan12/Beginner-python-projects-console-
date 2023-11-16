import random


def choose_word():
    """
    Choose a random word from a predefined list.

    Returns:
        str: A randomly selected word.
    """
    word_list = ["python", "hangman", "programming", "beginner", "code", "challenge"]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """
    Display the current state of the word with blanks for unguessed letters.

    Args:
        word (str): The target word.
        guessed_letters (list): List of letters guessed by the player.

    Returns:
        str: The word with blanks for unguessed letters.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    """
    The main function to run the Hangman game.
    """
    print("Welcome to Hangman!")

    # Ask the user for the number of attempts
    max_attempts = int(input("How many attempts do you want? Enter a number: "))

    # Choose a random word
    secret_word = choose_word()

    # Initialize variables
    guessed_letters = []
    attempts_left = max_attempts

    while attempts_left > 0:
        # Display the current state of the word
        current_display = display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")

        # Prompt the user for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in secret_word:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        # Check if the player has guessed all the letters
        if set(guessed_letters) >= set(secret_word):
            print("\nCongratulations! You've guessed the word.")
            break

    # Display the outcome of the game
    if attempts_left == 0:
        print(f"\nSorry, you've run out of attempts. The word was '{secret_word}'. Better luck next time!")


if __name__ == "__main__":
    hangman()

