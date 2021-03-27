import pygame
import settings


class Background:
    def __init__(self, image_file, location):
        self.image = pygame.transform.scale(pygame.image.load(image_file), settings.WINDOWS_SIZE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
