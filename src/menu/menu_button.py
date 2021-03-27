import pygame
import settings


class MenuButton(pygame.sprite.Sprite):
    def __init__(self, text: str, color: settings.Colors, width: int, height: int, name: str):
        super().__init__()
        self.font = settings.MENU_FONT
        self.name = name
        self.textSurf = self.font.render(text, True, color)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        w = self.textSurf.get_width()
        h = self.textSurf.get_height()
        self.image.blit(self.textSurf, (width / 2 - w / 2, height / 2 - h / 2))
