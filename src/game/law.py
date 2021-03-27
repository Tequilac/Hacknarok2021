from typing import List
from .law_scope import LawScope


class Law:
    def __init__(self, name: str, infection_chance_modifiers: List[dict], happiness_modifiers: List[dict],
                 scope: LawScope, exclusive_with: List[str]):
        self.name = name
        self.infection_chance_modifiers = infection_chance_modifiers
        self.happiness_modifiers = happiness_modifiers
        self.scope = scope
        self.exclusive_with = exclusive_with
