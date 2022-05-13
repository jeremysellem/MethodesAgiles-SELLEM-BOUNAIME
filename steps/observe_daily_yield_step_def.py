from behave import *
from dataclasses import dataclass
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp


@dataclass()
class ManageUpdateDailyYieldSteps:
    #_trader: TraderBnp
    #_chef: TraderChef(_trader)
    @given(u'Un Trader et son daily {current_daily}')
    def un_trader_bnp(self,current_daily):
        self._trader = TraderBnp()
        self._trader.set_daily_yield(current_daily)
        self._trader_chef = TraderChef(self._trader)

    @when(u'Un trader performe son {new_daily} et le transmet à son trader chef')
    def ajouter_au_daily_yield(self, new_daily):
        self._trader.add_to_daily_yield(new_daily)
        self._trader.notify_observers()

    @then(u'Le trader chef peut observer le daily updated {updated_daily} de son trader')
    def daily_yield_mis_a_jour(self, updated_daily):
        assert self._trader_chef.get_pnl() == float(updated_daily)
