Feature: Jira User Management

  Scenario: Fetch all users
    Given I have access to Jira user management
    When I fetch all users
    Then I should get a list of users

  Scenario: Fetch user details
    Given I have access to Jira user management
    When I fetch details of a specific user
    Then I should get user details

  Scenario: Fetch user groups
    Given I have access to Jira user management
    When I fetch the groups of a user
    Then I should get a list of groups

  Scenario: Fetch users in a group
    Given I have access to Jira user management
    When I fetch users in a specific group
    Then I should get a list of users in that group