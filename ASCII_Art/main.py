# Import the Figlet class from the pyfiglet library
from pyfiglet import Figlet


# Function to generate ASCII art from input text
def generate_ascii_art(text):
    # Create a Figlet object with a custom font ('block' in this case)
    custom_fig = Figlet(font='block')

    # Render the input text into ASCII art using the custom Figlet object
    ascii_art = custom_fig.renderText(text)

    # Print the generated ASCII art to the console
    print(ascii_art)


# Main program
if __name__ == "__main__":
    # Infinite loop to keep prompting the user for input
    while True:
        # Get user input
        input_text = input("Enter text (type 'exit' to end): ")

        # Check if the user wants to exit
        if input_text.lower() == 'exit':
            print("Exiting the program. Goodbye!")

            # Break out of the loop to end the program
            break

        # Call the function to generate and display ASCII art for the input text
        generate_ascii_art(input_text)
