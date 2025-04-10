Feature: Jira Project Management

  Scenario: Fetch all Jira projects
    Given I have access to Jira project management
    When I request all projects
    Then I should get a list of projects

  Scenario: Create a new Jira project
    Given I have a valid Jira API instance
    When I send a request to create a project
    Then The project should be successfully created