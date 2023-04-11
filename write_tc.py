def convert_input_to_output(input_str):
    # Split the input string by '=' and ',' to extract the RTM numbers
    rtm_list = input_str.split('=')[1].split(',')
    
    # Create a list to store the output test cases
    output_test_cases = []
    
    # Add the initial test case for file delivery
    output_test_cases.append("TC01_to test if files are delivered properly in the correct location")
    
    # Loop through the RTM numbers and generate the corresponding test cases
    for i, rtm in enumerate(rtm_list, start=2):
        test_case = f"TC{i:02d}_to test {rtm}"
        output_test_cases.append(test_case)
    
    # Add the final test case for data loading
    output_test_cases.append("TC{:02d}_to test if data is loading properly from these feeds".format(len(rtm_list) + 1))
    
    # Join the output test cases into a single string
    output_str = '\n'.join(output_test_cases)
    
    return output_str

# Example usage:
input_str = "rtm = rtm1,rtm2,rtm3,rtm4"

output_str = convert_input_to_output(input_str)

print("Output:")
print(output_str)
