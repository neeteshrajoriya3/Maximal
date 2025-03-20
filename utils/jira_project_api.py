import logging
import requests
import yaml
from requests.auth import HTTPBasicAuth
from utils.jira_user_api import get_lead_account_id  # ✅ Import Lead Account ID function

# ✅ Load configuration from config.yaml
with open("config.yaml","r") as file:
    config=yaml.safe_load(file)

JIRA_URL=config["jira"]["base_url"]
AUTH=HTTPBasicAuth(config["jira"]["email"],config["jira"]["api_token"])
GET_ALL_PROJECT=config["jira"]["project_api"]["GET_Get_all_projects"]
#PROJECT_KEY=config["jira"]["project"]["key"]

# Configure logging
logging.basicConfig(filename="logs/test_log.log", level=logging.INFO)

def get_all_projects(query="a"):  ##fetches all projects available for signed user
    url=f"{JIRA_URL}{GET_ALL_PROJECT}"
    response=requests.get(url,auth=AUTH)
    logging.info(f"Response from fetching projects: {response.status_code} - {response.text}")
    return response.json()

def get_project(project_key):
    GET_PROJECT=config["jira"]["project_api"]["GET_Get_project"]
    url=f"{JIRA_URL}{GET_PROJECT}"
    response=requests.get(url,auth=AUTH)
    return response

def delete_project(project_key):
    DELETE_PROJECT=config["jira"]["project_api"]["DEL_Delete_project"]
    url=f"{JIRA_URL}{DELETE_PROJECT}"
    response=requests.delete(url,auth=AUTH)
    return response

def delete_project_by_key(project_key):
    pass

def create_project(project_name, project_key, lead_email):
    pass

