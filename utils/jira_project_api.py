import logging
import requests
import yaml
from requests.auth import HTTPBasicAuth
from utils.status_messages import STATUS_MESSAGES

# Configure logging at the module level
logging.basicConfig(
    filename="logs/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger instance
logger = logging.getLogger(__name__)

class JiraProjectAPI:
    def __init__(self, config_path="config.yaml"):
        # ✅ Load configuration from config.yaml
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)
        self.jira_url = self.config["jira"]["base_url"]
        self.auth = HTTPBasicAuth(self.config["jira"]["email"], self.config["jira"]["api_token"])
        self.search_project_key = self.config["jira"]["project"]["key"]

        logger.info("JiraProjectAPI initialized successfully.")

    def get_url(self, endpoint_key, project_key=None):
        endpoint = self.config["jira"]["project_api"][endpoint_key]
        if project_key:
            endpoint = endpoint.replace("{projectIdOrKey}", str(project_key))
        return f"{self.jira_url}{endpoint}"

    def get_all_projects(self):
        logger.info("Initiating get_all_projects")
        url = self.get_url("GET_Get_all_projects")

        try:
            response = requests.get(url, auth=self.auth)
            logger.info(f"Response from fetching projects: {response.status_code} - {response.text}")
            status_code = response.status_code
            success, message = STATUS_MESSAGES.get(status_code, (False, f"Unexpected error: {status_code}: {response.text}"))
            logger.info(message) if success else logger.warning(message)
            return response.json() if success else None
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in get_project: {e}")
        return None

    def get_project(self, project_key):
        logger.info("Initiating get_project")
        url = self.get_url("GET_Get_project", project_key)

        try:
            response = requests.get(url, auth=self.auth)
            status_code = response.status_code
            response_data = response.json()
            logger.info(f"Project retrieved: {response_data}")
            return status_code, response_data
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in get_project: {e}")
        return None

    def delete_project(self, project_key):
        logger.info(f"Initiating delete_project: {project_key}")
        url = self.get_url("DEL_Delete_project", project_key)
        response = requests.delete(url, auth=self.auth)
        logger.info(f"Project deleted: {project_key}, Status Code: {response.status_code}")
        return response.status_code

    def restore_project(self, project_key):
        logger.info(f"Initiating restore_project: {project_key}")
        url = self.get_url("POST_Restore_deleted_or_archived_project", project_key)
        response = requests.post(url, auth=self.auth)
        logger.info(f"Project restored: {project_key}, Status Code: {response.status_code}")
        return response.status_code