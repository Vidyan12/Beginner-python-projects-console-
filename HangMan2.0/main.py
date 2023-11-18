import random
import time
import os


# Function to check if the player wants to play again
def play_again():
    question = 'Do You want to play again? y = yes, n = no \n'
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)

    if play_game.lower() == 'y':
        return True
    else:
        return False


# Function to handle the hangman game logic
def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []

    # Main game loop
    while count < limit:
        # Getting user input for the guess
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        while len(guess) == 0 or len(guess) > 1:
            print('Invalid input. Enter a single letter\n')
            guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()

        # Checking if the guess has already been tried
        if guess in guessed:
            print('Oops! You already tried that guess, try again!\n')
            continue

        # Checking if the guess is correct
        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index] + guess + display[index + 1:]

        # Handling incorrect guesses
        else:
            guessed.append(guess)
            count += 1
            # Displaying hangman figure based on the number of wrong guesses
            if count == 1:
                time.sleep(1)
                print('   _____ \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 2:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 3:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 4:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 5:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |    /|\ \n'
                      '  |    / \ \n'
                      '__|__\n')
                print('Wrong guess. You\'ve been hanged!!!\n')
                print(f'The word was: {word}')

        # Checking if the player has guessed the word
        if display == word:
            print(f'Congrats! You have guessed the word \'{word}\' correctly!')
            break


# Function to start the hangman game
def play_hangman():
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck!')
    time.sleep(1)
    print('The game is about to start!\nLet\'s play Hangman!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    # List of words to be guessed
    words_to_guess = [
        'january', 'border', 'image', 'film', 'promise', 'kids',
        'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world'
    ]

    # Main game loop
    play = True
    while play:
        word = random.choice(words_to_guess)
        hangman(word)
        play = play_again()

    print('Thanks For Playing! We expect you back again!')
    exit()


# Checking if the script is being run as the main program
if __name__ == '__main__':
    play_hangman()
