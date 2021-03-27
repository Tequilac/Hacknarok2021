import json
from typing import List
from game import City
from pathlib import Path


class CitiesParser:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def load_cities(self) -> List[City]:
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        cities = data['cities']
        cities_list = []
        for city in cities:
            cities_list.append(City(city['name'], city['pops_num'], tuple(city['cord'])))

        return cities_list
