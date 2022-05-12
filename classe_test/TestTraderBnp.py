from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp

class TestTraderBnp:

    # Attribut : un TraderBnp
    trader_bnp = TraderBnp()
    

    def test_get_daily_yield(self):

        # Le daily_yield est initialisé à 0 au départ
        assert self.trader_bnp.get_daily_yield() == 0

    def test_set_daily_yield(self):

        # On met le daily_yield à 5
        self.trader_bnp.set_daily_yield(5)

        # On vérifie
        assert self.trader_bnp.get_daily_yield() == 5

    def test_update_daily_yield(self):

        # On met le daily_yield à 0 pour que le test soit indépendant
        self.trader_bnp.set_daily_yield(0)

        # On ajoute 8 au daily_yield
        self.trader_bnp.add_to_daily_yield(8)

        # On vérifie (0 + 8 = 8)
        assert self.trader_bnp.get_daily_yield() == 8

    def test_notify_observers(self):

        # On met le daily_yield à 13 pour que le test soit indépendant
        self.trader_bnp.set_daily_yield(13)

        self.trader_bnp.notify_observers()
        # On vérifie que le PnL du trader est bien passé de 13 à 0
        assert self.trader_bnp.get_daily_yield() == 0


