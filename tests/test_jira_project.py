# test_jira_project.py
import pytest
from pytest_bdd import scenario, given, when, then
from types import SimpleNamespace
from conftest import generate_fake_text
from utils.jira_project_api import JiraProjectAPI

# --- Scenario Test Functions ---
@scenario("../features/test.feature", "Get all Projects")
def test_get_all_projects():
    pass


@scenario("../features/test.feature", "Fetch a Project")
def test_fetch_project():
    pass

# --- Step Definitions ---
@given("i have access to JIRA")
def access_jira(jira_api):
    pass

@when("user search for projects")
def search_all_projects(jira_api: JiraProjectAPI, context: SimpleNamespace):
    response = jira_api.get_all_projects()
    context.response = response

@when("user search for a project")
def search_project_by_key(jira_api: JiraProjectAPI, context: SimpleNamespace):
    key = jira_api.config["jira"]["project"]["key"]
    response = jira_api.get_project(key)
    context.response = response

@then("user gets a list of all projects")
def verify_all_projects(context: SimpleNamespace):
    response = context.response
    assert isinstance(response, list), "Expected list of projects"
    assert len(response) > 0, "No projects returned"

@then("projects details should be displayed")
def verify_project_response(context: SimpleNamespace):
    response = context.response
    assert isinstance(response, list), "Expected list of projects"
    assert response is not None, "Unable to fetch project"
    assert len(response)>0

@scenario("../features/test.feature","Create a Project")
def test_create_project():
    pass
@given("i have access to JIRA")
def access_to_jira():
    pass
@when("user creates a project")
def create_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    key=generate_fake_text("word").upper()
    print(f"Key is {key}")
    description=generate_fake_text("sentence").upper()
    print(f"description is {description}")
    response=jira_api.create_project(key,description)
    context.response=response
@then("a new project should get created")
def verify_project(jira_api:JiraProjectAPI, context:SimpleNamespace):
    response=context.response
    assert response == 201, f"Project creation failed {response}"

@scenario("../features/test.feature", "Delete a Project")
def test_delete_project():
    pass
@when("user deletes a project")
def delete_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    key = jira_api.config["jira"]["project"]["key"]
    project_status_code = jira_api.delete_project(key)
    context.response=project_status_code
    print(f"This is response from context.response from when: {context.response}")
@then("project should get deleted")
def verify_deleted_project(context:SimpleNamespace):
    response=context.response
    print(f"test_delete_project/then: This is response of context in then: {response}")
    if response in [200,204]:
        assert True
    elif response==404:
        assert False,f"test_delete_project/then: Project is not found. Check Project key again"
    elif response==401:
        assert False,f"test_delete_project/then: User is not authorized to delete Project"

@scenario("../features/test.feature","Get recent project")
def test_get_recent_projects():
    pass
@when("user search for recent projects")
def search_recent_projects(jira_api:JiraProjectAPI, context:SimpleNamespace):
    jira_api.logger.info("Inside search_recent_projects/when")
    response=jira_api.get_recent_projects()
    context.response=response
@then("a list of recent projects is displayed")
def verify_recent_projects(context:SimpleNamespace):
    response=context.response
    assert response.status_code==200,f"search_recent_projects/then: Unable to show recent projects: {response.status_code} "

@scenario("../features/test.feature","Get projects paginated")
def test_paginated_projects():
    pass
@when("user search for projects")
def search_projects(jira_api:JiraProjectAPI, context: SimpleNamespace):
    jira_api.logger.info("Inside search_projects/when")
    context.startAt=0
    context.maxResults=10
    response=jira_api.get_projects_paginated(context.startAt,context.maxResults)
    context.response=response
@then("a paginated list of projects is displayed")
def verify_paginated_projects(context:SimpleNamespace):
    response=context.response
    data=response.json()
    value_of_isLast=data.get("isLast")
    value_of_maxResults=data.get("maxResults")
    assert value_of_isLast==context.startAt,f"verify_paginated_projects/then: Value of isLast not matching:{value_of_isLast}"
    assert value_of_maxResults==context.maxResults, f"verify_paginated_projects/then: Value of maxResults not matching:{value_of_maxResults}"

@scenario("../features/test.feature","Update Project")
def test_update_project():
    pass
@when("I update a project")
def update_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    jira_api.logger.info("test_update_project/when: Inside when")
    key=jira_api.config["jira"]["new_project"]["key"]
    response=jira_api.update_project(key)
    context.response=response
    jira_api.config["jira"]["new_project"]["name"]="Neetesh"

