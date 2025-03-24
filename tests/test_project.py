import logging
import pytest
from utils.jira_project_api import JiraProjectAPI
import yaml

# Loading configuration from config yaml
with open("config.yaml", "r") as file:
    config=yaml.safe_load(file)

@pytest.fixture(scope="module")
def jira_api():
    return JiraProjectAPI()

def test_get_all_projects(jira_api):
    """Test to fetch all users from Jira."""
    projects = jira_api.get_all_projects()
    assert isinstance(projects, list)  # ✅ Ensure the result is a list
    assert len(projects) > 0  # ✅ Ensure there is at least one user


def test_delete_project_by_key(jira_api):
    key = config["jira"]["project"]["key"]
    project_status_code = jira_api.get_project(key)
    if project_status_code== 200:
        logging.info(f"Project key/ID is available for deletion: {key}. Starting deletion of Project")
        deletion_result=jira_api.delete_project(key)
    else:
        logging.info(f"Project is not found for deletion. Stopping execution for deletion")
    if deletion_result in [200,201]:
        logging.info(f"Project deleted successfully. Project key: {key}")
    else:
        logging.info(f"Error occured while deleting the project.")

def test_restore_project(jira_api):
    key = config["jira"]["project"]["key"]
    project_status_code = get_project(key)
    if project_status_code == 200:
        logging.info(f"Project already present: {key}. Stopping execution")
    else:
        logging.info(f"Project Key Found: {key}")
        response=jira_api.restore_project(key)

        assert response == 200