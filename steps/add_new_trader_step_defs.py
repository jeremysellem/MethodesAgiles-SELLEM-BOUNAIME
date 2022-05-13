from behave import *
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp
from dataclasses import dataclass

@dataclass()
class ManageAddTraderSteps:
    #_trader_chef: TraderChef

    @given(u'Un Trader')
    def un_trader_chef(self):
        self._trader = TraderBnp()

    @when(u'Je crée un trader chef et je le lie au trader')
    def ajouter_a_ma_liste(self):
        self._trader_chef = TraderChef(self._trader)

    @then(u'La liste est mise à jour')
    def liste_mise_a_jour(self):
        assert len(self._trader_chef.traders) == 1