@then("project should get updated")
def verify_update_project(context:SimpleNamespace):
    response=context.response
    print(f"This is response of update: {response}")
    assert response is not None,f"verify_update_project/then: Cannot update project: {response.status_code}"
    assert response.status_code==200,f"verify_update_project/then: Cannot update project:{response.status_code}"

@scenario("../features/test.feature","Archive Project")
###This will not work as user does not have the necessary permissions.
def test_archive_project():
    pass
@when("I archive a project")
def archive_project(jira_api:JiraProjectAPI, context:SimpleNamespace):
    jira_api.logger.info("Inside test_archive_project/when")
    key=jira_api.config["jira"]["new_project"]["key"]
    response=jira_api.archive_project(key)
    context.response=response
@then("project should get archived")
def verify_archive_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    jira_api.logger.info("Inside verify_archive_project/then")
    response=context.response
    if response.status_code==204:
        assert True
    elif response.status_code in [400,401,403,404]:
        assert False,f"Project cannot be archived: {response.status_code} - {response.text}"

@scenario("../features/test.feature","Delete Project asynchronously")
def test_delete_project_asynchronously():
    pass
@when("I delete project synchronously")
def delete_project_asynchronously(jira_api:JiraProjectAPI,context:SimpleNamespace):
    jira_api.logger.info("inside delete_project_asynchronously/when")
    key=jira_api.config["jira"]["new_project"]["key"]
    response=jira_api.delete_project_asynchronously(key)
    context.response=response
@then("project gets deleted synchronously")
def verify_delete_project_asynchronously(context:SimpleNamespace, jira_api:JiraProjectAPI):
    jira_api.logger.info("Inside verify_delete_project_asynchronously/then")
    response=context.response
    assert response is not None,f"There is no response: {response}"
    assert response.status_code==303,f"Project cannot be deleted:{response.status_code}"

@scenario("../features/test.feature","Restore Project")
def test_restore_project():
    pass
@when("I restore the project")
def restore_project(jira_api:JiraProjectAPI, context:SimpleNamespace):
    jira_api.logger.info("Inside test_restore_project/when")
    key=jira_api.config["jira"]["new_project"]["key"]
    response=jira_api.restore_project(key)
    context.response=response
@then("project should get restored")
def verify_restore_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    jira_api.logger.info("Inside test_restore_project/then")
    response=context.response
    assert response is not None,f"Cannot restore project: {response.status_code}"
    assert response.status_code==200,f"Cannot restore project: {response.status_code} : {response.text}"

@scenario("../features/test.feature","Get Statuses of Project")
def test_get_project_status():
    pass
@when("I search for statuses of project")
def search_status_of_project(jira_api:JiraProjectAPI, context: SimpleNamespace):
    jira_api.logger.info("Inside test_get_project_status/when")
    key=jira_api.config["jira"]["new_project"]["key"]
    response=jira_api.get_statuses_for_project(key)
    context.response=response
@then("I get a list of all project statuses")
def verify_status_of_project(jira_api:JiraProjectAPI, context:SimpleNamespace):
    response=context.response
    assert response.status_code==200, f"Cannot fetch statuses for project: {response.status_code}"

@scenario("../features/test.feature","Get project issue type")
def test_issue_type_of_project():
    pass
@when("I search for issue types for project")
def search_issue_types_of_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    jira_api.logger.info("Inside test_issue_type_of_project/when")
    id=jira_api.config["jira"]["new_project"]["id"]
    response=jira_api.get_project_issue_type_hierarchy(id)
    context.response=response
@then("I get a list of all issue types")
def verify_issuetype_of_project(jira_api:JiraProjectAPI, context: SimpleNamespace):
    jira_api.logger.info("Inside of test_issue_type_of_project/then")
    response=context.response
    assert response is not None,f"There is no response from API"
    assert response.status_code == 200,f"There is no response: {response.status_code} - {response.text}"

@scenario("../features/test.feature","Get project notification scheme")
def test_get_notification_scheme_for_project():
    pass
@when("I search for notification scheme for project")
def search_notification_scheme_for_project(jira_api:JiraProjectAPI, context:SimpleNamespace):
    jira_api.logger.info("Inside of test_get_notification_scheme_for_project/when")
    key=jira_api.config["jira"]["new_project"]["key"]
    response=jira_api.get_project_notification_scheme(key)
    context.response=response
@then("I get a list of all notification scheme")
def verify_notification_scheme_for_project(jira_api:JiraProjectAPI,context:SimpleNamespace):
    jira_api.logger.info("Inside of test_get_notification_scheme_for_project/then")
    response=context.response
    assert response is not None,f"There is no response from API"
    assert response.status_code==200,f"There is no response: {response.status_code} - {response.text}"