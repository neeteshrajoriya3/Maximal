import requests
import yaml
from requests.auth import HTTPBasicAuth
import logging

# Load configuration
with open("config.yaml","r") as file:
    config=yaml.safe_load(file)

JIRA_URL=config["jira"]["base_url"]
AUTH=HTTPBasicAuth(config["jira"]["email"],config["jira"]["api_token"])
PROJECT_KEY=config["jira"]["project_key"]
SEARCH_JQL=config["jira"]["search_jql"]

# Configure logging
logging.basicConfig(filename="logs/test_log.log",level=logging.INFO)

def create_issue(summary, description, issue_type="Task"):
    """Creates an issue in Jira under the specified project."""
    url=f"{JIRA_URL}/rest/api/3/issue"
    payload = {
        "fields":{
            "project": {"key": PROJECT_KEY},
            "summary":summary,
            "description":description,
            "issueType": {"name": issue_type}
        }
    }
    response=requests.post(url, json=payload, auth=AUTH)
    logging.info(f"Issue creation response: {response.status_code} - {response.text}")
    return response.json()

def search_issue(jql_query=None):
    """Searches for Jira issues using the provided JQL query or default from config.yaml."""
    if jql_query is None:
        jql_query = config["jira"]["search_jql"]  # ✅ Fetch JQL dynamically

    url = f"{JIRA_URL}/rest/api/3/search?jql={jql_query}"
    response = requests.get(url, auth=AUTH)

    logging.info(f"Issue search response: {response.status_code} - {response.text}")

    return response.json()

