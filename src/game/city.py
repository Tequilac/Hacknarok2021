from random import randint
from .pop_state import *


class City:
    def __init__(self, name, pops, laws, location):
        self.name = name
        self.pops = pops
        self.location = location
        self.laws = laws
        self.previous_turn_data = {}

    def get_healthy_pops(self):
        return len(list(filter(lambda pop: pop.state == PopState.healthy, self.pops)))

    def get_dead_pops(self):
        return len(list(filter(lambda pop: pop.state == PopState.dead, self.pops)))

    def get_ill_pops(self):
        return len(list(filter(lambda pop: pop.state == PopState.ill, self.pops)))

    def get_vaccinated_pops(self):
        return len(list(filter(lambda pop: pop.state == PopState.vaccinated, self.pops)))

    def get_recovered_pops(self):
        return len(list(filter(lambda pop: pop.state == PopState.recovered, self.pops)))

    def save_turn_data(self):
        self.previous_turn_data['healthy'] = self.get_healthy_pops()
        self.previous_turn_data['dead'] = self.get_dead_pops()
        self.previous_turn_data['ill'] = self.get_ill_pops()
        self.previous_turn_data['vaccinated'] = self.get_vaccinated_pops()
        self.previous_turn_data['recovered'] = self.get_recovered_pops()

    def introduce_law(self, law):
        self.laws.append(law)
        for pop in self.pops:
            for modifier in law.happiness_modifiers:
                pop.apply_modifier(modifier)

    def revoke_law(self, law):
        self.laws.remove(law)
        for pop in self.pops:
            for modifier in law.happiness_modifiers:
                pop.remove_modifier(modifier)

    def compute_pops_changes(self, state_laws, turn):
        ill_number = 0
        for pop in self.pops:
            if pop.state == PopState.ill:
                num = 1
                if pop.quarantined:
                    num = num / 2
                if pop.mask_on:
                    num = num / 2
                ill_number = ill_number + num

        death_chance = 10
        quarantine_chance = 20
        recovered_chance = 30

        for pop in self.pops:
            if pop.state == PopState.dead:
                self.pops.remove(pop)
            elif pop.state == PopState.ill:
                if randint(0, 99) < death_chance:
                    pop.state = PopState.dead
                elif randint(0, 99) < quarantine_chance:
                    pop.quarantined = True
                elif turn - pop.illness_date > 2:
                    pop.state = PopState.recovered
                    pop.quarantined = False
            elif pop.state == PopState.healthy:
                infection_chance = int(100 * ill_number / len(self.pops))
                self.compute_infection_chance(self.laws, pop, infection_chance)
                self.compute_infection_chance(state_laws, pop, infection_chance)
                if randint(0, 99) < infection_chance:
                    pop.state = PopState.ill
            elif pop.state == PopState.recovered:
                if randint(0, 99) < recovered_chance:
                    pop.state = PopState.healthy

        wearing_mask = 0
        for law in state_laws:
            if law.wearing_mask:
                wearing_mask = law.wearing_mask
        for pop in self.pops:
            if pop.mask_on:
                if randint(0, 99) < wearing_mask - (100 - pop.happiness):
                    pop.mask_on = False
            else:
                if randint(0, 99) > wearing_mask - (100 - pop.happiness):
                    pop.mask_on = True

    def compute_infection_chance(self, laws, pop, infection_chance):
        for law in laws:
            for modifier in law.infection_chance_modifiers:
                if 'all' in modifier:
                    infection_chance = infection_chance + modifier['all']
                elif 'wearing_mask' in modifier and pop.mask_on:
                    infection_chance = infection_chance + modifier['wearing_mask']
                elif 'not_wearing_mask' in modifier and not pop.mask_on:
                    infection_chance = infection_chance + modifier['not_wearing_mask']
                elif 'young' in modifier and pop.age < 40:
                    infection_chance = infection_chance + modifier['young']
                elif 'old' in modifier and pop.age > 50:
                    infection_chance = infection_chance + modifier['old']
