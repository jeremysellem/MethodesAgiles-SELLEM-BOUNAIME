from classe_cible.LeRobo import LeRobo
from classe_cible.InstaBo import InstaBo
from behave import *
from dataclasses import dataclass

@dataclass
class ManageLeRoboSteps:
    _robo1 = LeRobo()
    _robo2 = LeRobo()
    _result = False

    @given("a robo robo1 and a robo robo2")
    def two_robots_robo1_robo2(self):
        self.robo1 = LeRobo()
        self.robo1.set_name("robo1")
        self.robo2 = LeRobo()
        self.robo2.set_name("robo2")
        names = self.robo1 != "unknown" and self.robo2 != "unknown"
        assert names

    @when("we are connected to the same social network")
    def robo1_and_robo2_connect_to_instabo(self):
        self.insta = InstaBo()
        self.robo1.subscribe_to_instabo(self.insta)
        self.robo2.subscribe_to_instabo(self.insta)
        assert hasattr(self.robo1, 'insta') and hasattr(self.robo2, 'insta')

    @then("we can talk")
    def robo1_and_robo2_talk(self):
        self._result = self.robo1.robo_talks(self.robo2)
        assert self._result

    @given("a robo and another")
    def two_robots(self):
        self.robo1 = LeRobo()
        self.robo1.set_name("robo1")
        self.robo2 = LeRobo()
        self.robo2.set_name("robo2")
        names = self.robo1 != "unknown" and self.robo2 != "unknown"
        assert names

    @when("they are connected to the same network {connected}")
    def two_robots_connexion(self, connected):
        if connected == "True":
            self.insta = InstaBo()
            self.robo1.subscribe_to_instabo(self.insta)
            self.robo2.subscribe_to_instabo(self.insta)
            assert hasattr(self.robo1, 'insta') == True and hasattr(self.robo2, 'insta') == True
        else:
            assert hasattr(self.robo1, 'insta') == False and hasattr(self.robo2, 'insta') == False

    @then("they can {talk}")
    def two_robots_talk(self, talk):
        self._result = self.robo1.robo_talks(self.robo2)
        print("For this test, the wanted result is {} and the output is {}".format(talk, self._result))
        assert str(self._result) == str(talk)
