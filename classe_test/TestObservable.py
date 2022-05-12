from design_patterns import ObservateurDP

class TestObservable:

    
    observer = ObservateurDP.Observable()

    def test_subscribe(self):

        self.observer.subscribe('trader')
        assert len(self.observer.get_observers()) != 0
