import logging
import os
import requests
import yaml
from requests.auth import HTTPBasicAuth
from utils.status_messages import STATUS_MESSAGES

class JiraProjectAPI:
    def __init__(self, config_path="config.yaml"):
        # ✅ Set up logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)  # Set logging level

        # ✅ Ensure the logs directory exists
        log_dir = os.path.join(os.path.dirname(__file__), "../logs")
        log_file = os.path.join(log_dir, "test_log.log")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # ✅ Create a file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)  # Capture all logs in the file

        # ✅ Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Show only INFO+ in terminal

        # ✅ Set formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # ✅ Avoid duplicate handlers
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

        # ✅ Load configuration from config.yaml
        with open("config.yaml", "r") as file:
            self.config = yaml.safe_load(file)
        self.jira_url = self.config["jira"]["base_url"]
        self.auth = HTTPBasicAuth(self.config["jira"]["email"], self.config["jira"]["api_token"])
        self.search_project_key = self.config["jira"]["project"]["key"]

        self.logger.info("JiraProjectAPI initialized successfully.")

    def get_url(self, endpoint_key, project_key=None):
        endpoint = self.config["jira"]["project_api"][endpoint_key]
        if project_key:
            endpoint = endpoint.replace("{projectIdOrKey}", str(project_key))
        return f"{self.jira_url}{endpoint}"

    def get_all_projects(self):
        self.logger.info("Initiating get_all_projects")
        url = self.get_url("GET_Get_all_projects")

        try:
            response = requests.get(url, auth=self.auth)
            self.logger.info(f"Response from fetching projects: {response.status_code} - {response.text}")
            status_code = response.status_code
            success, message = STATUS_MESSAGES.get(status_code, (False, f"Unexpected error: {status_code}: {response.text}"))
            self.logger.info(message) if success else self.logger.warning(message)
            return response.json() if success else None
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error in get_all_projects: {e}")
        return None

    def get_project(self, project_key):
        self.logger.info(f"Initiating get_project for project_key: {project_key}")
        url = self.get_url("GET_Get_project", project_key)

        try:
            response = requests.get(url, auth=self.auth)
            status_code = response.status_code
            response_data = response.json()
            self.logger.info(f"Project retrieved: {response_data}")
            return status_code, response_data
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error in get_project: {e}")
        return None

    def delete_project(self, project_key):
        self.logger.info(f"Initiating delete_project: {project_key}")
        url = self.get_url("DEL_Delete_project", project_key)
        response = requests.delete(url, auth=self.auth)
        self.logger.info(f"Project deleted: {project_key}, Status Code: {response.status_code}")
        return response.status_code

    def restore_project(self, project_key):
        self.logger.info(f"Initiating restore_project: {project_key}")
        url = self.get_url("POST_Restore_deleted_or_archived_project", project_key)
        response = requests.post(url, auth=self.auth)
        self.logger.info(f"Project restored: {project_key}, Status Code: {response.status_code}")
        return response.status_code