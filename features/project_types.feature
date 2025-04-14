Feature: JIRA Project Types

  Scenario: Get all project types
    Given I have access to JIRA
    When I search for project types
    Then I get a list of all project types

  Scenario: Get licensed project types
    Given I have access to JIRA
    When I search for licensed project types
    Then I get a list of all licensed project types

  Scenario: Get Project Type by key
    Given I have access to JIRA
    When I search for project type by key
    Then I get a list of all project types by key

  Scenario: Get accessible project type by key
    Given I have access to JIRA
    When I search for accessible project type by key
    Then I get a list of all accessible project types

