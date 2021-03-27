import pygame
import menu
import settings


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = settings.WINDOWS_SIZE
        self.menu = menu.Menu(self.width)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self._display_surf.fill(settings.Colors.BLUE.value)
        self.menu.initialize(self._display_surf)

        pygame.display.update()

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
        self.on_init()

        self.menu.run(self._display_surf)

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
