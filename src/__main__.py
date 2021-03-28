import pygame
import menu
import settings
import game_over
import game
from settings import Paths
from view.visualizer import Visualizer


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = settings.WINDOWS_SIZE
        self.back_ground = None
        self.menu = menu.Menu(self.width)
        self.game = None
        self.visualizer = Visualizer()
        self.game_over = game_over.GameOver(self.width)

    def on_init_pygame(self):
        pygame.init()
        music_file = Paths.RESOURCES / 'main_theme.wav'
        pygame.mixer.init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        pygame.event.wait()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def game_init(self):
        self._running = True

        cities_list = settings.Initializer.initialize_cities()
        self.game = game.Game(0, cities_list)

        self.visualizer.initialize_background(settings.Paths.RESOURCES / 'country_map.png', self._display_surf)
        self.visualizer.initialize_cities_on_map(cities_list, settings.Paths.RESOURCES / 'city.png', self._display_surf)
        self.visualizer.initialize_city_options_buttons(self.game.city_laws, self._display_surf)
        self.visualizer.initialize_state_options_buttons(self.game.state_laws, self._display_surf)
        self.visualizer.initialize_next_turn_button(settings.Paths.RESOURCES / 'next_turn.png', self._display_surf)

        pygame.display.flip()
        pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            mouse_sprite = pygame.sprite.Sprite()
            mouse_sprite.rect = pygame.rect.Rect((x, y), (1, 1))
            for button in self.visualizer.buttons:
                if pygame.sprite.collide_rect(button, mouse_sprite):
                    if button.button_type == 'CITY_MAP_BUTTON':
                        for city in self.game.state.cities:
                            if city.name == button.name:
                                if self.visualizer.current_selected_city is not None:
                                    self.visualizer.clear_city_info_field(self._display_surf)
                                self.visualizer.display_city_info(city, self._display_surf)
                                self.visualizer.update_city_buttons(self._display_surf, self.game)
                                break
                    elif button.button_type == 'CITY_BUTTON':
                        current_selected_city = self.visualizer.current_selected_city
                        if current_selected_city is not None:
                            for law in self.game.city_laws:
                                if law.name == button.name:
                                    if law in current_selected_city.laws:
                                        self.visualizer.display_law_info(law, False, self._display_surf)
                                        current_selected_city.revoke_law(law)
                                        button.surface.fill(settings.Colors.RED.value)
                                    else:
                                        self.visualizer.display_law_info(law, True, self._display_surf)
                                        current_selected_city.introduce_law(law)
                                        button.surface.fill(settings.Colors.GREEN.value)
                                    button.render(self._display_surf)
                    elif button.button_type == 'STATE_BUTTON':
                        for law in self.game.state_laws:
                            if law.name == button.name:
                                if law in self.game.state.laws:
                                    button.surface.fill(settings.Colors.RED.value)
                                else:
                                    button.surface.fill(settings.Colors.GREEN.value)
                                button.render(self._display_surf)

    def on_loop(self):
        print(pygame.mouse.get_pos())
        self.visualizer.display_elections_statistics(self._display_surf, self.game)

    def on_render(self):
        pygame.display.flip()
        pygame.display.update()

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
