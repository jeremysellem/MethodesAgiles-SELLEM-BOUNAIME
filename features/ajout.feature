Feature: Ajouter un Trader
  As a BnpTrader
  Je veux ajouter un nouveau Trader à la liste des traders existants

  Scenario: Ajout
   Given Un trader <t1>,
    When J'ajoute le trader à ma liste
    Then il est ajouter à la liste actuelle <liste>
