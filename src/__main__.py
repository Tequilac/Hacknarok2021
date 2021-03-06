import pygame
import menu
import settings
import sys
import game_over
import game
#import this
from settings import Paths
from view.visualizer import Visualizer
from parsers import CitiesParser


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = settings.WINDOWS_SIZE
        self.back_ground = None
        self.menu = menu.Menu(self.width)
        self.game = None
        self.visualizer = None
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

        cities_list = CitiesParser.load_cities()
        self.game = game.Game(0, cities_list)
        self.visualizer = Visualizer(self.game)

        self.visualizer.initialize_background(settings.Paths.RESOURCES / 'country_map.png', self._display_surf)
        self.visualizer.initialize_cities_on_map(cities_list, settings.Paths.RESOURCES / 'city.png', self._display_surf)
        self.visualizer.initialize_city_options_buttons(self.game.city_laws, self._display_surf)
        self.visualizer.initialize_state_options_buttons(self.game.state_laws, self._display_surf)
        self.visualizer.initialize_next_turn_button(settings.Paths.RESOURCES / 'next_turn.png', self._display_surf)

        pygame.display.flip()
        pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            mouse_sprite = pygame.sprite.Sprite()
            mouse_sprite.rect = pygame.rect.Rect((x, y), (1, 1))
            for button in self.visualizer.buttons:
                if pygame.sprite.collide_rect(button, mouse_sprite):
                    if hasattr(button, 'button_type'):
                        if button.button_type == 'CITY_MAP_BUTTON':
                            self.visualizer.current_selected_law = None
                            self.visualizer.clear_law_info_field(self._display_surf)
                            for button_2 in self.visualizer.buttons:
                                if hasattr(button_2, 'button_type'):
                                    if button_2.button_type == 'ENACT_REVOKE_TYPE':
                                        self.visualizer.clear_law_button_field(button_2.rect, self._display_surf)
                                        self.visualizer.buttons.remove(button_2)
                            for city in self.game.state.cities:
                                if city.name == button.name:
                                    if self.visualizer.current_selected_city is not None:
                                        self.visualizer.clear_city_info_field(self._display_surf)
                                    self.visualizer.display_city_info(city, self._display_surf)
                                    self.visualizer.update_city_buttons(self._display_surf, self.game)
                                    if self.visualizer.current_selected_law is not None:
                                        for button_1 in self.visualizer.buttons:
                                            if hasattr(button, 'button_type') and button.button_type == 'ENACT_REVOKE_TYPE':
                                                self.visualizer.clear_law_button_field(button_1.rect, self._display_surf)
                                        if self.visualizer.current_selected_law in city.laws:
                                            self.visualizer.display_law_info(self.visualizer.current_selected_law, False,
                                                                             self._display_surf)
                                        else:
                                            self.visualizer.display_law_info(self.visualizer.current_selected_law, True,
                                                                             self._display_surf)

                                    break
                        elif button.button_type == 'CITY_BUTTON':
                            self.visualizer.update_state_buttons(self._display_surf, self.game)
                            current_selected_city = self.visualizer.current_selected_city
                            if current_selected_city is not None:
                                for law in self.game.city_laws:
                                    if law.name == button.name:
                                        self.visualizer.current_selected_law = law
                                        self.visualizer.update_city_buttons(self._display_surf, self.game)
                                        button.surface.fill(settings.Colors.VERY_LIGHT_BLUE.value)
                                        if law in current_selected_city.laws:
                                            self.visualizer.display_law_info(law, False, self._display_surf)
                                        else:
                                            self.visualizer.display_law_info(law, True, self._display_surf)
                                        button.render(self._display_surf)
                        elif button.button_type == 'STATE_BUTTON':
                            self.visualizer.update_city_buttons(self._display_surf, self.game)
                            for law in self.game.state_laws:
                                if law.name == button.name:
                                    self.visualizer.current_selected_law = law
                                    self.visualizer.update_state_buttons(self._display_surf, self.game)
                                    button.surface.fill(settings.Colors.VERY_LIGHT_BLUE.value)
                                    if law in self.game.state.laws:
                                        self.visualizer.display_law_info(law, False, self._display_surf)
                                    else:
                                        self.visualizer.display_law_info(law, True, self._display_surf)
                                    #else:
                                        #button.surface.fill(settings.Colors.GREEN.value)
                                    button.render(self._display_surf)
                        elif button.button_type == 'ENACT_REVOKE_TYPE':
                            if self.visualizer.current_selected_law in self.game.city_laws:
                                if button.name == 'Enact law':
                                    self.visualizer.current_selected_city.introduce_law(self.visualizer.current_selected_law)
                                    self.visualizer.clear_law_info_field(self._display_surf)
                                    self.visualizer.display_law_info(self.visualizer.current_selected_law, False, self._display_surf)

                                else:
                                    self.visualizer.current_selected_city.revoke_law(self.visualizer.current_selected_law)
                                    self.visualizer.clear_law_info_field(self._display_surf)
                                    self.visualizer.display_law_info(self.visualizer.current_selected_law, True, self._display_surf)
                                self.visualizer.update_city_buttons(self._display_surf, self.game)
                            else:
                                if button.name == 'Enact law':
                                    self.visualizer.game.state.introduce_law(self.visualizer.current_selected_law)
                                    self.visualizer.clear_law_info_field(self._display_surf)
                                    self.visualizer.display_law_info(self.visualizer.current_selected_law, False, self._display_surf)

                                else:
                                    self.visualizer.game.state.revoke_law(self.visualizer.current_selected_law)
                                    self.visualizer.clear_law_info_field(self._display_surf)
                                    self.visualizer.display_law_info(self.visualizer.current_selected_law, True, self._display_surf)
                                self.visualizer.update_state_buttons(self._display_surf, self.game)
                    elif button.name == 'NEXT_TURN':
                        self.game.next_turn()

    def on_loop(self):
        #print(pygame.mouse.get_pos())
        self.visualizer.clear_elections_statistics(self._display_surf)
        self.visualizer.display_elections_statistics(self._display_surf, self.game)
        if self.visualizer.current_selected_city is not None:
            self.visualizer.clear_city_info_field(self._display_surf)
            self.visualizer.display_city_info(self.visualizer.current_selected_city, self._display_surf)

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

            if self.game.elections.last_elections_result < 30:
                self._running = False

        self.game_over.run(self._display_surf)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
