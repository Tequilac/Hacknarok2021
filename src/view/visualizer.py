from .background import *
from .city_map_representation import *
from .city_options_button import *
from settings import Colors



class Visualizer:
    BUTTON_SPACE_DISTANCE= {
        'horizontal': 20,
        'vertical': 20,
    }

    def __init__(self):
        self.first_button_position = (1006, 272)
        self.buttons = []

    def initialize_background(self, file_name, display_surf):
        back_ground = Background(file_name, (0, 0))
        display_surf.fill(Colors.WHITE.value)
        display_surf.blit(back_ground.image, back_ground.rect)

    def initialize_cities_on_map(self, cities, file_name,  display_surf):
        for city in cities:
            city_representation = CityMapRepresentation(file_name, city.name, city.location)
            city_representation.render(display_surf)
            self.buttons.append(city_representation)

    def initialize_city_options_buttons(self, city_laws, display_surf):
        counter = 0
        for law in city_laws:
            city_options_button = CitiesOptionButton(
                law.name,
                Colors.WHITE.value,
                law.name,
                (self.first_button_position[0] +
                                  (counter % 2) * (CitiesOptionButton.BUTTON_SIZE['width']
                                   + self.BUTTON_SPACE_DISTANCE['vertical']),
                 self.first_button_position[1] +
                                   (counter // 2) * (CitiesOptionButton.BUTTON_SIZE['height']
                                                     + self.BUTTON_SPACE_DISTANCE['horizontal'])
                                   ))
            city_options_button.render(display_surf)
            self.buttons.append(city_options_button)
            counter = counter + 1

    def initialize_state_options_buttons(self, state_laws, display_surf):
        counter = 0
        for law in state_laws:
            city_options_button = CitiesOptionButton(
                law.name,
                Colors.WHITE.value,
                law.name,
                (self.first_button_position[0] +
                                  (counter % 2) * (CitiesOptionButton.BUTTON_SIZE['width']
                                   + self.BUTTON_SPACE_DISTANCE['vertical']),
                 self.first_button_position[1] +
                                   (counter // 2) * (CitiesOptionButton.BUTTON_SIZE['height']
                                                     + self.BUTTON_SPACE_DISTANCE['horizontal'])
                                   ))
            city_options_button.render(display_surf)
            self.buttons.append(city_options_button)
            counter = counter + 1




