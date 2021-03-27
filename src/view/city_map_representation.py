import pygame


class CityMapRepresentation(pygame.sprite.Sprite):
    CITY_SIZE = {
            'width': 85,
            'height': 75,
    }

    def __init__(self, image_file, name, location):
        self.name = name
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file),
                                            (self.CITY_SIZE['width'], self.CITY_SIZE['height']))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
