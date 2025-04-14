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

  Scenario: Update Project
    Given i have access to JIRA
    When I update a project
    Then project should get updated

  Scenario: Archive Project
    Given i have access to JIRA
    When I archive a project
    Then project should get archived

  Scenario: Delete Project asynchronously
    Given i have access to JIRA
    When I delete project synchronously
    Then project gets deleted synchronously

  Scenario: Restore Project
    Given i have access to JIRA
    When I restore the project
    Then project should get restored

  Scenario: Get Statuses of Project
    Given i have access to JIRA
    When I search for statuses of project
    Then I get a list of all project statuses

  Scenario: Get project issue type
    Given i have access to JIRA
    When I search for issue types for project
    Then I get a list of all issue types

  Scenario: Get project notification scheme
    Given i have access to JIRA
    When I search for notification scheme for project
    Then I get a list of all notification scheme