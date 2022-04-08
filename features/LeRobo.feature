Feature: Discussion in Instabo
  Two robots can discuss with each other when they are connected to the same
  social network.

  Scenario: Discussion in Instabo
    Given a robo robo1 and a robo robo2
    When we are connected to the same social network
    Then we can talk

  Scenario Outline:Outline
    Given a robo and another
    When they are connected to the same network <connected>
    Then they can <talk>
    Examples:
      | connected | talk  |
      | False     | False |
      | True      | True  |

