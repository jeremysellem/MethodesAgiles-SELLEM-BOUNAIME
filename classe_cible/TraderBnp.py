from design_patterns import ObservateurDP


# Chaque Trader possède un daily yield et un chef, il va reporter son daily yield chaque jour à son chef
class TraderBnp(ObservateurDP.Observable):

    def __init__(self):
        super().__init__()
        self.daily_yield = None
        self.set_daily_yield(0)

    def get_daily_yield(self):
        return self.daily_yield

    def set_daily_yield(self, val: float):
        self.daily_yield = float(val)

    def add_to_daily_yield(self, b: float):
        self.daily_yield += float(b)

    def notify_observers(self):
        for observer in self._observers :
            observer.notify(self.daily_yield)
        self.daily_yield = 0
    
    