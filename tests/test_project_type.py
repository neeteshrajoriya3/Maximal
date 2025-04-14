import requests
import yaml
from utils.jira_project_types_api import JIRAProjectTypeAPI
from types import SimpleNamespace
from pytest_bdd import scenario, given,when,then
import pytest

@scenario("../features/project_types.feature","Get all project types")
def test_get_all_project_types():
    pass
@given("I have access to JIRA")
def access_to_jira():
    pass
@when("I search for project types")
def get_all_project_types(jira_project_types: JIRAProjectTypeAPI, context: SimpleNamespace):
    jira_project_types.logger.info("Inside test_get_all_project_types/when")
    response=jira_project_types.get_all_project_types()
    context.response=response
@then("I get a list of all project types")
def verify_all_project_types(jira_project_types: JIRAProjectTypeAPI, context: SimpleNamespace):
    jira_project_types.logger.info("inside test_get_all_project_types/then")
    response=context.response
    jira_project_types.logger.info(response.text)
    assert response is not None,f"Cannot display project types"
    assert response.status_code==200, f"Cannot display project types: {response.status_code}: {response.text}"

@scenario("../features/project_types.feature","Get licensed project types")
def test_get_licensed_project_type():
    pass
@when("I search for licensed project types")
def get_licensed_project_type(jira_project_types:JIRAProjectTypeAPI, context:SimpleNamespace):
    jira_project_types.logger.info("inside test_get_licensed_project_type/when")
    response=jira_project_types.get_licensed_project_types()
    context.response=response

@then("I get a list of all licensed project types")
def verify_licensed_project_type(jira_project_types:JIRAProjectTypeAPI, context:SimpleNamespace):
    jira_project_types.logger.info("Inside test_get_licensed_project_type/then")
    response=context.response
    assert response is not None,f"No response received from API"
    assert response.status_code==200, f"Unable to display licensed projects: {response.status_code} - {response.text}"

@scenario("../features/project_types.feature","Get Project Type by key")
def test_get_project_type_by_key():
    pass
@when("I search for project type by key")
def get_project_types_by_key(jira_project_types:JIRAProjectTypeAPI,context:SimpleNamespace):
    jira_project_types.logger.info("Inside test_get_project_type_by_key/when")
    key=jira_project_types.config["jira"]["Project_type"]["Project_type_key"]
    response=jira_project_types.get_accessible_project_type_by_key(key)
    context.response=response
@then("I get a list of all project types by key")
def verify_project_type_by_key(jira_project_types:JIRAProjectTypeAPI, context:SimpleNamespace):
    jira_project_types.logger.info("Inside test_get_project_type_by_key/then")
    response=context.response
    assert response is not None,f"No response from API"
    assert response.status_code==200,f"Not able to show project type: {response.status_code} - {response.text}"

@scenario("../features/project_types.feature","Get accessible project type by key")
def test_get_accessible_project_type_by_key():
    pass
@when("I search for accessible project type by key")
def get_accessible_project_type_by_key(jira_project_types:JIRAProjectTypeAPI, context: SimpleNamespace):
    jira_project_types.logger.info("Inside get_accessible_project_type_by_key/when")
    key=jira_project_types.config["jira"]["Project_type"]["Project_type_key"]
    response=jira_project_types.get_accessible_project_type_by_key(key)
    context.response=response
@then("I get a list of all accessible project types")
def verify_accessible_project_type_by_key(jira_project_types: JIRAProjectTypeAPI, context:SimpleNamespace):
    jira_project_types.logger.info("Inside test_get_accessible_project_type_by_key/then")
    response=context.response
    jira_project_types.logger.info(f"Response for Accessible Project Type: {response}")
    assert response is not None,f"No response from API"
    assert response.status_code==200,f"Unable to display project type: {response.status_code} - {response.text}"