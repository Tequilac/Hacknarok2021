import pygame
from .button import *
from settings import Colors


class CitiesOptionButton(Button):
    BUTTON_SIZE = {
        'width': 200,
        'height': 75,
    }
    CITY_OPTIONS_FONT_SIZE = 18
    CITY_OPTIONS_FONT = pygame.font.SysFont("calibri", CITY_OPTIONS_FONT_SIZE)

    def __init__(self, text, color, name, location):
        self.surface = pygame.Surface((self.BUTTON_SIZE['width'], self.BUTTON_SIZE['height']))
        self.surface.fill(Colors.RED.value)
        super().__init__(name, self.surface, location)
        self.font = self.CITY_OPTIONS_FONT
        self.textSurf = self.font.render(text, True, color)
        w = self.textSurf.get_width()
        h = self.textSurf.get_height()
        self.image.blit(self.textSurf, (self.BUTTON_SIZE['width'] / 2 - w / 2, self.BUTTON_SIZE['height'] / 2 - h / 2))