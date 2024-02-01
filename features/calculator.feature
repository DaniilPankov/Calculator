Feature: Calculator

  Scenario: Addition
    Given I have a calculator
    And I have entered 10 in first entry
    And I have entered 5 in second entry
    When I press sum button
    Then The result should be 15.0 on the screen

  Scenario: Subtraction
    Given I have a calculator
    And I have entered 14 in first entry
    And I have entered 7 in second entry
    When I press sub button
    Then The result should be 7.0 on the screen

  Scenario: Multiplication
    Given I have a calculator
    And I have entered 5 in first entry
    And I have entered 5 in second entry
    When I press mul button
    Then The result should be 25.0 on the screen

  Scenario: Division
    Given I have a calculator
    And I have entered 28 in first entry
    And I have entered 4 in second entry
    When I press div button
    Then The result should be 7.0 on the screen

  Scenario: Division by zero
    Given I have a calculator
    And I have entered 10 in first entry
    And I have entered 0 in second entry
    When I press div button
    Then An error ZeroDivision should be raised

  Scenario: Input Error
    Given I have a calculator
    And I have entered sometext in first entry
    And I have entered 10 in second entry
    When I press sum button
    Then An ValueError should be raised
