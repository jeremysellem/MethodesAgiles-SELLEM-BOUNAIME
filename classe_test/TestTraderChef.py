from classe_cible.TraderChef import TraderChef
from classe_cible.TraderBnp import TraderBnp

class TestTraderChef:

    # Attribut : un TraderChef
    trader_chef = TraderChef()

    def test_get_pnl(self):

        # Le PnL est initialisé à 0 au départ
        assert self.trader_chef.get_pnl() == 0

    def test_set_pnl(self):

        # On met le PnL à 5
        self.trader_chef.set_pnl(5)

        # On vérifie
        assert self.trader_chef.get_pnl() == 5

    def test_add_to_pnl(self):

        # On met le PnL à 5
        self.trader_chef.set_pnl(2)

        # On ajoute 5 au PnL
        self.trader_chef.add_to_pnl(5)

        # On vérifie (2 + 5 = 7)
        assert self.trader_chef.get_pnl() == 7

    def test_add_new_trader(self):

        # On garde en copie la taille de la liste des tarders
        current_length = len(self.trader_chef.traders)

        # On rattache un TraderBnp à notre chef
        new_trader = TraderBnp(self.trader_chef)

        # On vérifie que la taille de la liste s'est incrémentée
        assert len(self.trader_chef.traders) == current_length + 1

    def test_update_pnl(self):

        # On va créer deux traders sous la responsabilité de trader_chef
        trader_bnp1 = TraderBnp(self.trader_chef)
        trader_bnp2 = TraderBnp(self.trader_chef)

        # On leur attribue un daily_yield
        trader_bnp1.set_daily_yield(1)
        trader_bnp2.set_daily_yield(2)

        # On met à jour le PnL du chef
        self.trader_chef.update_pnl()

        # Somme des deux traders dans ma liste (1 + 2 = 3)
        assert self.trader_chef.get_pnl() == 3
    
