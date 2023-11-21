def read_file(file_path):
    try:
        # Remove any double quotes from the file path
        file_path = file_path.strip('"')

        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"File not found at the specified path: {file_path}")
    except OSError as e:
        print(f"An error occurred while trying to open the file: {e}")

if __name__ == "__main__":
    # Get user input for the file path
    file_path = input("Enter the path of the file: ")

    # Call the function to read the file
    read_file(file_path)






    #only text file can be viewed
