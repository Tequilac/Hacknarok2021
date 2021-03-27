import settings
import parsers
import pygame
import view

from pathlib import Path


class Initializer:
    LEFT_UPPER_CORNER = (0, 0)

    @staticmethod
    def initialize_background(filepath: Path, surface: pygame.Surface):
        back_ground = view.Background(filepath, Initializer.LEFT_UPPER_CORNER)
        surface.fill(settings.colors.Colors.WHITE.value)
        surface.blit(back_ground.image, back_ground.rect)

    @staticmethod
    def initialize_cities(filepath: Path, surface: pygame.Surface):
        cities_parser = parsers.CitiesParser(settings.Paths.RESOURCES / 'cities.json')

        cities_list = cities_parser.load_cities()
        for city in cities_list:
            city_representation = view.CityMapRepresentation(filepath, city.name, city.location)
            surface.blit(city_representation.image, city_representation.rect)
