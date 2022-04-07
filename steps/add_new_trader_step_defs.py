from behave import *
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp
from dataclasses import dataclass

@dataclass()
class ManageAddTraderSteps:
    _trader_chef: TraderChef

    @given(u'Un TraderChef')
    def un_trader_chef(self):
        self._trader_chef = TraderChef()

    @when(u'Je crée et j\'ajoute un TraderBnp')
    def ajouter_a_ma_liste(self):
        TraderBnp(self._trader_chef)

    @then(u'La liste est mise à jour avec ce nouveau trader')
    def liste_mise_a_jour(self):
        assert len(self._trader_chef.traders) == 1