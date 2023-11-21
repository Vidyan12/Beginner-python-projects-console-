# Function to capitalize the first letter of each word in a sentence
def capitalize_sentence(sentence):
    # Split the sentence into words, capitalize the first letter of each word, and join them back
    capitalized_sentence = ' '.join(word.capitalize() for word in sentence.split())

    # Print the resulting capitalized sentence
    print(capitalized_sentence)


# Main program
if __name__ == "__main__":
    # Infinite loop to keep prompting the user for input
    while True:
        # Get user input for a sentence
        input_sentence = input("Enter a sentence (type 'exit' to end): ")

        # Check if the user wants to exit
        if input_sentence.lower() == 'exit':
            print("Exiting the program. Goodbye!")

            # Break out of the loop to end the program
            break

        # Call the function to capitalize the first letter of each word in the sentence
        capitalize_sentence(input_sentence)
