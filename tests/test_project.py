import logging
import pytest
from utils.jira_project_api import JiraProjectAPI
import yaml

@pytest.fixture(scope="module")
def jira_api():
    return JiraProjectAPI()

def test_get_all_projects(jira_api):
    """Test to fetch all users from Jira."""
    projects = jira_api.get_all_projects()
    assert isinstance(projects, list)  # ✅ Ensure the result is a list
    assert len(projects) > 0  # ✅ Ensure there is at least one user


def test_delete_project_by_key():
    key = config["jira"]["project"]["key"]
    project_status_code = get_project(key)
    if project_status_code == 404:
        logging.info(f"Project Key Not Found: {key}")
    else:
        logging.info(f"Project Key Found: {key}")
        delete_project(key)


def test_restore_project():
    key = config["jira"]["project"]["key"]
    project_status_code = get_project(key)
    if project_status_code == 200:
        logging.info(f"Project already present: {key}. Stopping execution")
    else:
        logging.info(f"Project Key Found: {key}")
        response=restore_project(key)
        #print(response)
        assert response == 200

