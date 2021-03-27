import json
from src.settings import RESOURCES_PATH


def load_cities():
    data = json.load(open(RESOURCES_PATH + 'cities.json'))
    cities = data['cities']
    citiesList = []
    for city in cities:
        city_name = city['name']
        city_cord = city['cord']
        pops_num = city['pops_num']
        citiesList.append((city_name, (city_cord[0], city_cord[1]), pops_num))
    return citiesList