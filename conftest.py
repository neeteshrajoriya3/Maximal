import pytest
from utils.jira_project_api import JiraProjectAPI
from types import SimpleNamespace
from faker import Faker
import random
import string

@pytest.fixture
def jira_api() -> JiraProjectAPI:
    return JiraProjectAPI()

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
    else:
        return "Invalid type"