import sys
import pygame
from setting import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption(self.setting.name)

        #Background settings
        self.bg = pygame.image.load(self.setting.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.setting.screen_width, self.setting.screen_height))

        self.running = True
        self.clock = pygame.time.Clock()

        #Ship settings
        self.ship = Ship(self)


    def run_game(self):
        # Game Loop
        while self.running:
            self._check_events()

            self._update_screen()
            self.clock.tick(self.setting.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
