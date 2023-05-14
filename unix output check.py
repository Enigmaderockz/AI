import subprocess

# Define the Unix command to run
cmd = 'ls -l'

# Run the command and capture its output
output = subprocess.check_output(cmd, shell=True)

# Convert the byte string output to a regular string
output = output.decode()

# Search for a string in the output
search_string = 'myfile.txt'
if search_string in output:
    print(f'{search_string} found in the output')
else:
    print(f'{search_string} not found in the output')
