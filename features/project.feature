Feature: Jira Project Management

  Scenario: Fetch all projects
    Given I have access to Jira project management
    When I fetch all projects
    Then I should get a list of projects

  Scenario: Fetch Project
    Given I have access to Jira project management
    When I search for a project
    Then I should get the details of project

  Scenario: Delete project with Key
    Given I have Project Key
    When I delete the Project
    Then The Project should get deleted

  Scenario: Delete project with ProjectID
    Given I have ProjectID
    When I delete the Project
    Then The Project should get deleted
