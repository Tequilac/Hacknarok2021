import pygame


class Button(pygame.sprite.Sprite):
    BUTTON_SIZE = {
        'width': 85,
        'height': 75,
    }

    def __init__(self, name, image, location):
        super().__init__()
        self.name = name
        if image is None:
            self.image = pygame.Surface((self.BUTTON_SIZE['width'], self.BUTTON_SIZE['height']))
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def render(self, display_surf):
        display_surf.blit(self.image, self.rect)