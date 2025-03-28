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
    jira_api.logger.info("Project details fetched")
    # assert isinstance(projects, list)  # ✅ Ensure the result is a list
    # assert len(projects) > 0  # ✅ Ensure there is at least one user


def test_delete_project_by_key(jira_api):
    key = config["jira"]["project"]["key"]
    project_status_code = jira_api.get_project(key)
    jira_api.logger.info(f"Value of project_status_code: {project_status_code}")
    deletion_result=None
    if project_status_code== 200:
        jira_api.logger.info(f"Project key/ID is available for deletion: {key}. Starting deletion of Project")
        deletion_result=jira_api.delete_project(key) #status is returned by method
        #jira_api.logger.info(f"Value of deletion_result: {deletion_result}")
    else:
        jira_api.logger.info(f"Project is not found for deletion. Stopping execution for deletion")
        assert False
    if deletion_result == 204:
        logging.info(f"Project deleted successfully. Project key: {key}")
    else:
        jira_api.logger.info(f"Error occurred while deleting the project.")
        assert False

def test_restore_project(jira_api):
    key = config["jira"]["project"]["key"]
    # project_status_code = jira_api.get_project(key)
    # print(project_status_code)
    jira_api.logger.info(f"Starting project restore: {key}")
    response_status_code=jira_api.restore_project(key)
    print(response_status_code)
    if response_status_code == 200:
        print(f"Project restored: {key}")
        jira_api.logger.info(f"Project restored successfully: {key}")
    else:
        jira_api.logger.info(f"Issue occurred in restoring project: {key}")
        print("Project was not restored")
        assert False

def test_get_project(jira_api):
    "method for getting detail for specific project data"
    #project_key_to_search=jira_api.config["jira"]["project"]["key"]
    project_key_to_search="PEDRO"
    jira_api.logger.info("Executing get project")
    print("executing get project")
    status_code, data=jira_api.get_project(project_key_to_search)
    jira_api.logger.info(f"The status code is: {status_code} and data is {data}")
    #print(f"The status code is: {status_code} and data is {data}")

def test_create_project(jira_api):
    key=jira_api.config["jira"]["new_project"]["key"]
    description=jira_api.config["jira"]["new_project"]["description"]
    jira_api.create_project(key, description)
    print("project created")