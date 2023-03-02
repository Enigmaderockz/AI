import requests

# Set the JIRA issue ID
issue_id = "JIRA-1234"

# Set the URL to JIRA's REST API
url = "https://your-jira-url/rest/api/2/issue/{}".format(issue_id)

# Set the JIRA credentials
username = "your-username"
password = "your-password"

# Set the headers for the API request
headers = {
    "Accept": "application/json"
}

# Send the API request to retrieve the issue data
response = requests.get(url, headers=headers, auth=(username, password))

# Parse the response to extract the necessary fields
issue_data = response.json()
summary = issue_data['fields']['summary']
description = issue_data['fields']['description']
priority = issue_data['fields']['priority']['name']
status = issue_data['fields']['status']['name']

# Generate a test case template based on the extracted data
test_case_template = """
Test Case ID: {}
Test Case Summary: {}
Test Case Description: {}
Test Case Priority: {}
Test Case Status: {}
"""

# Fill in the template with the extracted data
test_case = test_case_template.format(issue_id, summary, description, priority, status)

# Print the generated test case
print(test_case)
