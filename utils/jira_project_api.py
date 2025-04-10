import json
import logging
import pytest
import requests
import yaml
import os
from utils.customlogger import LogGen
from requests.auth import HTTPBasicAuth
from utils.status_messages import STATUS_MESSAGES

class JiraProjectAPI:
    def __init__(self, config_path="config.yaml"):

        self.logger=LogGen.loggen()

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
            print(f"generated url: {self.jira_url}{endpoint}")
        return f"{self.jira_url}{endpoint}"

    def get_all_projects(self):
        self.logger.info("Initiating get_all_projects")

        url = self.get_url("GET_Get_all_projects")

        try:
            response = requests.get(url, auth=self.auth)
            self.logger.info(f"Response from fetching projects: {response.status_code} - {response.text}")
            status_code = response.status_code
            print(f"\nStatus code from utils {status_code}")

            if response is not None:
                try:
                    data = response  # Parse the JSON
                    self.logger.info(f"Response JSON: {data}")  # Log the parsed JSON
                    return data  # Return the parsed JSON data
                except ValueError as e:
                    self.logger.error(f"Error parsing JSON: {e}")
                    return None
            else:
                self.logger.warning(message)
                return None
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
            if status_code==200:
                self.logger.info(f"Project retrieved: {status_code}")
            else:
                self.logger.info(f"Project could not be retrieved: {status_code}")
            #self.logger.info(response.json())
            # self.logger.info(f"status_code: {status_code}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error: {e}")
            return None
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
    def archive_project(self, key):
        self.logger.info("Initiating archive_project")
        response_data=self.get_project(key)
        print(response_data.status_code)
        if response_data is None:
            print(f"None is returned from get project")
        if response_data.status_code==200:
            self.logger.info(f"archive_project:Project found. Archiving project: {key}")
            url = self.get_url("POST_Archive_project")
            print(url)
            try:
                response=requests.post(url, auth=self.auth)
                print(requests.post(url, auth=self.auth))
                self.logger.info(f"status code came from response: {response.status_code} ")
                return response.status_code

            except Exception as e:
                self.logger.info(f"archive_project: Unable to archive project: {e}")
                return None
        else:
            self.logger.info(f"archive_project: Project not found. Stopping execution")
        return None

    def delete_project_asynchronously(self,key):
        self.logger.info("Initiating delete_project_asynchronously")
        response_data=self.get_project(key)
        #print(response_data.json())
        if response_data.status_code==200:
            self.logger.info(f"Project found, deleting asynchronously: {key}")
            try:
                url=self.get_url("POST_Delete_project_asynchronously",key)
                response=requests.post(url,auth=self.auth)
                return response.status_code
            except Exception as e:
                self.logger.info(f"Could not delete the project: {e}")
                print(e)

    def get_statuses_for_project(self, key):
        self.logger.info("Initiating get_statuses_for_project")
        response_data=self.get_project(key)
        if response_data:
            self.logger.info(f"Project is found. Getting all statuses for project:{key}")
            if response_data.status_code==200:
                try:
                    url=self.get_url("GET_Get_all_statuses_for_project",key)
                    response=requests.get(url,auth=self.auth)
                    self.logger.info(response.json())
                    return response
                except Exception as e:
                    self.logger.info(f"Project couldn't be found: {e}")
                    return None
            else:
                self.logger.info(f"Project couldn't be found. Status Code:{response_data.status_code}")

    def get_project_issue_type_hierarchy(self, key):
        self.logger.info("Initiating get_project_issue_type_hierarchy")
        response_data = self.get_project(key)
        if response_data:
            self.logger.info(f"Project is found. Getting issue type hierarchy for project:{key}")
            if response_data.status_code == 200:
                try:
                    url = self.get_url("GET_Get_project_issue_type_hierarchy", key)
                    response = requests.get(url, auth=self.auth)
                    self.logger.info(response.json())
                    return response
                except Exception as e:
                    self.logger.info(f"Project couldn't be found: {e}")
                    return None
            else:
                self.logger.info(f"Project couldn't be found. Status Code:{response_data.status_code}")

    def get_project_notification_scheme(self,key):
        self.logger.info("Initiating get_project_notification_scheme")
        response_data = self.get_project(key)
        if response_data:
            self.logger.info(f"Project is found. Getting notification scheme for project:{key}")
            if response_data.status_code == 200:
                try:
                    url = self.get_url("GET_Get_project_notification_scheme", key)
                    response = requests.get(url, auth=self.auth)
                    self.logger.info(response.json())
                    return response
                except Exception as e:
                    self.logger.info(f"Project couldn't be found: {e}")
                    return None
            else:
                self.logger.info(f"Project couldn't be found. Status Code:{response_data.status_code}")
    def print_hello(self):
        h="Hello World"
        return h