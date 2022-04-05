

class TraderBnp:
    def __init__(self,trader):
        self.daily_yield = 0
        self.trader_chef = trader

    def get_daily_yield(self):
        return self.daily_yield

    def set_daily_yield(self,val):
        self.daily_yield = val

    def update_daily_yield(self,b):
        self.daily_yield += b
    
    def update_pnl_trader_chef(self):
        self.trader_chef.add_to_pnl(self.daily_yield)
    
    