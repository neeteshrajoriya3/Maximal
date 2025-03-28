# import pytest
# import yaml
# import logging
#
# from utils.jira_project_api import JiraProjectAPI
# from utils.jira_user_api import get_all_users, get_lead_account_id, search_user
# from utils.jira_issue_api import search_issue,create_issue
#
#
#
# with open("config.yaml","r") as file:
#     config=yaml.safe_load(file)
#
# @pytest.fixture(scope="session")
# def fetch_all_users():
#     """Fixture to fetch all users."""
#     return get_all_users()
#
# @pytest.fixture(scope="session")
# def search_specific_user():
#     """Fixture to search for a specific user."""
#     user_email=config["jira"]["test_user_email"]
#     return search_user(user_email)
#
# @pytest.fixture(scope="session")
# def setup_jira_project():
#     """Fixture to create a Jira project using a dynamic Lead Account ID."""
#     project_name=config["jira"]["project"]["name"]
#     project_key=config["jira"]["project"]["key"]
#     lead_email=config["jira"]["project"]["key"]
#     return create_project(project_name, project_key, lead_email)
#
# @pytest.fixture()
# def create_sample_issue():
#     """Fixture to create a sample issue using values from config.yaml."""
#     issue_summary=config["jira"]["project"]["issue"]["summary"]
#     issue_description=config["jira"]["project"]["issue"]["description"]
#     return create_issue(issue_summary,issue_description)
#
# @pytest.fixture()
# def fetch_latest_issues():
#     """Fixture to get the latest Jira issues using JQL from config.yaml."""
#     jql_query=config["jira"]["search_jql"]
#     return search_user(jql_query)
#
