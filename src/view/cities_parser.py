import json


def load_cities():
    data = json.load(open('../src/view/cities.json'))
    cities = data['cities']
    citiesList = []
    for city in cities:
        city_name = city['name']
        city_cord = city['cord']
        citiesList.append((city_name, (city_cord[0], city_cord[1])))
    return citiesList