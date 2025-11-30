import pygame
from alien import Alien
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class AlienFleet:

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

    def create_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        fleet_arrangement = {
            1: self._create_rectangle_fleet,
            2: self._create_pyramid_fleet,
            3: self._create_diamond_fleet
        }
        random_number = random.randint(1, 3)
        fleet_arrangement[random_number](alien_h, alien_w, fleet_h, fleet_w, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_h, fleet_w, x_offset, y_offset):
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def _create_pyramid_fleet(self, alien_h: int, alien_w: int, fleet_h: int, fleet_w: int, x_offset: int,
                              y_offset: int):
        n = fleet_h
        # space out ships
        gap = 10
        for i in range(n, 0, -1):
            leading_space = n - i
            aliens_per_row = 2 * i - 1
            row_y = (n - i) * (alien_h + gap) + y_offset

            for a in range(aliens_per_row):
                column = leading_space + a
                if 0 <= column < fleet_w:
                    current_x = column * (alien_w + gap) + x_offset
                    self._create_alien(current_x, row_y)

    def _create_diamond_fleet(self, alien_h: int, alien_w: int, fleet_h: int, fleet_w: int, x_offset: int,
                              y_offset: int):
        # Reduce height since shape is very big otherwise
        n = fleet_h - 2
        # space out ships
        gap = 10
        for i in range(1, n + 1):
            leading_space = n - i
            aliens_per_row = 2 * i - 1
            row_y = (i - 1) * (alien_h + gap) + y_offset
            for a in range(aliens_per_row):
                current_x = (leading_space + a) * (alien_w + gap) + x_offset
                self._create_alien(current_x, row_y)

        # other half
        for i in range(n - 1, 0, -1):
            leading_space = n - i
            aliens_per_row = 2 * i - 1
            row_y = (2 * n - i - 1) * (alien_h + gap) + y_offset
            for a in range(aliens_per_row):
                current_x = (leading_space + a) * (alien_w + gap) + x_offset
                self._create_alien(current_x, row_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w-fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h /2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2


        return int(fleet_w), int(fleet_h)

        
    def _create_alien(self, current_x: int, current_y:int):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break


    def _drop_alien_fleet(self):
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed


    def update_fleet(self):
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        return not self.fleet