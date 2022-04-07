Feature: Mettre à jour le Daily Yield d'un trader
  As a TraderBnp
  Je veux mettre à jour mon Daily Yield

  Scenario Outline: Update Daily Yield
   Given Un TraderBnp et son Daily Yield initialement à <current_daily>
    When J'ajoute une somme <new_daily> à son Daily Yield
    Then Je récupère la valeur du Daily Yield mis à jour <updated_daily>
    Examples:
    |current_daily | new_daily | updated_daily |
    | 4            | 3         | 7             |
    | 7.1          | 5.2       | 12.3          |
    | -1           | 4         | 3             |


