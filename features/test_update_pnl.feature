Feature: Tester la mise à jour du pnl

En tant que chef des traders (BnpTrader), la variable pnl de la classe mere Trader doit contenir tous les rendements gagnés par les traders.

Scenario Outline: L'ajout de les rendements quotidients des traders dans la variable pnl
Given: un objet Trader (par exemple BnpTrader)
When: L'appel à la fonction update pnl
Then: 