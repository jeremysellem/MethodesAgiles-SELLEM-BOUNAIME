Feature: Mettre à jour le PnL du chef
  As a TraderChef
  Je veux mettre à jour mon PnL à partir de tous les daily yield de mes traders

  Scenario: Update PnL
   Given Un TraderChef et sa liste de traders
    When Je récupère les daily yields de ses traders
    Then La valeur du PnL est mise à jour
