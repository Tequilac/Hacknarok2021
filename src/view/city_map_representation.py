import pygame

class CityMapRepresentation(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (70, 62))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
