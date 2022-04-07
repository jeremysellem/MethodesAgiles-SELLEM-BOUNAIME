from behave import *
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp
from dataclasses import dataclass

@dataclass()
class ManageUpdateDailyYieldSteps:
    _trader_bnp: TraderBnp

    @given(u'Un TraderBnp et son Daily Yield')
    def un_trader_bnp(self):
        self._trader_bnp = TraderBnp(TraderChef())

    @when(u'J\'ajoute une somme à son Daily Yield')
    def ajouter_au_daily_yield(self):
        self._trader_bnp.add_to_daily_yield(8)

    @then(u'La valeur du Daily Yield est mise à jour')
    def daily_yield_mis_a_jour(self):
        assert self._trader_bnp.get_daily_yield() == 8