from random import randint


class State:
    def __init__(self, laws, last_election, cities):
        self.laws = laws
        self.last_election = last_election
        self.cities = cities

    def compute_migrations(self):
        migration_chance = 2
        for i in range(len(self.cities)):
            for pop in self.cities[i].pops:
                if randint(0, 99) < migration_chance:
                    self.cities[i].pops.remove(pop)
                    chosen_city = randint(1, len(self.cities) - 1)
                    self.cities[(i + chosen_city) % len(self.cities)].append(pop)
