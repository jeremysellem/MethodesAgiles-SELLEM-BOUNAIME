Feature: Créer un TraderBnp et le rattacher à un TraderChef
  As a TraderChef
  Je veux ajouter un nouveau TraderBnp à ma liste de traders

  Scenario: add_new_trader
   Given Un TraderChef
    When Je crée et j'ajoute un TraderBnp
    Then La liste est mise à jour avec ce nouveau trader
