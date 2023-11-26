#pip install Pillow

from PIL import Image
from collections import Counter

def analyze_color_palette(image_path, num_colors=5):
    # Open the image
    image = Image.open(image_path)

    # Resize the image for faster processing
    image = image.resize((100, 100))

    # Get the image pixels
    pixels = list(image.getdata())

    # Count the occurrences of each color
    color_counter = Counter(pixels)

    # Get the most common colors
    dominant_colors = color_counter.most_common(num_colors)

    # Display or save the color palette
    display_color_palette(dominant_colors)

def display_color_palette(colors):
    print("Dominant Colors:")
    for color, count in colors:
        print(f"Color: {color} | Count: {count}")

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")

    try:
        analyze_color_palette(image_path)
    except Exception as e:
        print(f"An error occurred: {e}")

#In the example output:

#The color is represented as an RGB tuple (Red, Green, Blue).
#The count indicates how many pixels in the image have that particular color.