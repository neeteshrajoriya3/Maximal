Feature: Jira Project Management

  Scenario: Fetch all users
    Given I have access to Jira project management
    When I fetch all projects
    Then I should get a list of projects