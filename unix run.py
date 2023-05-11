import os
import subprocess

# Get the current working directory
current_directory = os.getcwd()

# Set the path to your shell script
script_path = os.path.join(current_directory, 'script.sh')

# Make sure the script has execute permissions
subprocess.run(['chmod', '+x', script_path])

# Execute the shell script with the dot command
result = subprocess.run(['. ' + script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

# Check if the script executed successfully
if result.returncode == 0:
    print("Script executed successfully.")
    print("Output:", result.stdout)
else:
    print("Script execution failed.")
    print("Error:", result.stderr)
