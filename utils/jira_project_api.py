import logging
import requests
import yaml
from requests.auth import HTTPBasicAuth
from utils.jira_user_api import get_lead_account_id  # ✅ Import Lead Account ID function

# ✅ Load configuration from config.yaml
with open("config.yaml","r") as file:
    config=yaml.safe_load(file)

JIRA_URL=config["jira"]["base_url"]
AUTH=HTTPBasicAuth(config["jira"]["email"],config["jira"]["api_token"])
GET_ALL_PROJECT=config["jira"]["project_api"]["GET_Get_all_projects"]
# Configure logging
logging.basicConfig(filename="logs/test_log.log", level=logging.INFO)


