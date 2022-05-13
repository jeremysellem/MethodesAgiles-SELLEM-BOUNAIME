class Observer:

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, observed):
        print ('Got {} from {}'.format(observed, observable))


class Observable:

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, to_notify):
        for obs in self._observers:
            obs.notify(self, to_notify)

    def unsubscribe(self, observer):
        self._observers.remove(observer)
    
    def get_observers(self):
        return self._observers

