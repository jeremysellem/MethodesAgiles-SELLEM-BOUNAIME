class InstaBo:

    def __init__(self):
        self._community = list()

    def add_robo(self, robo):
        self._community.append(robo.get_name())

    def get_community(self):
        return self._community

