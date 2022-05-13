from behave import *
from dataclasses import dataclass
from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp


@dataclass()
class ManageUpdateDailyYieldSteps:
    _trader: TraderBnp
    _chef: TraderChef(_trader)
    @given(u'Un TraderChef et son daily <current_daily>')
    def un_trader_bnp(self,current_daily):
        self._chef.set_pnl(current_daily)

    @when(u'Un trader performe son <new_daily> et le transmet à son trader chef')
    def ajouter_au_daily_yield(self, new_daily):
        self._trader.add_to_daily_yield(new_daily)
        self._trader.notify_observers()

    @then(u'Le trader chef peut observer le <updated_daily> de son trader')
    def daily_yield_mis_a_jour(self, updated_daily):
        assert self._chef.get_daily_yield() == float(updated_daily)
