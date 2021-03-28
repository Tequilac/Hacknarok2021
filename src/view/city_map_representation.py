from .button import *
from settings import Colors


class CityMapRepresentation(Button):
    CITY_SIZE = {
        'width': 100,
        'height': 75,
    }

    CITY_FONT_SIZE = 18
    CITY_FONT = pygame.font.SysFont("calibri", CITY_FONT_SIZE)
    TEXT_VERTICAL_TRANSPOSITION = 77
    TEXT_HORIZONTAL_TRANSPOSITION = 15

    def __init__(self, image_file, name, location):
        super().__init__(name, pygame.transform.scale(pygame.image.load(image_file),
                        (self.CITY_SIZE['width'], self.CITY_SIZE['height'])), location)
        self.font = self.CITY_FONT
        self.textSurf = self.font.render(self.name, True, Colors.BLACK.value)

    def render(self, display_surf):
        display_surf.blit(self.image, self.rect)
        display_surf.blit(self.textSurf,
                          (self.rect.left + self.TEXT_HORIZONTAL_TRANSPOSITION,
                           self.rect.top + self.TEXT_VERTICAL_TRANSPOSITION))

