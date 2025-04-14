Feature: Jira Project Management

  Scenario: Get all Projects
    Given i have access to JIRA
    When user search for projects
    Then user gets a list of all projects

  Scenario: Fetch a Project
    Given i have access to JIRA
    When user search for a project
    Then projects details should be displayed

  Scenario: Create a Project
    Given i have access to JIRA
    When user creates a project
    Then a new project should get created

  Scenario: Delete a Project
    Given i have access to JIRA
    When user deletes a project
    Then project should get deleted

  Scenario: Get recent project
    Given i have access to JIRA
    When user search for recent projects
    Then a list of recent projects is displayed

  Scenario: Get projects paginated
    Given i have access to JIRA
    When user search for projects
    Then a paginated list of projects is displayed