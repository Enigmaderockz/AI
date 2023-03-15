import requests
import json

# Set up the Informatica REST API endpoint and authentication
endpoint = "https://<informatica_host>/api/v2"
username = "<informatica_username>"
password = "<informatica_password>"
auth = (username, password)

# Fetch the list of mappings
response = requests.get(f"{endpoint}/mappings", auth=auth)
mappings = json.loads(response.content)

# Loop through the mappings and fetch the columns
for mapping in mappings:
    mapping_name = mapping["name"]
    response = requests.get(f"{endpoint}/mappings/{mapping_name}", auth=auth)
    mapping_data = json.loads(response.content)
    for transformation in mapping_data["transformations"]:
        if transformation["type"] == "Source Definition":
            source_name = transformation["name"]
            source_fields = transformation["fields"]
        elif transformation["type"] == "Target Definition":
            target_name = transformation["name"]
            target_fields = transformation["fields"]
    # Print the mapping between source and target columns
    for source_field in source_fields:
        for target_field in target_fields:
            if source_field["name"] == target_field["name"]:
                print(f"{source_name}.{source_field['name']} -> {target_name}.{target_field['name']}")
