from design_patterns import ObservateurDP

# C'est le chef de tous les traders, il agrège les Pnl des traders sous sa responsabilite (sa liste)
class TraderChef(ObservateurDP.Observer):

    def __init__(self, trader):
        super().__init__(trader)
        self.pnl = None
        self.set_pnl(0)
        self.traders = []
        self.traders.append(trader)

    def get_pnl(self):
        return self.pnl

    def set_pnl(self, val):
        self.pnl = val

    def add_to_pnl(self, val):
        self.pnl += val

    def add_new_trader(self, new_trader):
        self.traders.append(new_trader)

    def notify(self, observed):
        new_pnl = self.get_pnl() + observed
        self.set_pnl(new_pnl)
        print("J'ai reçu un PnL de {}% de la part d'un trader, le PnL total est maintenant de {}%".format(observed*100, new_pnl*100))

    def update_pnl(self):
        pnl = 0
        for trader in self.traders:
            pnl += trader.get_daily_yield()
            self.set_pnl(pnl)