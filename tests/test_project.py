import pytest
import yaml
from utils.jira_project_api import get_all_projects

# ✅ Load configuration from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


@pytest.mark.api  # ✅ API-related test
@pytest.mark.user  # ✅ User-related test
def test_get_all_projects():
    """Test to fetch all users from Jira."""
    projects = get_all_projects()

    assert isinstance(projects, list)  # ✅ Ensure the result is a list
    assert len(projects) > 0  # ✅ Ensure there is at least one user

def delete_project_by_key(project_key)
