from jira import JIRA

# Set up JIRA credentials
jira_url = "https://your_jira_url.com"
jira_username = "your_jira_username"
jira_password = "your_jira_password"

# Set up JIRA client
jira_client = JIRA(jira_url, basic_auth=(jira_username, jira_password))

# Execute JQL query
jql_query = "project = TEST"
issues = jira_client.search_issues(jql_query)

# Print results
for issue in issues:
    print(issue.key, issue.fields.summary)
