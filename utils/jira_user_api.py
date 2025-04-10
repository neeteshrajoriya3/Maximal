import pytest
import logging
from utils.customlogger import LogGen
import requests
import yaml
from requests.auth import HTTPBasicAuth
from utils.data_configuration import configuration

class JiraUserAPI:
    def __init__(self, config_path="config.yaml"):
        self.logger=LogGen.loggen()
        self.config=configuration.load_config_read()
        self.jira_url=self.config["jira"]["base_url"]
        self.auth = HTTPBasicAuth(self.config["jira"]["email"], self.config["jira"]["api_token"])
        self.logger.info("JiraUserAPI initialized successfully.")

    def get_url(self,endpoint_key):
        endpoint=self.config["jira"]["user_api"][endpoint_key]
        return f"{self.jira_url}{endpoint}"
    def get_user(self,accountid):
        self.logger.info("Initiating JIRAUserAPI::get_user")
        url=self.get_url("GET_Get_user")
        payload={
            "accountId" : accountid
        }
        try:
            response=requests.get(url, auth=self.auth, json=payload)
            self.logger.info(f"Response from request: {response.status_code}, {response.text}")
            if response is not None:
                try:
                    return response
                except Exception as e:
                    return e
            else:
                return None
        except requests.exceptions.RequestException as e:
            return e





    def create_user(self, email):
        self.logger.info("Initiating create_user from utils")
        url=self.get_url("POST_Create_user")
        print(url)
        url="https://neeteshrajoriya3.atlassian.net/rest/api/3/user"
        payload={
            "emailAddress":"pa@yopmail.com",
            "products": []
        }
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response=requests.post(url, auth=self.auth, json=payload, headers=headers)
            self.logger.info(f"Status code for response: {response.status_code}")
            self.logger.info(response.json())
            return response
        except requests.exceptions.RequestException as e:
            return e
        except Exception as e:
            return e


    #
    # def delete_user(self):
    #     pass
    #
    # def get_bulk_users(self):
    #     pass
    #
    # def get_account_ids_for_users(self):
    #     pass
    #
    # def get_user_details_columns(self):
    #     pass
    #
    # def set_user_details_columns(self):
    #     pass
    #
    # def reset_user_details_coulmn():
    #     pass
    #
    # def get_user_email():
    #     pass
    #
    # def get_user_email_bulk():
    #     pass
    #
    # def get_user_groups():
    #     pass
    #
    # def get_all_users_default():
    #     pass
    #
    # def get_all_users():
    #     pass
