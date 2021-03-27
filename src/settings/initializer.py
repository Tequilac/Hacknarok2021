from random import randint

import view
import settings
from game import city
from game import Pop
from game import PopState
from resources import cities_parser


class Initializer:
    def initialize_background(self, file_name, display_surf):
        back_ground = view.background.Background(file_name, (0, 0))
        display_surf.fill(settings.colors.Colors.WHITE.value)
        display_surf.blit(back_ground.image, back_ground.rect)

    def initialize_cities(self, file_name, display_surf):
        cities_list = cities_parser.load_cities()
        for city_name, city_cord, pops_num in cities_list:
            pops = []
            for _ in range(pops_num):
                state = PopState.healthy
                if randint(0, 99) < 10:
                    state = PopState.ill
                age = randint(10, 80)
                pops.append(Pop(state, -1, False, False, age, 100))
            city_obj = city.City(city_name, pops, [], city_cord)
            city_representation = view.city_map_representation.CityMapRepresentation(file_name,
                                                                                city_obj.name, city_obj.location)
            display_surf.blit(city_representation.image, city_representation.rect)
