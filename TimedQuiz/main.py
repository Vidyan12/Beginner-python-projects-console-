import time

def quiz_game(questions, time_limit):
    """
    Conducts a quiz game with a time limit and evaluates the user's score.

    Parameters:
    - questions (list): A list of tuples, each containing a question and its correct answer.
    - time_limit (int): The time limit for the entire quiz in seconds.
    """
    score = 0
    start_time = time.time()

    for question, answer in questions:
        # Display the question and get the user's answer
        print(question)
        user_answer = input("Your answer: ")

        # Check if the user's answer is correct and provide feedback
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

        # Check if the time limit has been exceeded
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time's up!")
            break

    # Display the final score
    print(f"Your final score is {score}/{len(questions)}")

# Example usage:
quiz_questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote Romeo and Juliet?", "Shakespeare"),
    ("What is the largest mammal?", "Blue Whale"),
    ("In which year did World War II end?", "1945"),
    ("What is the currency of Japan?", "Yen")
]

# Set a time limit for the quiz (in seconds)
time_limit = 60

# Call the quiz_game function with the provided questions and time limit
quiz_game(quiz_questions, time_limit)


