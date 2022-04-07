Feature: Mettre à jour le Daily Yield d'un trader
  As a TraderBnp
  Je veux mettre à jour mon Daily Yield

  Scenario: Update Daily Yield
   Given Un TraderBnp et son Daily Yield
    When J'ajoute une somme à son Daily Yield
    Then La valeur du Daily Yield est mise à jour
