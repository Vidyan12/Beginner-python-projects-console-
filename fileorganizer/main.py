import os
import shutil


def organize_files(source_dir, destination_dir):
    # Get a list of all files in the source directory
    files = os.listdir(source_dir)

    for file in files:
        # Get the full path of the file
        file_path = os.path.join(source_dir, file)

        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(file)

            # Create a directory with the name of the extension if it doesn't exist
            target_folder = os.path.join(destination_dir, extension[1:].lower())
            os.makedirs(target_folder, exist_ok=True)

            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved '{file}' to '{target_folder}'")


if __name__ == "__main__":
    # Specify your source and destination directories
    source_directory = r"C:/Users/ACER/Desktop/VIDYAN"
    destination_directory = r"C:/Users/ACER/Desktop/port"

    # Ensure the source and destination directories exist
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
    elif not os.path.exists(destination_directory):
        print(f"Error: Destination directory '{destination_directory}' does not exist.")
    else:
        # Organize the files
        organize_files(source_directory, destination_directory)

    # Ensure the source and destination directories exist
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
    elif not os.path.exists(destination_directory):
        print(f"Error: Destination directory '{destination_directory}' does not exist.")
    else:
        # Organize the files
        organize_files(source_directory, destination_directory)
