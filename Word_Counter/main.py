def word_counter(text):
    """
    This function counts the number of words in the given text.

    Args:
        text (str): The input text to be analyzed.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    word_count = len(words)
    return word_count


if __name__ == "__main__":
    print("Welcome to the Word Counter App!")
    print("Let's see how many words are in your sentence or paragraph.")

    # Get input text from the user
    input_text = input("Enter a sentence or paragraph: ")

    # Count the number of words
    count = word_counter(input_text)

    # Display the result
    if count == 1:
        print(f"There is 1 word in your text.")
    else:
        print(f"There are {count} words in your text.")

    # Provide a friendly message based on the word count
    if count < 10:
        print("That's a short one! Keep it up!")
    elif count < 20:
        print("A decent length! Nice job!")
    else:
        print("Wow, that's a long one! Great writing!")

    print("Thanks for using the Word Counter App. Happy coding!")
