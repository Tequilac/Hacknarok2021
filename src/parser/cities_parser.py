import json


class CitiesParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_cities(self) -> list:
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        cities = data['cities']
        cities_list = []
        for city in cities:
            city_name = city['name']
            city_cord = city['cord']
            pops_num = city['pops_num']
            cities_list += [(city_name, (city_cord[0], city_cord[1]), pops_num)]

        return cities_list
