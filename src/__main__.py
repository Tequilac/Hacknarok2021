import pygame
from game import city
from src.view import background, city_map_representation
import menu
import settings

RESOURCES_PATH = '../resources/'


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
        self.back_ground = background.Background(RESOURCES_PATH + 'country_map.png', (0, 0))

        self._display_surf.fill(settings.colors.Colors.WHITE.value)
        self._display_surf.blit(self.back_ground.image, self.back_ground.rect)
        self._running = True

        for i in range(1, 16):
            city_obj = city.City(i, None, None, (626 / i, 626 / i))
            city_representation = city_map_representation.CityMapRepresentation(RESOURCES_PATH + 'city.png', city_obj.location)
            self._display_surf.blit(city_representation.image, city_representation.rect)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
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
