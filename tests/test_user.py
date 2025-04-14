import requests
import pytest
from pytest_bdd import scenario, given, when, then
from utils.jira_user_api import JiraUserAPI

@scenario("../features/user.feature", "Create a user")
def some_function1():
    pass

@pytest.fixture()
def jira_apii():
    return JiraUserAPI()

@given("I have access to Jira project management")
def some_function1(jira_apii):
    p=jira_apii.get_url()

@when()