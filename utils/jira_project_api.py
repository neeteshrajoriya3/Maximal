import json
import logging
import requests
import yaml
import os
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

        def load_config():
            """Force reload the latest config.yaml every time it's called."""
            with open("config.yaml", "r") as f:
                return yaml.safe_load(f)

        # Call load_config() each time you need the config
        self.config = load_config()

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
            self.logger.error(f"Unexpected error in get_project: {e}")
        return None

    def get_project(self, project_key):
        self.logger.info("Initiating get_project")
        url = self.get_url("GET_Get_project", project_key)

        try:
            response = requests.get(url, auth=self.auth)
            status_code = response.status_code
            response_data = response.json()
            self.logger.info(f"Project retrieved: {status_code}")
            self.logger.info(response.json())
            # self.logger.info(f"status_code: {status_code}")
            return response
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

    def create_project(self, key, description):
        self.logger.info("Initiating project creation")
        url=self.get_url("POST_Create_project")

        payload={
            "key": key,
            "description": description,
            "leadAccountId": "712020:ca1ae7f1-3fce-4238-b039-fa6332bcd5d0",
            "name": self.config["jira"]["new_project"]["name"],
            "projectTemplateKey": self.config["jira"]["new_project"]["projectTemplateKey"],
            "projectTypeKey": self.config["jira"]["new_project"]["projectTypeKey"]
        }
        try:

            response=requests.post(url, auth=self.auth, json= payload)
            # self.logger.info(f"Request sent: {response.status_code}")
            data=response.json()
            self.logger.info(f"{response.text}")
            project_key=data.get("key")
            self.logger.info(f"Project Key: {project_key}")
            self.config["jira"]["new_project"]["id"] = data.get("id")

            with open("config.yaml","w") as file:
                yaml.safe_dump(self.config,file,default_flow_style=False,sort_keys=False)
                self.logger.info(f"Project ID {data.get("id")} saved in Config.yaml for further use")

            return response.status_code
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error in get_project: {e}")
        return None
    def update_project(self, key):
        self.logger.info("Initiating Update project")
        response = self.get_project(key)
        print(f"This is response from update_project method: {response}")
        if response is None:
            self.logger.error("Failed to retrieve project. Cannot proceed with update.")
            return response
        else:

            try:
                url=self.get_url("PUT_Update_project",key)
                payload={
                    "name": self.config["jira"]["new_project"]["name"]
                }
                response=requests.put(url, json=payload, auth=self.auth)
                self.logger.info("utils.update_project: Project updated")
                return response
            except Exception as e:
                self.logger.info(f"util.update_project:Unexpected error has occurred while updating project: {e}")
                return None
    def get_recent_projects(self):
        self.logger.info("Initiating get_recent_projects")
        try:
            url=self.get_url("GET_Get_recent_projects")
            response=requests.get(url, auth=self.auth)
            self.logger.info("utils.get_recent_projects: List of recent projects:\n")
            self.logger.info(response.json())
            return response
        except Exception as e:
            self.logger.info(f"util.get_recent_projects: Recent projects are not available: {e}")
            return None

    def get_projects_paginated(self, startAt, maxResults):
        self.logger.info("Initiating get_projects_paginated")
        params= {
            "startAt": startAt,
            "maxResults": maxResults
        }
        url = self.get_url("GET_Get_projects_paginated")

        try:
            url=self.get_url("GET_Get_projects_paginated")
            print(url)
            response=requests.get(url, params=params,auth=self.auth)
            json_data=response.json()

           # len(json_data['values']))
            return response.json()
        except Exception as e:
            self.logger.info(f"get_projects_paginated: Unable to fetch projects: {e}")
            return None
