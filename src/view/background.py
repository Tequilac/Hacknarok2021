import pygame
import settings

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        MAP_SIZE = {
            'width': 900,
            'heigth': 900,
        }

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), settings.WINDOWS_SIZE)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location