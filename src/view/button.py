import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, name, image, location):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def render(self, display_surf):
        display_surf.blit(self.image, self.rect)