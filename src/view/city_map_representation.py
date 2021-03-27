import pygame

class CityMapRepresentation(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        CITY_SIZE = {
            'width': 70,
            'heigth': 62,
        }

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (CITY_SIZE['width'], CITY_SIZE['heigth']))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
