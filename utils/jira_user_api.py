# from urllib.parse import quote
# import requests
# import yaml
# import logging
# from requests.auth import HTTPBasicAuth
#
# #load JIRA configuration
# with open("config.yaml","r") as file:
#     config=yaml.safe_load(file)
# JIRA_URL=config["jira"]["base_url"]
# AUTH=HTTPBasicAuth(config["jira"]["email"],config["jira"]["api_token"])
# GET_ALL_USER=config["jira"]["user_api"]["GET_Get_all_users"]
#
# #Configure Logging
# ##This will put all the log info in test_log.log
# logging.basicConfig(filename="logs/test_log.log",level=logging.INFO)
#
#
# def get_all_users():  # ✅ Default query parameter
#     """Fetches a list of all users in Jira with a default query."""
#     """url1 = f"{JIRA_URL}/rest/api/3/user/search?query={query}"  # ✅ Pass query param"""
#     url = f"{JIRA_URL}{GET_ALL_USER}"  # ✅ Pass query param
#     response = requests.get(url, auth=AUTH)
#
#     logging.info(f"Fetched users for function get_all_user: {response.status_code} - {response.text}")
#
#     return response.json()
#
# def search_user(query):
#     """Searches for a user by name or email."""
#     encoded_query=quote(query)
#     url=f"{JIRA_URL}/rest/api/3/user/search?query={encoded_query}"
#
#     response=requests.get(url,auth=AUTH)
#     logging.info(f"User search response: {response.status_code} - {response.text}")
#     return response.json()
#
# def get_lead_account_id(user_email):
#     """Gets the Lead Account ID of a specific user (needed for project creation)."""
#     users = search_user(user_email)
#     if users:
#         lead_account_id=users[0]["accountId"]
#         logging.info(f"Lead Account ID for {user_email}: {lead_account_id}")
#         return lead_account_id
#     return None