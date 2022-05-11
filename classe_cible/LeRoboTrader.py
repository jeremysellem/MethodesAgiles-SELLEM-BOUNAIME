from classe_cible import TraderBnp, TraderChef

class LeRoboTrader(TraderBnp.TraderBnp):

    def __init__(self, trader):
        super().__init__(trader)
        self._name = "unknown"
        self._oil_level = 100
        self._is_alive = True

    def add_oil(self, oil):
        new_level = self._oil_level + oil
        #if positive --> Add
        if oil > 0 :
            #Level cannot exceed 100
            self.oil_level = min(100, new_level)
        #Else --> Remove
        else :
            #Level cannot be below 0
            self.oil_level = max(0, new_level)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_oil_level(self, level):
        if level > 0 :
            self._oil_level = level
            self._is_alive = True
        else :
            self._oil_level = 0
            self._is_alive = False

    def is_alive(self):
        return self._is_alive

    def get_oil_level(self):
        return self._oil_level