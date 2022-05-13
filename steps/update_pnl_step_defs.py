from behave import *
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp
from dataclasses import dataclass

@dataclass()
class ManageUpdatePnLSteps:
    _trader_chef: TraderChef

    @given(u'Un TraderChef et sa liste de traders')
    def un_trader_chef(self):
        trader_bnp1 = TraderBnp()
        trader_bnp2 = TraderBnp()
        self._trader_chef = TraderChef(trader_bnp1)
        self._trader_chef.add_new_trader(trader_bnp2)
        trader_bnp1.set_daily_yield(3)
        trader_bnp2.set_daily_yield(7)

    @when(u'Je récupère les daily yields de ses traders')
    def recuperer_daily_yields(self):
        self._trader_chef.update_pnl()

    @then(u'La valeur du PnL est mise à jour')
    def pnl_mis_a_jour(self):
        assert self._trader_chef.get_pnl() == 10
