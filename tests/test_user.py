import requests
import yaml
import pytest
from pytest_bdd import scenario, given,when,then, parsers
import logging
from utils.customlogger import LogGen
from utils.data_configuration import configuration
from utils.jira_user_api import JiraUserAPI

# logger=LogGen.loggen()
@pytest.fixture(scope="session")
def jira_api():
    return JiraUserAPI()

# def test_create_user(jira_api):
#     jira_api.logger.info("Starting execution of test_create_user")
#     user_email=jira_api.config["jira"]["user_api"]["user_email_for_creation"] #when step
#     response=jira_api.create_user(user_email) #when step
#     if response is not None: #then
#         jira_api.logger.info(response.json())#then
#     assert response.status_code is 201,"Test Failed"#then

##Defining scenario for create user feature:

@scenario(".\\features\\user.feature", "Create a user")
@pytest.fixture()
def context():
    return()

##Step definition begins here
# @given("I have access to Jira project management")
@given(parsers.parse("I have access to Jira project management"))
def access_to_jira():
    jira_api().logger.info("Given: I have access to Jira project management")

@when("I have a user for user creation"):
def create_jira_user(jira_api):
