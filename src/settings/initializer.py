from random import randint

from game import city
from game import Pop
from game import PopState
from resources import cities_parser


class Initializer:
    def initialize_cities(self):
        cities_list = cities_parser.load_cities()
        cities_list_to_return = []
        for city_name, city_cord, pops_num in cities_list:
            pops = []
            for _ in range(pops_num):
                state = PopState.healthy
                if randint(0, 99) < 10:
                    state = PopState.ill
                age = randint(10, 80)
                pops.append(Pop(state, -1, False, False, age, 100))
            cities_list_to_return.append(city.City(city_name, pops, [], city_cord))
        return cities_list_to_return

