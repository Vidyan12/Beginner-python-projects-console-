def are_anagrams(word1, word2):
    """
    Check if two words are anagrams.

    Parameters:
    - word1 (str): The first word.
    - word2 (str): The second word.

    Returns:
    - bool: True if the words are anagrams, False otherwise.
    """
    # Convert the words to lowercase and sort the characters
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())

    # Compare the sorted characters of the two words
    return sorted_word1 == sorted_word2

if __name__ == "__main__":
    # Get user input for the two words
    input_word1 = input("Enter the first word: ")
    input_word2 = input("Enter the second word: ")

    # Check if the words are anagrams and display the result
    if are_anagrams(input_word1, input_word2):
        print("They are anagrams!")
    else:
        print("They are not anagrams.")



#An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
# typically using all the original letters exactly once. For example, the word "listen" can be rearranged to form the anagram "silent."
# Anagrams are often used as word puzzles or games,
# where the goal is to rearrange the letters to discover or create a new word or phrase.