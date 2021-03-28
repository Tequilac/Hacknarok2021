import json
from pathlib import Path

from game.law import *
from game.law_scope import *


class LawsParser:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def load_law(self) -> Law:
        with open(self.filepath, 'r') as f:
            data = json.load(f)

        name = data['name']
        scope = LawScope[data['scope']]
        infection_chance_modifiers = data['infection_chance_modifiers']
        happiness_modifiers = data['infection_chance_modifiers']
        exclusive_with = data['exclusive_with'] if 'exclusive_with' in data else None
        wearing_mask = data['wearing_mask'] if 'wearing_mask' in data else None
        return Law(name, infection_chance_modifiers, happiness_modifiers, scope, exclusive_with, wearing_mask)
