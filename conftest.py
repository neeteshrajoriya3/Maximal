import pytest
from utils.jira_project_api import JiraProjectAPI
from types import SimpleNamespace
from faker import Faker
import random
import string
import yaml
from utils.jira_project_types_api import JIRAProjectTypeAPI
@pytest.fixture
def jira_api() -> JiraProjectAPI:
    return JiraProjectAPI()

@pytest.fixture
def jiraAPI_ProjectType() -> JIRAProjectTypeAPI:
    return JIRAProjectTypeAPI()
@pytest.fixture
def context() -> SimpleNamespace:
    return SimpleNamespace()

fake = Faker()
def generate_fake_text(type="sentence"):
    if type == "word":
        return ''.join(random.choices(string.ascii_lowercase, k=4))
    elif type == "sentence":
        return fake.sentence()
    elif type == "paragraph":
        return fake.paragraph()
    elif type == "name":
        return fake.name()

    else:
        return "Invalid type"

def get_url(endpoint, key=None):
    with open("config.yaml","r") as file:
        config=yaml.safe_load(file)
    endpoint=config["jira"]["Project_type"][endpoint]
    if key:
        endpoint=endpoint.replace("{projectTypeKey}",str(key))
    jira_url = config["jira"]["base_url"]
    return f"{jira_url}{endpoint}"
