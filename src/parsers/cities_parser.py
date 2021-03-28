import json
from typing import List
from game import City
from settings import Paths


class CitiesParser:
    CITIES_PATH = Paths.RESOURCES / 'cities.json'

    @staticmethod
    def load_cities() -> List[City]:
        with open(CitiesParser.CITIES_PATH, 'r') as f:
            data = json.load(f)
        cities = data['cities']
        cities_list = []
        for city in cities:
            cities_list.append(City(city['name'], city['pops_num'], tuple(city['cord'])))

        return cities_list
