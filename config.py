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
                # Search for the string "EDW1_RBG_STAGE"
                if "EDW1_RBG_STAGE" in line:
                    # If the search string is found, extract the prefix from the line
                    prefix = line.split(".")[0]
                    # Search for the string "TABLE_NAME" in the file
                    file.seek(0)  # Return to the beginning of the file
                    for line in file:
                        if f"{prefix}.TABLE_NAME" in line:
                            # If the search string is found, print the line
                            print(f"File: {filename} - Line: {line}")
                            break
                    break  # Stop searching for "EDW1_RBG_STAGE" after the first occurrence
