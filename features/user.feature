Feature: Jira User Management

  Scenario: Fetch a user
    Given I have access to Jira project management
    When I search for a user
    Then I should get details of the user

  Scenario: Create a user
    Given I have access to Jira project management
    When I have a user for user creation
    Then user should get created

  Scenario: Delete a user
    Given I have access to Jira project management
    When I delete a user
    Then user should get deleted

  Scenario: Bulk get user
    Given I have access to Jira project management
    When I search for users in bulk
    Then I get a list of users

  Scenario: Get account ids for users
    Given I have access to Jira project management
    When I search for account ids for users
    Then I get list of users with account ids

  Scenario: Get user default columns
    Given I have access to Jira project management
    When I search for default table columns for a user
    Then I get a list of default columns for the user

  Scenario: Set