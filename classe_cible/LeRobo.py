from classe_cible import Engine, InstaBo
from dataclasses import dataclass
from classe_cible import TraderBnp
from design_patterns import ObservateurDP

@dataclass
class LeRobo(TraderBnp.TraderBnp):

    def __init__(self):
        super().__init__()
        self._name = "unknown"
        self._oil_level = 100
        self._is_alive = True
        self._ready_to_walk = False

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

    def get_engine(self, engine: Engine):
        self.engine = engine

    def ready_to_walk(self):
        return self.is_alive() and self.engine.get_state()

    def subscribe_to_instabo(self, insta:InstaBo):
        insta.add_robo(self)
        self.insta = insta

    def robo_talks(self, robo2):
        #Check if the Robo is in a social network
        if not (hasattr(self, 'insta') or hasattr(robo2, 'insta')):
            return False

        #Check if both robots are in InstaBo
        if(self.get_name() and robo2.get_name()) in self.insta.get_community():
            return True
        else :
            return False
