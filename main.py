def modify_content(content):
    # Example modification: convert all text to uppercase
    return content.upper()

def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        # Read from the original file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define a new filename for output
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write the file '{filename}'.")

# Run the program
read_and_write_file()
