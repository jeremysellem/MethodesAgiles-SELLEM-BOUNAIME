# C'est le chef de tous les traders, il agrège les Pnl des traders sous sa responsabilite (sa liste)
class TraderChef:

    def __init__(self):
        self.pnl = None
        self.set_pnl(0)
        self.traders = []

    def get_pnl(self):
        return self.pnl

    def set_pnl(self, val):
        self.pnl = val

    def add_to_pnl(self, val):
        self.pnl += val

    def add_new_trader(self, new_trader):
        self.traders.append(new_trader)

    def update_pnl(self):
        new_pnl = 0
        for t in self.traders:
            new_pnl += t.get_daily_yield()
        self.set_pnl(new_pnl)
