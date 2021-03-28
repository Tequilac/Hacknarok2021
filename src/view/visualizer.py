from .background import *
from .city_map_representation import *
from .city_options_button import *
from settings import Colors



class Visualizer:
    BUTTON_SPACE_DISTANCE= {
        'horizontal': 20,
        'vertical': 20,
    }
    CITY_INFO_FONT_SIZE = 18
    CITY_INFO_FONT = pygame.font.SysFont("calibri", CITY_INFO_FONT_SIZE)

    def __init__(self):
        self.first_city_options_button_position = (1006, 272)
        self.first_state_options_button_position = (1455, 20)
        self.city_info_position = (1030, 35)
        self.buttons = []
        self.current_selected_city = None

    def initialize_background(self, file_name, display_surf):
        back_ground = Background(file_name, (0, 0))
        display_surf.fill(Colors.WHITE.value)
        display_surf.blit(back_ground.image, back_ground.rect)

    def initialize_cities_on_map(self, cities, file_name,  display_surf):
        for city in cities:
            city_representation = CityMapRepresentation(file_name, city.name, city.location, 'CITY_MAP_BUTTON')
            city_representation.render(display_surf)
            self.buttons.append(city_representation)

    def initialize_city_options_buttons(self, city_laws, display_surf):
        counter = 0
        for law in city_laws:
            city_options_button = CitiesOptionButton(
                law.name,
                Colors.WHITE.value,
                law.name,
                (self.first_city_options_button_position[0] +
                                  (counter % 2) * (CitiesOptionButton.BUTTON_SIZE['width']
                                   + self.BUTTON_SPACE_DISTANCE['vertical']),
                 self.first_city_options_button_position[1] +
                                   (counter // 2) * (CitiesOptionButton.BUTTON_SIZE['height']
                                                     + self.BUTTON_SPACE_DISTANCE['horizontal'])
                                   ), 'CITY_BUTTON')
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
                (self.first_state_options_button_position[0] +
                                  (counter % 2) * (CitiesOptionButton.BUTTON_SIZE['width']
                                   + self.BUTTON_SPACE_DISTANCE['vertical']),
                 self.first_state_options_button_position[1] +
                                   (counter // 2) * (CitiesOptionButton.BUTTON_SIZE['height']
                                                     + self.BUTTON_SPACE_DISTANCE['horizontal'])
                                   ), 'STATE_BUTTON')
            city_options_button.render(display_surf)
            self.buttons.append(city_options_button)
            counter = counter + 1

    def display_city_info(self, city, display_surf):
        self.current_selected_city = city
        font = self.CITY_INFO_FONT
        name_text_surf = font.render(str(city.name), True, Colors.BLACK.value)
        healthy_pops_text_surf = font.render("Num of healthy pops:" + str(city.get_healthy_pops_num()), True, Colors.BLACK.value)
        recovered_pops_text_surf = font.render("Num of recovered pops:" + str(city.get_recovered_pops_num()), True, Colors.BLACK.value)
        vaccinated_pops_text_surf = font.render("Num of vaccinated pops:" + str(city.get_vaccinated_pops_num()), True, Colors.BLACK.value)
        ill_pops_text_surf = font.render("Num of ill pops:" + str(city.get_ill_pops_num()), True, Colors.BLACK.value)
        dead_pops_text_surf = font.render("Num of dead pops:" + str(city.get_dead_pops_num()), True, Colors.BLACK.value)

        display_surf.blit(name_text_surf, self.city_info_position)
        display_surf.blit(healthy_pops_text_surf, (self.city_info_position[0], self.city_info_position[1] + 20))
        display_surf.blit(recovered_pops_text_surf, (self.city_info_position[0], self.city_info_position[1] + 40))
        display_surf.blit(vaccinated_pops_text_surf, (self.city_info_position[0], self.city_info_position[1] + 60))
        display_surf.blit(ill_pops_text_surf, (self.city_info_position[0], self.city_info_position[1] + 80))
        display_surf.blit(dead_pops_text_surf, (self.city_info_position[0], self.city_info_position[1] + 100))

    def clear_city_info_field(self, display_surf):
        surface = pygame.Surface((250, 150))
        surface.fill(Colors.WHITE.value)
        display_surf.blit(surface, self.city_info_position)

    def update_city_buttons(self, display_surf, game):
        if self.current_selected_city is not None:
            for law in game.city_laws:
                for button in self.buttons:
                    if button.name == law.name:
                        if law in self.current_selected_city.laws:
                            button.surface.fill(settings.Colors.GREEN.value)
                        else:
                            button.surface.fill(settings.Colors.RED.value)
                    button.render(display_surf)





