import logging
import os.path
from requests.auth import HTTPBasicAuth
import pytest
import yaml
import requests
from utils.customlogger import LogGen


class JIRAProjectTypeAPI:
    def __init__(self, config_path="config.yaml"):
        self.logger=LogGen.loggen()
        ##Load config from config.yaml
        def load_config():
            base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_path=os.path.join(base_dir,"config.yaml")
            with open(config_path,"r") as file:
                return yaml.safe_load(file)
        # Call load_config() each time you need config
        self.config=load_config()
        self.jira_url=self.config["jira"]["base_url"]
        self.auth=HTTPBasicAuth(self.config["jira"]["email"],self.config["jira"]["api_token"])
        self.logger.info("JIRAProjectTypeAPI intiated successfully")

    def get_all_project_types(self):
        self.logger.info("Inside get_all_project_types")
        from conftest import get_url
        url=get_url("GET_Get_all_project_types")
        try:
            response=requests.get(url, auth=self.auth)
            if response:
                self.logger.info(response)
                return response
            else:
                return None
        except requests.exceptions.RequestException as e:
            return e
        except Exception as e:
            return e

    def get_licensed_project_types(self):
        self.logger.info("Inside get_licensed_project_types")
        from conftest import get_url
        url=get_url("GET_Get_licensed_project_types")
        try:
            response=requests.get(url, auth=self.auth)
            if response:
                self.logger.info(response)
                return response
            else:
                return None
        except requests.exceptions.RequestException as e:
            return e
        except Exception as e:
            return e
    def get_project_type_by_key(self,key):
        self.logger.info("Inside get_project_type_by_key")
        from conftest import get_url
        url=get_url("GET_Get_project_type_by_key",key)
        try:
            response=requests.get(url, auth=self.auth)
            if response:
                return response
        except requests.exceptions.RequestException as e:
            return e
        except Exception as e:
            return e
    def get_accessible_project_type_by_key(self,key):
        self.logger.info("Inside get_accessible_project_type_by_key")
        from conftest import get_url
        url=get_url("GET_Get_accessible_project_type_by_key",key)
        try:
            response=requests.get(url, auth=self.auth)
            if response:
                return response
            else:
                return None
        except requests.exceptions.RequestException as e:
            return e
        except Exception as e:
            return e


