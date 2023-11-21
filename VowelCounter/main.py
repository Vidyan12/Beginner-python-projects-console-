def count_vowels(text):
    # Define the vowels
    vowels = "aeiouAEIOU"

    # Count the number of vowels in the given text
    vowel_count = sum(1 for char in text if char in vowels)

    # Print a fun message based on the number of vowels
    if vowel_count == 0:
        print("No vowels found. Try adding some!")
    elif vowel_count == 1:
        print("You've got a lonely vowel in there!")
    elif vowel_count <= 3:
        print(f"Nice! You have {vowel_count} vowels. Keep it up!")
    else:
        print(f"Wow! {vowel_count} vowels! You're on a roll!")


# Main program
if __name__ == "__main__":
    # Infinite loop to keep prompting the user for input
    while True:
        # Get user input for a text
        input_text = input("Enter some text (type 'exit' to end): ")

        # Check if the user wants to exit
        if input_text.lower() == 'exit':
            print("Exiting the program. Goodbye!")

            # Break out of the loop to end the program
            break

        # Call the function to count and have fun with vowels
        count_vowels(input_text)
