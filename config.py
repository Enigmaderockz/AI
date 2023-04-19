
import os

# Define the directory path where the .cfg files are located
dir_path = "/path/to/directory"

# Loop through each file in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".cfg"):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "r") as file:
            # Read each line of the file
            for line in file:
                # Search for the string "EDW1_RBG_STAGE" or "EDW1_RBE_STAGE"
                if "EDW1_RBG_STAGE" in line or "EDW1_RBE_STAGE" in line:
                    # If the search string is found, search for the string "TABLE_NAME"
                    if "TABLE_NAME" in line:
                        print(f"File: {filename} - Line: {line}")
