# Define lists for words representing ones, teens, tens, and suffixes for large numbers
ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')
suffixes = ('', 'Thousand', 'Million', 'Billion')


# Function to convert a three-digit number to words
def fetch_words(number, index):
    if number == '0':
        return 'Zero'

    # Extract individual digits
    number = number.zfill(3)
    hundreds_digit = int(number[0])
    tens_digit = int(number[1])
    ones_digit = int(number[2])

    # Initialize the words string
    words = '' if number[0] == '0' else ones[hundreds_digit]

    # Add 'Hundred' if the hundreds digit is not zero
    if words != '':
        words += ' Hundred '

    # Process the tens and ones digits
    if tens_digit > 1:
        words += tens[tens_digit - 2]
        words += ' '
        words += ones[ones_digit]
    elif (tens_digit == 1):
        words += twos[((tens_digit + ones_digit) % 10) - 1]
    elif (tens_digit == 0):
        words += ones[ones_digit]

    # Remove trailing 'Zero' if present
    if (words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '

    # Add the appropriate suffix based on the index
    if len(words) != 0:
        words += suffixes[index]

    return words


# Function to convert a number to words
def convert_to_words(number):
    length = len(str(number))
    # Check if the number is too large for the program to handle
    if length > 12:
        return 'This program supports a maximum of 12 digit numbers.'

    # Calculate the number of groups of three digits
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    # Process the number in groups of three digits
    for i in range(length - 1, -1, -3):
        words.append(fetch_words(
            str(number)[0 if i - 2 < 0 else i - 2: i + 1], copy - count))

        count -= 1

    # Concatenate the words in reverse order
    final_words = ''
    for s in reversed(words):
        final_words += (s + ' ')

    return final_words


# Main program
while True:
    try:
        # Get user input for a number
        number = int(input('Enter any number with upto 12 digits (or type "exit" to end): '))
        # Check for the exit command
        if number == 'exit':
            break
        # Convert the number to words and print the result
        print('%d in words is: %s' % (number, convert_to_words(number)))
    except ValueError:
        print('Invalid input. Please enter a valid number or type "exit" to end.')
