# Chaque Trader possède un daily yield et un chef, il va reporter son daily yield chaque jour à son chef
class TraderBnp:

    def __init__(self, trader):
        self.daily_yield = None
        self.set_daily_yield(0)
        self.trader_chef = trader
        self.trader_chef.add_new_trader(self)

    def get_daily_yield(self):
        return self.daily_yield

    def set_daily_yield(self, val):
        self.daily_yield = val

    def add_to_daily_yield(self, b):
        self.daily_yield += b
    
    def update_pnl_trader_chef(self):
        self.trader_chef.add_to_pnl(self.daily_yield)
    
    