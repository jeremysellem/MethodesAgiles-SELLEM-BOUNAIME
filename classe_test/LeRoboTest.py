import unittest
from LeRobo import LeRobo
from Engine import Engine
from InstaBo import InstaBo
import sys
import subprocess


class LeRoboTest(unittest.TestCase):

    '''
    def setUp(self):
        self.robo = LeRobo()
        self.engine = Engine()
        self.engine.set_state(True)
        self.robo.get_engine(self.engine)

    def test_walk(self):
        self.assertEqual(True, self.robo.ready_to_walk())
    '''

    def setUp(self):
        self.insta = InstaBo()
        self.robo1 = LeRobo()
        self.robo1.set_name('Bobo')
        self.robo2 = LeRobo()
        self.robo2.set_name('Coco')
        self.robo1.subscribe_to_instabo(self.insta)
        self.robo2.subscribe_to_instabo(self.insta)

    def test_talk(self):
        talk = self.robo1.robo_talks(self.robo2)
        talk2 = self.robo2.robo_talks(self.robo1)
        talk_union = talk and talk2
        self.assertEqual(True, talk_union)
