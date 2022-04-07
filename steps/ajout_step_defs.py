from behave import *
from classe_cible import TraderChef
from dataclasses import dataclass

@dataclass
class ManageTraderSteps:
    _trader: Trader

    @given(u'Un trader t1,')
    def un_trader_t1(t1):
        self._trader = Trader()

    @when(u'J\'ajoute le trader à ma liste')
    def ajouter_a_ma_liste(context):
        raise NotImplementedError(u'STEP: When J\'ajoute le trader à ma liste')


    @then(u'il est ajouter à la liste actuelle <liste>')
    def step_impl(context):
        raise NotImplementedError(u'STEP: Then il est ajouter à la liste actuelle <liste>')