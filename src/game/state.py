from random import randint

from .pop_state import *

class State:
    def __init__(self, laws, last_election, cities):
        self.laws = laws
        self.last_election = last_election
        self.cities = cities
        self.migration_chance = 2

    def get_healthy_pops(self):
        pops = []
        for city in self.cities:
            pops.extend(city.pops)
        return len(list(filter(lambda pop: pop.state == PopState.healthy, pops)))

    def get_dead_pops(self):
        pops = []
        for city in self.cities:
            pops.extend(city.pops)
        return len(list(filter(lambda pop: pop.state == PopState.dead, pops)))

    def get_ill_pops(self):
        pops = []
        for city in self.cities:
            pops.extend(city.pops)
        return len(list(filter(lambda pop: pop.state == PopState.ill, pops)))

    def get_vaccinated_pops(self):
        pops = []
        for city in self.cities:
            pops.extend(city.pops)
        return len(list(filter(lambda pop: pop.state == PopState.vaccinated, pops)))

    def get_recovered_pops(self):
        pops = []
        for city in self.cities:
            pops.extend(city.pops)
        return len(list(filter(lambda pop: pop.state == PopState.recovered, pops)))

    def introduce_law(self, law):
        if law.exlusive_with:
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
                    elif 'young' in modifier and pop.age < 40:
                        pop.happiness = pop.happiness + modifier['young']
                    elif 'old' in modifier and pop.age > 50:
                        pop.happiness = pop.happiness + modifier['old']

    def revoke_law(self, law):
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
