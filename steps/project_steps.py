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

@scenario("../features/projeect.feature", "Restore deleted or archived project")
@given("I have Project key")
def search_project(project_key):
    logging.info(f"Searching Project: {project_key}")

@when("I restore the Project")
def restore_project(project_key):
    logging.info(f"Restoring Project: {project_key}")

@then("The Project should be visible in the list")
def verify_project_in_list(project_key):
    logging.info(f"Project Restored: {project_key}")

@scenario("../features/project.feature", "Create a project")

@given("I have access to Jira project management")
def jira_user_access():
    logging.info("Accessing JIRA")

@when("I create a project")
def create_project():
    logging.info("Creating a project")

@then("The project should get created")
def create_project():
    logging.info("Project got created")

@scenario("../features/project.feature", "Update a Project")

@given("I have access to Jira project management")
def jira_user_access():
    logging.info("Accessing JIRA")
@when("I update a project")
def update_project():
    logging.info("Updating project")

@then("The project should get updated")
def update_project():
    logging.info("Project updated")

@scenario("../features/project.feature", "Get Recent Project")
@given("I have access to Jira project management")
def jira_user_access():
    logging.info("Accessing JIRA")

@when("I search for recent projects")
def get_projects():
    logging.info("Searching recent projects")

@then("I get a list of recent projects viewed by user")
def show_projects():
    logging.info("Showing recent projects")

