"""
Lab 13: Custom Assets
Gavin Kidd
This is a modification of the alien_invasion project to use custom assets for the alien and alien fleet formation
11/23/2025
"""

import sys
import pygame
from setting import Settings
from ship import Ship
from arsenal import Arsenal
#from alien import Alien
from alien_fleet import AlienFleet

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

        #Sounds
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.setting.laser_sound)
        self.laser_sound.set_volume(0.5)

        #Ship settings
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()


    def run_game(self) -> None:
        # Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            #self.alien.update()
            self._update_screen()
            self.clock.tick(self.setting.FPS)

    def _update_screen(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right =True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(500)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
