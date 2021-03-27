from view import background, city_map_representation
from settings import colors

class Visualizer:
    def initialize_background(self, file_name, display_surf):
        back_ground = background.Background(file_name, (0, 0))
        display_surf.fill(colors.Colors.WHITE.value)
        display_surf.blit(back_ground.image, back_ground.rect)

    def initialize_cities_on_map(self, cities, file_name,  display_surf):
        for city in cities:
            city_representation = city_map_representation.\
                CityMapRepresentation(file_name, city.name, city.location)
            display_surf.blit(city_representation.image, city_representation.rect)
