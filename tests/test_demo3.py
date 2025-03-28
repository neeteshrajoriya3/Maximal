import logging
import pytest
from utils.demo2 import JiraProjectAPI
from utils.demo2 import JiraProjectAPI
import yaml

# Loading configuration from config yaml
# with open("config.yaml", "r") as file:
#     config=yaml.safe_load(file)

@pytest.fixture(scope="module")
def jira_api():
    return JiraProjectAPI()

def test_get_all_projects(jira_api):
    jira_api.logger.info("Hello World")