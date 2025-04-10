import pytest
from utils.jira_project_api import JiraProjectAPI


@pytest.fixture(scope="session")
def jira_api():
    return JiraProjectAPI


# conftest.py (where you define your fixtures)
import pytest
# from your_database_module import DatabaseConnection

@pytest.fixture
def database_connection():
    """Fixture to establish a database connection."""
    connection = DatabaseConnection("your_db_url")
    yield connection  # Provide the connection to the tests
    connection.close()  # Teardown: close the connection

# feature/your_feature.feature
# Feature: Example using database

# Scenario: Verify data in the database
#   Given the database is initialized
#   Then the data should be present

# steps/your_steps.py
from pytest_bdd import given, then

@given("the database is initialized")
def initialize_database(database_connection):
    """Step definition that uses the database_connection fixture."""
    # Use the database_connection to perform initialization tasks
    database_connection.initialize_tables()

@then("the data should be present")
def verify_data(database_connection):
    """Step definition to verify data."""
    
    data = database_connection.fetch_data()

    assert len(data) > 0
