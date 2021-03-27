from random import randint

import pygame

from .pop_state import *

class City(pygame.sprite.Sprite):
    def __init__(self, name, pops, image_file, law, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (70, 62))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.name = name
        self.pops = pops
        self.x_cords, self.y_cords = location
        self.law = law

    def compute_pops_changes(self, state_laws, turn):
        ill_number = 0
        for pop in self.pops:
            if pop.state == PopState.ill:
                ill_number = ill_number + 1

        death_chance = 10

        for pop in self.pops:
            if pop.state == PopState.dead:
                self.pops.remove(pop)
            elif pop.state == PopState.ill:
                if randint(0, 99) < death_chance:
                    pop.state = PopState.dead
                elif turn - pop.illness_date > 2:
                    pop.state = PopState.recovered
            elif pop.state == PopState.healthy:
                infection_chance = int(100 * ill_number / len(self.pops))
                self.compute_infection_chance(self.law, pop, infection_chance)
                self.compute_infection_chance(state_laws, pop, infection_chance)
                if randint(0, 99) < infection_chance:
                    pop.state = PopState.ill


    def compute_infection_chance(self, laws, pop, infection_chance):
        for law in laws:
            for modifier in law.infection_chance_modifiers:
                if 'all' in modifier:
                    infection_chance = infection_chance + modifier['all']
                elif 'wearing_mask' in modifier and pop.mask_on:
                    infection_chance = infection_chance + modifier['wearing_mask']
                elif 'young' in modifier and pop.age < 40:
                    infection_chance = infection_chance + modifier['young']
                elif 'old' in modifier and pop.age > 50:
                    infection_chance = infection_chance + modifier['old']
