import logging
import requests
import yaml
from requests.auth import HTTPBasicAuth
from utils.status_messages import STATUS_MESSAGES

#from utils.jira_user_api import get_lead_account_id  # ✅ Import Lead Account ID function

class JiraProjectAPI:
    #class to interact with JIRA Project API

    def __init__(self, config_path="config.yaml"):
        # ✅ Load configuration from config.yaml
        with open(config_path,"r") as file:
            self.config=yaml.safe_load(file)
        self.jira_url=self.config["jira"]["base_url"]
        self.auth=HTTPBasicAuth(self.config["jira"]["email"],self.config["jira"]["api_token"])
        self.search_project_key=self.config["jira"]["project"]["key"]
        # GET_ALL_PROJECT=config["jira"]["project_api"]["GET_Get_all_projects"]
        # #PROJECT_KEY=config["jira"]["project"]["key"]

        # Configure logging
        logging.basicConfig(filename="logs/test_log.log", level=logging.INFO)

    def get_url(self,endpoint_key, project_key=None):
        # Helper Method to construct API URLs dynamically
        endpoint= self.config["jira"]["project_api"][endpoint_key]
        if project_key:
            endpoint=endpoint.replace("{projectIdOrKey}", str(project_key))
        return f"{self.jira_url}{endpoint}"
    def get_all_projects(self):
        ##fetches all projects available for signed user
        logging.info("Initiating get_all_projects")
        url=self.get_url("GET_Get_all_projects")

        try:

            response=requests.get(url,auth=self.auth)
            logging.info(f"Response from fetching projects: {response.status_code} - {response.text}")
            logging.info("Ended execution of get_all_projects. Returning response.json")
            status_code=response.status_code
            success, message=STATUS_MESSAGES.get(status_code, (False, f"Unexpected error: {status_code}: {response.text}"))
            logging.info(message) if success else logging.warning(message)
            return response.json() if success else None
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error in get_project: {e}")
        return None


    def get_project(self,project_key):
        logging.info("Initiating get_project")
        url=self.get_url("GET_Get_project",project_key)
        response=requests.get(url,auth=self.auth)
        logging.info("Ended execution of get_project. Returning response.status_code")
        #print(f"Status code from util: {response.status_code}")
        return response.status_code

    def delete_project(self, project_key):
        logging.info("Initiating delete_project")
        search_key=self.search_project_key
        url = self.get_url("DEL_Delete_project", project_key)
        response = requests.delete(url, auth=self.auth)
        logging.info(f"Ended execution of delete_project. Project deleted: {project_key}")
        return response.status_code

    def restore_project(self, project_key):
        logging.info(f"Ended execution of restore_project. Project Restored: {project_key}")
        url=self.get_url("POST_Restore_deleted_or_archived_project", project_key)
        response=requests.post(url, auth=self.auth)
        logging.info(f"Ended execution of restore_project. Project restored {project_key}")
        return response.status_code

    def delete_project_by_key(project_key):
        pass

    def create_project(project_name, project_key, lead_email):
        pass

