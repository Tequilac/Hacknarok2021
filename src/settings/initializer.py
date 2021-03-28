from random import randint
from game import City
from typing import List
from game import Pop, PopState
from parsers import CitiesParser


class Initializer:
    BASIC_HAPPINESS_OF_THE_NOT_ANGRY_YET_MOB = 100

    # @staticmethod
    # def initialize_cities() -> List[City]:
    #     cities_list = CitiesParser.load_cities()
    #     for city in cities_list:
    #         pops = [Pop(state=PopState.ill if randint(0, 99) < 10 else PopState.healthy,
    #                     illness_date=-1,
    #                     mask_on=False,
    #                     quarantined=False,
    #                     age=randint(10, 80),
    #                     happiness=Initializer.BASIC_HAPPINESS_OF_THE_NOT_ANGRY_YET_MOB)
    #                 for _ in range(pops_num)]
    #         city.pops = pops
    #
    #     return cities_list

