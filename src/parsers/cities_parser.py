import json
from typing import List
from game import City
from settings import Paths
from random import randint
from game import PopState, Pop


class CitiesParser:
    BASIC_HAPPINESS_OF_THE_NOT_ANGRY_YET_MOB = 100
    CITIES_PATH = Paths.RESOURCES / 'cities.json'

    @staticmethod
    def load_cities() -> List[City]:
        with open(CitiesParser.CITIES_PATH, 'r') as f:
            data = json.load(f)
        cities = data['cities']
        cities_list = []
        pops_num = []
        for city in cities:
            cities_list.append(City(city['name'], tuple(city['cord'])))
            pops_num.append(city['pops_num'])

        for i, city in enumerate(cities_list):
            pops = [Pop(state=PopState.ill if randint(0, 99) < 10 else PopState.healthy,
                        illness_date=-1,
                        mask_on=False,
                        quarantined=False,
                        age=randint(10, 80),
                        happiness=CitiesParser.BASIC_HAPPINESS_OF_THE_NOT_ANGRY_YET_MOB)
                    for _ in range(pops_num[i])]
            city.pops = pops

        return cities_list
