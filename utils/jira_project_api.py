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
    logging.info("Initiating get_all_projects")
    url=f"{JIRA_URL}{GET_ALL_PROJECT}"
    response=requests.get(url,auth=AUTH)
    logging.info(f"Response from fetching projects: {response.status_code} - {response.text}")
    logging.info("Ended execution of get_all_projects. Returning response.json")
    return response.json()

def get_project(project_key):
    logging.info("Initiating get_project")
    config["jira"]["project_api"]["GET_Get_project"] += str(project_key)
    GET_PROJECT=config["jira"]["project_api"]["GET_Get_project"]
    print(GET_PROJECT)
    url=f"{JIRA_URL}{GET_PROJECT}"
    response=requests.get(url,auth=AUTH)
    logging.info("Ended execution of get_project. Returning response.status_code")
    #print(f"Status code from util: {response.status_code}")
    return response.status_code

def delete_project(project_key):
    logging.info("Initiating delete_project")
    config["jira"]["project_api"]["DEL_Delete_project"] += str(project_key)
    DELETE_PROJECT=config["jira"]["project_api"]["DEL_Delete_project"]
    url=f"{JIRA_URL}{DELETE_PROJECT}"
    response=requests.delete(url,auth=AUTH)
    logging.info(f"Ended execution of delete_project. Project deleted: {project_key}")
    return response.status_code

def restore_project(project_key):
    logging.info("Initiating restore_project")
    RESTORE_PROJECT=config["jira"]["project_api"]["POST_Restore_deleted_or_archived_project"]
    RESTORE_PROJECT1=RESTORE_PROJECT.replace("{projectIdOrKey}",project_key)
    url=f"{JIRA_URL}{RESTORE_PROJECT1}"
    response=requests.post(url,auth=AUTH)
    logging.info(f"Ended execution of restore_project. Project Restored: {project_key}")
    return response.status_code

def delete_project_by_key(project_key):
    pass

def create_project(project_name, project_key, lead_email):
    pass

