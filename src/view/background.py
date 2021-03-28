import pygame
import settings


class Background:
    BACKGROUND_WIDTH = 1000
    BACKGROUND_HEIGHT = 1000

    def __init__(self, image_file, location):
        self.image = pygame.transform.scale(
            pygame.image.load(image_file),
            (self.BACKGROUND_WIDTH, self.BACKGROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
