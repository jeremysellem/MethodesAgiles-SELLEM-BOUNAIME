from TP2 import Trader, TraderBnp

class Test_trader():
    trader_chef = Trader.Trader() 
    trader = TraderBnp.TraderBnp(trader_chef)

    def test_get_daily_yield(self):
        assert self.trader.get_daily_yield() == 0

    def test_set_daily_yield(self):
        self.trader.set_daily_yield(5)
        assert self.trader.get_daily_yield() == 5

    def test_get_pnl(self):
        assert self.trader_chef.get_pnl() == 0

    def test_set_pnl(self):
        self.trader_chef.set_pnl(5)
        assert self.trader_chef.get_pnl() == 5
    
    def test_update_pnl(self):
        self.trader.set_daily_yield(5)
        self.trader_chef.set_pnl(2)
        self.trader.update_pnl_trader_chef()       
        assert self.trader_chef.get_pnl() == 7
    

