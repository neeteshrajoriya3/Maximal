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

  Scenario: Restore deleted or archived project
    Given I have Project key
    When I restore the Project
    Then The Project should be visible in the list

  Scenario: Create a project
    Given I have access to Jira project management
    When I create a project
    Then The project should get created

  Scenario: Update a Project
    Given I have access to Jira project management
    When I update a project
    Then The project should get updated

  Scenario: Get Recent Project
    Given I have access to Jira project management
    When I search for recent projects
    Then I get a list of recent projects viewed by user

 Scenario: Archive project with Key
    Given I have Project Key
    When I archive the Project
    Then The Project should get archived