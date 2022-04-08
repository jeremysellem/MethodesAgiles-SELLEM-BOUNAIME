class Engine:

    def __init__(self):
        self._state = False

    def set_state(self, state:bool):
        self._state = state

    def get_state(self):
        return self._state