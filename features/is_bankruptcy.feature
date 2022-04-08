Feature: Le chef trader checke le PnL de ses traders. Si PnL égale -1 (-100%) alors faillite.
  As a TraderBnp
  Je veux savoir si je suis en faillite

  Scenario Outline: Check PnL amount
   Given Le chef trader reçoit les PnL <current_pnl>
    When Je verifie le montant du PnL <current_pnl>
    Then Si PnL égale -100% alors bankrupcy.
    Examples:
    |current_pnl | current_pnl |
    | -1         | True        |
