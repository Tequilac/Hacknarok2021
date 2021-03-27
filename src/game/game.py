import os
import settings
from parsers.laws_parser import *
from .law_scope import *
from .state import State


class Game:
    def __init__(self, turn: int, state: State):
        self.turn = turn
        self.state = state
        laws = self.create_laws()
        self.state_laws = laws[0]
        self.city_laws = laws[1]

    def next_turn(self) -> None:
        for city in self.state.cities:
            city.compute_pops_changes(self.state.laws, self.turn)
        self.state.compute_migrations()
        self.turn = self.turn + 1

    def create_laws(self) -> List[List[Law]]:
        state_laws = []
        city_laws = []
        laws_path = settings.Paths.RESOURCES / 'laws'

        for file in os.listdir(laws_path):
            law = LawsParser(laws_path / file).load_law()
            if law.scope == LawScope.state:
                state_laws.append(law)
            else:
                city_laws.append(law)

        return [state_laws, city_laws]
