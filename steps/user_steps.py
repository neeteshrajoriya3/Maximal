# from pytest_bdd import scenario, given, when, then
# import logging
#
# @scenario("../feature/user.feature","Fetch all users")
# def test_fetch_all_users():
#     pass
#
# @given("I have access to Jira user management")
# def jira_user_access():
#     logging.info(f"Fetched users: {fetch_all_users}")
#
# @then("I should get a list of users")
# def verify_user_fetch():
#     assert isinstance(fetch_all_users, list)
#
# @scenario("../feature/user.feature","Search for a specific Jira user")
# def test_search_user():
#     pass
#
# @when("I search for a user by email or name")
# def search_user_step(search_specific_user):
#     logging.info(f"User search results: {search_specific_user}")
#
# @then("I should get user details")
# def verify_user_search(search_specific_user):
#     assert isinstance(search_specific_user,list) and len(search_specific_user)>0
#
