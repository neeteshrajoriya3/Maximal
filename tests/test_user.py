# import pytest
# import yaml
# from utils.jira_user_api import get_all_users, search_user
#
# # ✅ Load configuration from config.yaml
# with open("config.yaml", "r") as file:
#     config = yaml.safe_load(file)
#
#
# @pytest.mark.api  # ✅ API-related test
# @pytest.mark.user  # ✅ User-related test
# def test_get_all_users():
#     """Test to fetch all users from Jira."""
#     users = get_all_users()
#
#     assert isinstance(users, list)  # ✅ Ensure the result is a list
#     assert len(users) > 0  # ✅ Ensure there is at least one user
#
#
# @pytest.mark.api  # ✅ API-related test
# @pytest.mark.user  # ✅ User-related test
# def test_search_user():
#     """Test to search for a user using email from config.yaml."""
#     user_email = config["jira"]["test_user_email"]  # ✅ Fetch dynamically
#     user_results = search_user(user_email)
#
#     assert isinstance(user_results, list)  # ✅ Ensure the response is a list
#     assert len(user_results) > 0  # ✅ Ensure at least one result is found
#     assert user_results[0]["emailAddress"] == user_email  # ✅ Verify correct user
#
# def delete_project():
#     #delete a project by key if it is present
#
