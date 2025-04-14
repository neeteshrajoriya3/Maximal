import pytest
from pytest_bdd import scenario, given, when, then
from utils.jira_project_api import JiraProjectAPI

# Define the scenario
@scenario("../features/simple.feature", "This is a Simple Feature")
def test_simple_feature():
    pass  # This function is needed for pytest-bdd to link the feature file

# Define a fixture that provides an instance of JiraProjectAPI
@pytest.fixture
def jira_api():
    return JiraProjectAPI()  # Create an instance

# Step Definitions
@given("I have a number")
def number_given(jira_api):
    # Example usage of jira_api instance
    print(f"Using Jira API instance: {JiraProjectAPI.print_hello()}")
    print()
@when("add number with 2")
def add_number(jira_api):
    a=JiraProjectAPI.get_all_projects()