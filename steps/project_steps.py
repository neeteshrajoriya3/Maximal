from pytest_bdd import scenario,then,when,given
import logging

@scenario("../features/project.feature", "Fetch all projects")
def test_fetch_all_projects():
    pass

@given("I have access to Jira project management")
def jira_user_access():
    logging.info("Accessing JIRA")
    logging.info(f"Projects fetched: {fetch_all_project}")

@then("I should get a list of projects")
def verify_project_fetch():
    assert isinstance(fetch_all_project, list)

@scenario("../features/project.feature", "Delete project with Key")
def fetch_project_key():
    logging.info("Project Key fetched")

@when("I delete the Project")
def delete_project_key():
    logging.info(f"Deleting Project by Key: {delete_project_by_key}")

@then("The Project should get deleted")
def verify_project_deleted():
    logging.info(f"Deleted Project by Key: {verify_project_key}" )

@scenario("../features/project.feature", "Fetch Project")

@given("I have Project Key")
def search_project(project_key):
    logging.info(f"Searching Project with Key: {project_key}")

@when("I delete the Project")
def delete_project(project_key):
    logging.info(f"Deleting Project: {project_key}")

@then("The Project should get deleted")
def verify_project_deleted(project_key):
    logging.info(f"Project deleted: {project_key}")