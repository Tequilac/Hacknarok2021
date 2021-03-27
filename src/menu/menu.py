import sys
import settings
import pygame


class Menu:
    BUTTONS = [
        'start_game',
        'quit',
    ]
    BUTTONS_HEIGHT = {
        'start_game' : 150,
        'quit' : 170,
    }

    def __init__(self, width):
        self._running = True
        self.current_menu_option = 0

        self.width = width

        self.start_game_button = settings.MENU_FONT.render('Start', False, settings.Colors.BLACK.value,
                                                           settings.Colors.VERY_LIGHT_BLUE.value)
        # self.

    def initialize(self, app_surface):
        app_surface.fill(settings.Colors.BLUE.value)
        textsurface = settings.MENU_FONT.render('Menu XD', False, settings.Colors.WHITE.value)

        app_surface.blit(self.start_game_button, ((self.width - self.start_game_button.get_width()) // 2,
                                                  self.BUTTONS_HEIGHT['start_game']))

        pygame.display.update()


    def on_render(self, app_surface):
        pass
        #app_surface.blit(self.start_game_button, ((self.width - self.start_game_button.get_width()) // 2,
        #                                          self.BUTTONS_HEIGHT['start_game']))
        # left_edge_cord = 0
        # top_cord = self.BUTTONS_HEIGHT[self.BUTTONS[self.current_menu_option]]
        # rectangle = pygame.Rect(left_edge_cord, top_cord, 30, 30)
        # rect_surface = pygame.surface.Surface((rectangle.w, rectangle.h))
        # pygame.draw.rect(app_surface, settings.Colors.VERY_LIGHT_BLUE.value, rectangle)
        # pygame.display.update()
        # app_surface.blit(rect_surface)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYUP:
            self.current_menu_option = (self.current_menu_option + len(self.BUTTONS) - 1) % len(self.BUTTONS)
        if event.type == pygame.KEYDOWN:
            self.current_menu_option = (self.current_menu_option + 1) % len(self.BUTTONS)

    def run(self, app_surface):
        self.initialize(app_surface)

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render(app_surface)
