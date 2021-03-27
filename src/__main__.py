import pygame
from settings.initializer import Initializer
import menu
import settings
from view.visualizer import Visualizer


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = settings.WINDOWS_SIZE
        self.back_ground = None
        self.menu = menu.Menu(self.width)

    def on_init_pygame(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def game_init(self):
        self._running = True

        visualizer = Visualizer()
        initializer = Initializer()

        cities_list = initializer.initialize_cities()

        visualizer.initialize_background(settings.RESOURCES_PATH + 'country_map.png', self._display_surf)
        visualizer.initialize_cities_on_map(cities_list, settings.RESOURCES_PATH + 'city.png', self._display_surf)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        # print(pygame.mouse.get_pos())
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init_pygame()

        self.menu.run(self._display_surf)

        self.game_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
