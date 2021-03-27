import sys
import pygame

from settings import MENU_FONT, Colors


class Menu:
    BUTTONS_INIT_HEIGHT = 200
    BUTTONS_DIST = 10
    BUTTONS_NAMES = [
        'START',
        'QUIT',
    ]

    def __init__(self, width):
        self._running = True
        self.current_menu_option = 0

        self.width = width
        self.buttons = {
            self.BUTTONS_NAMES[0]: MENU_FONT.render(self.BUTTONS_NAMES[0],
                                                    True,
                                                    Colors.BLACK.value,
                                                    Colors.VERY_LIGHT_BLUE.value),
            self.BUTTONS_NAMES[1]: MENU_FONT.render(self.BUTTONS_NAMES[1],
                                                    True,
                                                    Colors.BLACK.value,
                                                    Colors.VERY_LIGHT_BLUE.value),
        }
        self.buttons_num = len(self.BUTTONS_NAMES)
        self.buttons_heights = []
        height_sum = self.BUTTONS_INIT_HEIGHT
        for i, button_name in enumerate(self.buttons.values()):
            button_name = self.buttons[self.BUTTONS_NAMES[i]]

            self.buttons_heights += [height_sum]
            height_sum += button_name.get_height() + self.BUTTONS_DIST

    def initialize(self, app_surface):
        app_surface.fill(Colors.BLUE.value)
        self.draw_buttons(app_surface)
        pygame.display.update()

    def draw_buttons(self, app_surface):
        height_sum = self.BUTTONS_INIT_HEIGHT

        for i, button_name in enumerate(self.buttons.values()):
            app_surface.blit(button_name, ((self.width - button_name.get_width()) // 2, height_sum))
            height_sum += button_name.get_height() + self.BUTTONS_DIST

    def on_render(self, app_surface):
        app_surface.fill(Colors.BLUE.value)
        current_button = self.buttons[self.BUTTONS_NAMES[self.current_menu_option]]
        left_cord = 0
        top_cord = self.buttons_heights[self.current_menu_option]
        rectangle = pygame.Rect((left_cord, top_cord), (self.width, current_button.get_height()))
        pygame.draw.rect(app_surface, Colors.VERY_LIGHT_BLUE.value, rectangle)
        self.draw_buttons(app_surface)
        pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.current_menu_option = (self.current_menu_option - 1) % self.buttons_num
            elif event.key == pygame.K_UP:
                self.current_menu_option = (self.current_menu_option + 1) % self.buttons_num
            elif event.key == pygame.K_RETURN:
                self.action_perform()

    def action_perform(self):
        if self.BUTTONS_NAMES[self.current_menu_option] == 'START':
            self._running = False
        elif self.BUTTONS_NAMES[self.current_menu_option] == 'QUIT':
            sys.exit(0)

    def run(self, app_surface):
        self.initialize(app_surface)

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render(app_surface)
