import requests
import json

# Define the Informatica REST API endpoint
endpoint = 'https://<informatica_server>/api/v2'

# Define the API credentials
username = '<username>'
password = '<password>'

# Define the workflow to be executed
workflow_name = '<workflow_name>'

# Authenticate with the Informatica REST API
auth_url = endpoint + '/auth/token'
auth_data = {'@type': 'login', 'username': username, 'password': password}
auth_headers = {'Content-Type': 'application/json'}
response = requests.post(auth_url, data=json.dumps(auth_data), headers=auth_headers)
token = response.json()['token']

# Execute the workflow
workflow_url = endpoint + '/public/workflows/' + workflow_name + '/execute'
workflow_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
response = requests.post(workflow_url, headers=workflow_headers)

# Check the status of the workflow execution
execution_id = response.json()['executionId']
status_url = endpoint + '/public/executions/' + execution_id + '/status'
status_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
response = requests.get(status_url, headers=status_headers)
status = response.json()['status']
while status == 'IN_PROGRESS':
    response = requests.get(status_url, headers=status_headers)
    status = response.json()['status']
    
# Print the final status of the workflow execution
print('Workflow execution status:', status)
