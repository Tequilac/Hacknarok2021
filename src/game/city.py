from random import randint
from typing import List, Tuple
from .pop import Pop
from .pop_state import *
from .law import Law


class City:
    DEATH_CHANCE = 10
    QUARANTINE_CHANCE = 20
    RECOVERED_CHANCE = 30
    
    def __init__(self, name: str, pops: List[Pop], location: Tuple[int], laws=None):
        self.name = name
        self.pops = pops
        self.location = location
        self.laws = laws if laws else []

    def get_pops_num_by_state(self, pop_state: PopState):
        return len([pop for pop in self.pops if pop.state == pop_state])

    def get_healthy_pops_num(self) -> int:
        return self.get_pops_num_by_state(PopState.healthy)

    def get_dead_pops_num(self) -> int:
        return self.get_pops_num_by_state(PopState.dead)

    def get_ill_pops_num(self) -> int:
        return self.get_pops_num_by_state(PopState.ill)

    def get_vaccinated_pops_num(self) -> int:
        return self.get_pops_num_by_state(PopState.vaccinated)

    def get_recovered_pops_num(self) -> int:
        return self.get_pops_num_by_state(PopState.recovered)

    def introduce_law(self, law: Law) -> None:
        self.laws.append(law)
        for pop in self.pops:
            for modifier in law.happiness_modifiers:
                if 'all' in modifier:
                    pop.happiness = pop.happiness + modifier['all']
                elif 'wearing_mask' in modifier and pop.mask_on:
                    pop.happiness = pop.happiness + modifier['wearing_mask']
                elif 'not_wearing_mask' in modifier and not pop.mask_on:
                    pop.happiness = pop.happiness - modifier['not_wearing_mask']
                elif 'young' in modifier and pop.age < 40:
                    pop.happiness = pop.happiness + modifier['young']
                elif 'old' in modifier and pop.age > 50:
                    pop.happiness = pop.happiness + modifier['old']

    def revoke_law(self, law: Law) -> None:
        self.laws.remove(law)
        for pop in self.pops:
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

    def compute_pops_changes(self, state_laws: List[Law], turn: int) -> None:
        ill_number = 0
        for pop in self.pops:
            if pop.state == PopState.ill:
                ill_number += 1

        def dice_roll() -> int:
            return randint(0, 99)

        for pop in self.pops:
            if pop.state == PopState.dead:
                self.pops.remove(pop)
            elif pop.state == PopState.ill:
                if dice_roll() < self.DEATH_CHANCE:
                    pop.state = PopState.dead
                elif dice_roll() < self.QUARANTINE_CHANCE:
                    pop.quarantined = True
                elif turn - pop.illness_date > 2:
                    pop.state = PopState.recovered
                    pop.quarantined = False
            elif pop.state == PopState.healthy:
                infection_chance = int(100 * ill_number / len(self.pops))
                infection_chance = City.compute_infection_chance(self.laws, pop, infection_chance)
                infection_chance = City.compute_infection_chance(state_laws, pop, infection_chance)
                if dice_roll() < infection_chance:
                    pop.state = PopState.ill
            elif pop.state == PopState.recovered:
                if dice_roll() < self.RECOVERED_CHANCE:
                    pop.state = PopState.healthy

    @staticmethod
    def compute_infection_chance(laws: List[Law], pop: Pop, infection_chance: int):
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

        return infection_chance
