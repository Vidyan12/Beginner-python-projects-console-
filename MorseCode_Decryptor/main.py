morse_code_dict = {
    '.-': 'A', '-...': 'B',
    '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W',
    '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '/': ' '  # Space in Morse code is represented by '/'
}

def morse_code_to_text(morse_code):
    """
    Decrypts Morse code to text and prints the result.

    Parameters:
    - morse_code (str): The Morse code to be decrypted.
    """
    # Split the Morse code into individual Morse code characters
    morse_code_list = morse_code.split(' ')

    # Use a list comprehension to convert each Morse code character to its corresponding text character
    text = ''.join(morse_code_dict[morse_char] for morse_char in morse_code_list)

    # Print the Morse code and its decrypted text
    print(f"Morse Code: {morse_code}")
    print(f"Decrypted Text: {text}")

if __name__ == "__main__":
    # Get user input for the Morse code
    input_morse_code = input("Enter Morse code: ")

    # Decrypt the Morse code and display the result
    morse_code_to_text(input_morse_code)
