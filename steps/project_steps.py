import logging
import pytest
from utils.jira_project_api import JiraProjectAPI
import yaml
import logging

@pytest.fixture
def jira_api():
    return JiraProjectAPI()


def test_four(jira_api):
    b=jira_api.get_all_projects()

def test_five(jira_api, key):
    c= jira_api.delete_project(key)
    jira_api.logger.info("some message")
    print(c)



