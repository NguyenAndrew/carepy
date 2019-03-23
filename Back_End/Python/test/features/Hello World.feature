Feature: Hello World!

  Scenario: Calling the Flask route
    Given an Flask application called app
    When I call the health route on app
    Then I should see Hello World!
    And I should see a 200 status