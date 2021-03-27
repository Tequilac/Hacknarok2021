import pygame
import background
import city
from pygame.locals import *
import menu
import settings

pygame.font.init()

class App:
    GAME_FONT = pygame.font.SysFont("Arial.ttf", 24)

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 950, 950
        self.back_ground = None
        self.menu = menu.Menu()

    def on_init(self):
        pygame.init()
        self.back_ground = background.Background('../resources/country_map.png', [0, 0])
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill([255, 255, 255])
        self._display_surf.blit(self.back_ground.image, self.back_ground.rect)
        self._running = True

        for i in range(1, 16):
            city_obj = city.City(i, None, '../resources/city.png', None, [626 / i, 626 / i])
            self._display_surf.blit(city_obj.image, city_obj.rect)

        pygame.display.flip()

        """self._display_surf.fill(settings.Colors.BLUE.value)
        textsurface = self.GAME_FONT.render('Menu XD', False, settings.Colors.WHITE.value)
        self._display_surf.blit(textsurface, (0, 0))
        pygame.display.update()"""

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.KEYUP:
            pass

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
