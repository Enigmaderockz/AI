import requests
import pandas as pd

# Replace with your JIRA instance URL, username, and API token
jira_url = "https://your_jira_instance.atlassian.net"
jira_username = "your_username"
jira_api_token = "your_api_token"

# Define your projects and their corresponding JQLs
projects = {
    "Project1": [
        "JQL1",
        "JQL2",
        "JQL3",
        "JQL4",
    ],
    "Project2": [
        # ...
    ],
    # ...
}

# Define the labels for each JQL
jql_labels = [
    "story points",
    "PAIN points",
    "IN points",
    "KILL points",
]

# Function to execute JQL and return results as a DataFrame
def execute_jql(jql):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    auth = (jira_username, jira_api_token)
    url = f"{jira_url}/rest/api/3/search"
    params = {"jql": jql, "maxResults": 1000}  # Adjust maxResults as needed
    response = requests.get(url, headers=headers, auth=auth, params=params)
    response.raise_for_status()
    issues = response.json()["issues"]
    
    data = []
    for issue in issues:
        data.append({
            "key": issue["key"],
            "summary": issue["fields"]["summary"],
            "status": issue["fields"]["status"]["name"],
            # Add more fields as needed
        })
    return pd.DataFrame(data)

# Execute JQLs for each project and print results in the desired format
for project, jqls in projects.items():
    print(f"{project}\n")
    for i, jql in enumerate(jqls):
        result = execute_jql(jql)
        print(f"{jql_labels[i]}|{jql}|result")
        print(result)
        print("\n")
    print("\n")

# Function to execute JQL and return results as a DataFrame
def execute_jql(jql):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    auth = (jira_username, jira_api_token)
    url = f"{jira_url}/rest/api/3/search"
    params = {"jql": jql, "maxResults": 0}  # Adjust maxResults as needed
    response = requests.get(url, headers=headers, auth=auth, params=params)
    response.raise_for_status()
    issues = response.json()["issues"]
    
    data = []
    story_points_total = 0
    for issue in issues:
        story_points = issue["fields"]["customfield_10002"]
        story_points_total += story_points
        data.append({
            "key": issue["key"],
            "storyPoints": story_points,
        })
    print(f"Total story points: {story_points_total}")
    return pd.DataFrame(data)

