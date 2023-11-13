import random


def generate_password(length):
    """
    Generates a random password of the specified length.

    Parameters:
    - length (int): Length of the password.

    Returns:
    - str: The randomly generated password.
    """
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    # Check if the specified length is valid
    if length > len(characters):
        print("Password length is greater than the number of available characters. Please choose a shorter length.")
        return None

    password = "".join(random.sample(characters, length))
    return password


while True:
    # Get user input for password length
    password_length = int(input("Enter the length of the password upto 50 (0 to exit): "))

    if password_length == 0:
        print("Exiting. Goodbye!")
        break

    # Generate and print the password
    generated_password = generate_password(password_length)

    if generated_password is not None:
        print("Your randomly generated password is:", generated_password)

