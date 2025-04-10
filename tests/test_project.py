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

@pytest.mark.project
def test_get_all_projects(jira_api):
    """Test to fetch all users from Jira."""
    projects = jira_api.get_all_projects()
    jira_api.logger.info(f"project details {projects}")
    print(f"\nProject is: {type(projects)}")
    if projects is None:
        jira_api.logger.error("Failed to fetch projects. The response was None.")
        assert False, "Failed to fetch projects (response is None)"
    jira_api.logger.info("Project details fetched")
    print(f"Type of Project: {type(projects)}")
    assert isinstance(projects.json(), list), f"response is not a list. its a {type(projects)}"  # ✅ Ensure the result is a list
    assert len(projects.json()) > 0, "get_project worked but there are no projects to show"  # ✅ Ensure there is at least one user

@pytest.mark.project
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
@pytest.mark.project
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
@pytest.mark.project
def test_get_project(jira_api):
    "method for getting detail for specific project data"
    #project_key_to_search=jira_api.config["jira"]["project"]["key"]
    project_key_to_search="RAM"
    jira_api.logger.info("Executing get project")
    print("executing get project")
    response=jira_api.get_project(project_key_to_search)
    jira_api.logger.info(f"The status code is: {response.status_code} and data is {response.json()}")
    #print(f"The status code is: {status_code} and data is {data}")
@pytest.mark.project
def test_create_project(jira_api):
    key=jira_api.config["jira"]["new_project"]["key"]
    description=jira_api.config["jira"]["new_project"]["description"]
    response=jira_api.create_project(key, description)
    assert response == 200, f"Project not created. Got Error code as {response}"
@pytest.mark.project
def test_update_project(jira_api):
    key=jira_api.config["jira"]["new_project"]["key"]
    print(key)
    response=jira_api.update_project(key)
    print(f"test_update_project: {response}")
    if response.status_code==200:
        data=response.json()
        print(f"test_update_project: This is value of name in response: {data.get("name")}")
        assert data.get("name")==jira_api.config["jira"]["new_project"]["name"]
    else:
        jira_api.logger.info("test_update_project: Project is not updated")
        assert False, f"Project not updated. Status code received from Response: {response.status_code}"
@pytest.mark.project
def test_get_recent_projects(jira_api):
    response=jira_api.get_recent_projects()
    assert response is not None, "test_get_recent_projects: Unable to display recent projects"
    assert len(response.json())<= 20, "More than 20 projects are showing"
@pytest.mark.project
def test_get_projects_paginated(jira_api):
    StartAt=0
    maxResults=5
    response=jira_api.get_projects_paginated(StartAt,maxResults)
    assert response is not None, "test_get_projects_paginated: Unable to fetch projects"
    assert len(response['values']) ==maxResults, "Number of projects are not equal to maxResults"
@pytest.mark.project
@pytest.mark.skip(reason="Dont have authorization. Always throw 405")
def test_archive_project(jira_api):
###This doesn't work as user is not authorized to use feature###
    key=jira_api.config["jira"]["project"]["key"]
    print(key)
    response=jira_api.archive_project(key)
    assert response==200, "test_archive_project: Unable to archive project"
@pytest.mark.project
def test_delete_project_asynchronously(jira_api):
    key=jira_api.config["jira"]["project"]["key"]
    response=jira_api.delete_project_asynchronously(key)
    assert response== 200, f"Project couldn't be deleted: {key}"
@pytest.mark.project
def test_get_statuses_for_project(jira_api):
    key = jira_api.config["jira"]["project"]["key"]
    response=jira_api.get_statuses_for_project(key)
    assert response.status_code==200, f"Project statuses couldn't be fetched: {response.status_code}"
@pytest.mark.project
def test_get_project_issue_type_hierarchy(jira_api):
    key=jira_api.config["jira"]["project"]["key"]
    response=jira_api.get_project_issue_type_hierarchy(key)
    assert response.status_code == 200, f"issue type hierarchy for project couldn't be fetched: {response.status_code}"
@pytest.mark.project
def test_get_project_notification_scheme(jira_api):
    key = jira_api.config["jira"]["project"]["key"]
    response = jira_api.get_project_notification_scheme(key)
    assert response.status_code == 200, f"Notification scheme for project couldn't be fetched: {response.status_code}"