import sys
import pygame

from .menu_button import MenuButton
from settings import Colors


class Menu:
    BUTTONS_INIT_HEIGHT = 200
    BUTTONS_DIST = 10

    def __init__(self, width):
        self._running = True
        self.current_menu_option = 0

        self.width = width
        self.buttons = pygame.sprite.Group()

        button_names = [
            'START',
            'QUIT',
        ]

        height = self.BUTTONS_INIT_HEIGHT
        for button_name in button_names:
            button = MenuButton(button_name, Colors.WHITE.value, 200, 100, button_name)
            button.rect.center = (self.width // 2, height)
            height += self.BUTTONS_DIST + button.rect.height
            self.buttons.add(button)

    def initialize(self, app_surface):
        app_surface.fill(Colors.BLUE.value)

    def on_render(self):
        pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            mouse_sprite = pygame.sprite.Sprite()
            mouse_sprite.rect = pygame.rect.Rect((x, y), (1, 1))
            for button in self.buttons:
                if pygame.sprite.collide_rect(button, mouse_sprite):
                    if button.name == 'START':
                        self._running = False
                    elif button.name == 'QUIT':
                        sys.exit(0)

    def run(self, app_surface):
        self.initialize(app_surface)

        while self._running:
            self.buttons.draw(app_surface)
            for event in pygame.event.get():
                self.on_event(event)

            self.on_render()
