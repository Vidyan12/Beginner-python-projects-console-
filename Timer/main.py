import time
import os
import pygame


def simple_timer(seconds):
    print(f"Timer started for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up!")

    # Play an audio ringtone from the same directory
    ringtone_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "your_ringtone.mp3")

    # Initialize the mixer
    pygame.mixer.init()

    # Load and play the ringtone
    pygame.mixer.music.load(ringtone_path)
    pygame.mixer.music.play()

    # Wait for the ringtone to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Cleanup the mixer
    pygame.mixer.quit()


# Main program
if __name__ == "__main__":
    # Infinite loop to keep prompting the user for input
    while True:
        # Get user input for timer duration
        input_seconds = int(input("Enter the timer duration in seconds (type '0' to exit): "))

        # Check if the user wants to exit
        if input_seconds == 0:
            print("Exiting the timer program. Goodbye!")

            # Break out of the loop to end the program
            break

        # Call the function to start the timer
        simple_timer(input_seconds)


