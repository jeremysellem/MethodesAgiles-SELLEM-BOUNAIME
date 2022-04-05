from TP2 import TraderBnp 
# c'est le chef
class Trader:
    def __init__(self):
        self.pnl = 0
        self.daily_yield = 0

    def get_pnl(self):
        return self.pnl

    def get_daily_yield(self):
        return self.daily_yield

    def set_pnl(self,val):
        self.pnl = val
    
    def set_daily_yield(self,val):
        self.daily_yield = val

    def add_to_pnl(self,val):
        self.pnl += val

    
    
    