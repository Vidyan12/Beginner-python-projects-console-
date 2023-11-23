# Dictionary mapping characters to their Morse code representations
morse_code_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    ' ': '/'  # Space is represented by '/'
}

def text_to_morse_code(text):
    """
    Converts a text message to its Morse code representation and prints the result.

    Parameters:
    - text (str): The text message to be converted to Morse code.
    """
    # Use a list comprehension to convert each character to its Morse code representation
    morse_code = ' '.join(morse_code_dict[char.upper()] for char in text)

    # Print the original text and its Morse code representation
    print(f"Text: {text}")
    print(f"Morse Code: {morse_code}")

if __name__ == "__main__":
    # Get user input for the text message
    input_text = input("Enter a text message: ")

    # Convert the text to Morse code and display the result
    text_to_morse_code(input_text)
