import re

# specify input and output file paths
input_file = 'abc.txt'
output_file = 'output.txt'
ignored_keywords = ["NO BEFORE", "DEFAULT MERGEBLOCKRATIO", "TD MAP", "PRIMARY INDEX", "Request Text", "||Request|Text"]

with open("abc.txt") as f:

    # initialize variables to hold table information
    current_database = ''
    current_table = ''

    # open input and output files
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # loop over each line in the input file
        for line in f_in:
            # remove leading and trailing whitespace from the line
            line = line.strip()
            # check if the line is a CREATE TABLE statement
            if line.startswith('CREATE MULTISET TABLE'):
                # extract the database and table names from the statement
                current_database, current_table = re.search(r'CREATE MULTISET TABLE (\S+)\.(\S+)', line).groups()
            # check if the line defines a column and if it should not be ignored
            elif re.search(r'^\w+ ', line) and not any(keyword in line for keyword in ignored_keywords):
                # extract the column name and data type from the line
                column_name_match = re.search(r'(\w+) (\w+\(\d+(,\d+)?\)|\w+)', line)
                # check if a match was found
                if column_name_match:
                    column_name = column_name_match.group(1)
                    data_type = column_name_match.group(2)
                    # write the table information to the output file
                    f_out.write(f'{current_database}|{current_table}|{column_name}|{data_type}\n')
                # if no match was found, print a warning message
                else:
                    print(f'Warning: line "{line}" does not define a column')
            # ignore all other lines and print them to the console
            else:
                print(f'Ignoring line "{line}"')

    print('Output file generated successfully.')
