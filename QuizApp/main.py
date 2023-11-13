def check_guess(guess, answer):
    """
    Checks if the user's guess matches the correct answer.

    Parameters:
    - guess (str): The user's guess.
    - answer (str): The correct answer.

    Global:
    - score (int): The user's score.

    Prints:
    - Correct answer message if the guess is correct.
    - Number of attempts message if the guess is incorrect after three attempts.
    """
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer!")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, wrong answer. Try again: ")
            attempt += 1

    if attempt == 3:
        print("Sorry, you've reached the maximum number of attempts. The correct answer is:", answer)

# Initialize score
score = 0

# General knowledge questions and answers
questions_and_answers = {
    "What is the capital of France? ": "Paris",
    "Which planet is known as the Red Planet? ": "Mars",
    "What is the largest ocean on Earth? ": "Pacific",
    "Who wrote 'Romeo and Juliet'? ": "Shakespeare",
    "What is the currency of Japan? ": "Yen",
    "What is the tallest mountain in the world? ": "Everest",
    "Which element has the chemical symbol 'H'? ": "Hydrogen",
    "What is the largest mammal on Earth? ": "Bluewhale",
    "Who painted the Mona Lisa? ": "DaVinci",
    "What is the capital of Australia? ": "Canberra"
}

# Ask questions and check guesses
print("Welcome to the General Knowledge Quiz!")
for question, answer in questions_and_answers.items():
    user_guess = input(question)
    check_guess(user_guess, answer)

# Print final score
print("Your Score is:", score)
