import os
from .laws_parser import *
from .law_scope import *


class Game:
    def __init__(self, turn, state):
        self.turn = turn
        self.state = state
        laws = self.create_laws()
        self.state_laws = laws[0]
        self.city_laws = laws[0]

    def create_laws(self):
        state_laws = []
        city_laws = []
        for file in os.listdir('..\\resources\\laws'):
            law = load_law('..\\resources\\laws\\' + file)
            if law.scope == LawScope.state:
                state_laws.append(law)
            else:
                city_laws.append(law)
        return [state_laws, city_laws]
