Feature: Créer un TraderBnp et le rattacher à un TraderChef

  Scenario: add_new_trader
   Given Un Trader
    When Je crée un trader chef et je le lie au trader
    Then La liste est mise à jour
