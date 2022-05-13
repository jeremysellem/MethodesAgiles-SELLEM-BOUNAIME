from behave import *
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp
from dataclasses import dataclass

@dataclass()
class ManageUpdateDailyYieldSteps:
    _trader_bnp: TraderBnp

    @given(u'Un TraderBnp et son Daily Yield initialement à {current_daily}')
    def un_trader_bnp(self, current_daily):
        self._trader_bnp = TraderBnp(TraderChef())
        self._trader_bnp.set_daily_yield(current_daily)

    @when(u'J\'ajoute une somme {new_daily} à son Daily Yield')
    def ajouter_au_daily_yield(self, new_daily):
        self._trader_bnp.add_to_daily_yield(new_daily)

    @then(u'Je récupère la valeur du Daily Yield mis à jour {updated_daily}')
    def daily_yield_mis_a_jour(self, updated_daily):
        assert self._trader_bnp.get_daily_yield() == float(updated_daily)
