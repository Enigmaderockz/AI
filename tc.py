# Input string
input_str = '''what: there is no ins

Why: there are many

QA scope:

configs|job
ABCDE|asklffksgskgskfasfkasfksak/ mscopydaily/sgmskgfmsfsmfsf
BCDEF|swfskmvskgfskjfsfgksgksgs/ datacheckexecute/ askfafmafnasfana
LOVELY|wgskmgfsgfksfgsksgf/ extract/.sfs fsjfsjfsjfsfkjlksfksfskfwsk
DEFH|sgjsjfsfmsjvdsvdemgvdsbvmdb/dsfvjsfsfjss./workflow
BCDE|sjfsjgfswjgsgjsgfsjgfjsg/ extratrun/ sfjsfsfjsgfwjwfsafswmnfsgfsjsfjskfswfsfkjsfskfsmfsfmsfgdsgfjg
VBCN|sgjsjfsfmsjvdsvdemgvdsbvmdb/dsfvjsfsfjss./mscopydaily
'''

# Split the input string by lines
lines = input_str.split("\n")

# Initialize a counter for test case sequence numbers
seq_num = 1

# Loop through each line
for line in lines:
    # Skip the line containing "configs|job"
    if "configs|job" in line:
        continue
    # Check if the line contains "mscopydaily"
    elif "mscopydaily" in line:
        # Extract the config value
        config = line.split("|")[0].strip()

        # Write the test case for file watcher job
        print(f"Test Case {seq_num}: Verify if file watcher job is working fine for config {config} as part of code decoupling.")
        seq_num += 1
    # Check if the line contains "datacheckexecute"
    elif "datacheckexecute" in line:
        # Extract the config value
        config = line.split("|")[0].strip()

        # Write the test case for stage or fact load
        print(f"Test Case {seq_num}: Verify if stage or fact load is working fine for config {config} as part of code decoupling.")
        seq_num += 1
    elif "workflow" in line:
        # Extract the config value
        config = line.split("|")[0].strip()

        # Write the test case for stage or fact load
        print(f"Test Case {seq_num}: Verify if workflow load is working fine for config {config} as part of code decoupling.")
        seq_num += 1
    # Check if the line contains "extract" or "extrarun" or a config value    
    elif "extract" in line or "extrarun" in line or line.split("|")[0].strip().isalpha():
        # Extract the config value
        config = line.split("|")[0].strip()

        # Write the test case for extract
        print(f"Test Case {seq_num}: Verify if extract is working fine for config {config} as part of code decoupling.")
        seq_num += 1
