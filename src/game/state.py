from random import randint
from functools import reduce
from typing import List
from .law import Law
from .city import City
from .pop_state import *


class State:
    INITIAL_MIGRATION_CHANCE = 2

    def __init__(self, laws: List[Law], last_election: int, cities: List[City]):
        self.laws = laws
        self.last_election = last_election
        self.cities = cities
        self.migration_chance = self.INITIAL_MIGRATION_CHANCE

    def get_pops_num_by_state(self, pop_state: PopState) -> int:
        all_pops = reduce(lambda x, y: x + y, [city.pops for city in self.cities])
        return len([pop for pop in all_pops if pop.state == pop_state])

    def get_healthy_pops_num(self) -> int:
        return self.get_pops_num_by_state(PopState.healthy)

    def get_dead_pops(self) -> int:
        return self.get_pops_num_by_state(PopState.dead)

    def get_ill_pops(self) -> int:
        return self.get_pops_num_by_state(PopState.ill)

    def get_vaccinated_pops(self) -> int:
        return self.get_pops_num_by_state(PopState.vaccinated)

    def get_recovered_pops(self) -> int:
        return self.get_pops_num_by_state(PopState.recovered)

    def introduce_law(self, law: Law):
        if law.exclusive_with:
            for current_law in self.laws:
                if law.exclusive_with == current_law.name:
                    self.revoke_law(current_law)
        if law.name == 'No migration':
            self.migration_chance = 0
        elif law.name == 'Limited migration':
            self.migration_chance = 1
        self.laws.append(law)
        for city in self.cities:
            for pop in city:
                for modifier in law.happiness_modifiers:
                    if 'all' in modifier:
                        pop.happiness = pop.happiness + modifier['all']
                    elif 'wearing_mask' in modifier and pop.mask_on:
                        pop.happiness = pop.happiness + modifier['wearing_mask']
                    elif 'not_wearing_mask' in modifier and not pop.mask_on:
                        pop.happiness = pop.happiness + modifier['not_wearing_mask']
                    elif 'young' in modifier and pop.age < 40:
                        pop.happiness = pop.happiness + modifier['young']
                    elif 'old' in modifier and pop.age > 50:
                        pop.happiness = pop.happiness + modifier['old']

    def revoke_law(self, law: Law):
        if law.name == 'No migration' or law.name == 'Limited migration':
            self.migration_chance = 2
        self.laws.remove(law)
        for city in self.cities:
            for pop in city:
                for modifier in law.happiness_modifiers:
                    if 'all' in modifier:
                        pop.happiness = pop.happiness - modifier['all']
                    elif 'wearing_mask' in modifier and pop.mask_on:
                        pop.happiness = pop.happiness - modifier['wearing_mask']
                    elif 'not_wearing_mask' in modifier and not pop.mask_on:
                        pop.happiness = pop.happiness - modifier['not_wearing_mask']
                    elif 'young' in modifier and pop.age < 40:
                        pop.happiness = pop.happiness - modifier['young']
                    elif 'old' in modifier and pop.age > 50:
                        pop.happiness = pop.happiness - modifier['old']

    def compute_migrations(self):
        for i in range(len(self.cities)):
            for pop in self.cities[i].pops:
                if randint(0, 99) < self.migration_chance:
                    self.cities[i].pops.remove(pop)
                    chosen_city = randint(1, len(self.cities) - 1)
                    self.cities[(i + chosen_city) % len(self.cities)].append(pop)
