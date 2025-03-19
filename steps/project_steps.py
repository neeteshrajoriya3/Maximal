from pytest_bdd import scenario,then,when,given
import logging

@scenario("../features/project.feature", "Fetch all users")
def test_fetch_all_projects():
    pass

@given("I have access to Jira project management")
def jira_user_access():
    logging.info("Accessing JIRA")
    logging.info(f"Projects fetched: {fetch_all_project}")

@then("I should get a list of projects")
def verify_project_fetch():
    assert isinstance(fetch_all_project, list)