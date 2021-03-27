import sys
import pygame

from .menu_button import MenuButton
from settings import Colors


class Menu:
    BUTTONS_INIT_HEIGHT = 200
    BUTTONS_DIST = 10
    BUTTON_SIZE = (200, 100)
    BUTTONS_NAMES = [
        'START',
        'QUIT',
    ]

    def __init__(self, width: int):
        self._running = True
        self.current_menu_option = 0
        self.width = width
        self.buttons = []

        # Initializing
        self.initialize_buttons()

    def initialize_buttons(self) -> None:

        height = self.BUTTONS_INIT_HEIGHT
        for button_name in self.BUTTONS_NAMES:
            button = MenuButton(button_name, Colors.WHITE.value, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1], button_name)
            button.rect.center = (self.width // 2, height)
            height += self.BUTTONS_DIST + button.rect.height
            self.buttons.append(button)

    def initialize(self, app_surface: pygame.Surface) -> None:
        app_surface.fill(Colors.BLUE.value)

    def on_event(self, event : pygame.event.Event) -> None:
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

    def run(self, app_surface: pygame.Surface) -> None:
        self.initialize(app_surface)
        pygame.sprite.Group(self.buttons).draw(app_surface)

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            pygame.display.update()
