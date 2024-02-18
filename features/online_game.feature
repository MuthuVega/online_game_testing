Feature: Play Finding the truth game
  As a new user
  I would like to play the online game Finding the truth
  To explore different aspects of the criminal justice system

  Background:
    Given the user has access to the Finding the truth game link
    And navigates to the game link for the first time
    And the landing page is displayed

  Scenario: Correct game score displayed at start of game
    When the user  clicks on the START button to start playing
    Then the cases are presented to the user
    And a game score of 0/2 is dispalyed

  Scenario: Correct case details displayed on case selection
    When the user  clicks on the START button to start playing
    And the cases are presented to the user
    And the user chooses a case
    Then the case details for the chosen case are displayed to the user

  Scenario: Select a verdict for Making a case against Kevin case
    Given the user has chosen the case "Making a case against Kevin"
    And watched the video
    And clicked the button `JUDGE THIS`
    When the page to select the verdict is displayed
    And the user chooses the `Guilty` option
    And clicks the `VOTE` button
    Then a confirmation window with the text 'GUILTY' is diplayed

