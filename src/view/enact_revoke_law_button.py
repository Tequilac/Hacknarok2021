import pygame
from .button import *
from settings import Colors


class EnactRevokeLawButton(Button):
    BUTTON_SIZE = {
        'width': 210,
        'height': 75,
    }
    CITY_OPTIONS_FONT_SIZE = 18
    CITY_OPTIONS_FONT = pygame.font.SysFont("calibri", CITY_OPTIONS_FONT_SIZE)

    def __init__(self, text, color, fill_color, name, location, button_type):
        self.surface = pygame.Surface((self.BUTTON_SIZE['width'], self.BUTTON_SIZE['height']))
        self.surface.fill(fill_color)
        super().__init__(name, self.surface, location)
        self.font = self.CITY_OPTIONS_FONT
        self.textSurf = self.font.render(text, True, color)
        self.button_type = button_type
        w = self.textSurf.get_width()
        h = self.textSurf.get_height()
        self.image.blit(self.textSurf, (self.BUTTON_SIZE['width'] / 2 - w / 2, self.BUTTON_SIZE['height'] / 2 - h / 2))

    def render(self, display_surf):
        w = self.textSurf.get_width()
        h = self.textSurf.get_height()
        self.image.blit(self.textSurf, (self.BUTTON_SIZE['width'] / 2 - w / 2, self.BUTTON_SIZE['height'] / 2 - h / 2))
        display_surf.blit(self.image, self.rect)