import pygame
import random
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.setting
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

    def create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_width
        screen_h = self.settings.screen_height

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_h, alien_w, fleet_h, fleet_w, screen_w)

        fleet_arrangement = {
            1: self._create_rectangle_fleet,
            2: self._create_pyramid_fleet
        }
        random_number = random.randint(1, 2)
        fleet_arrangement[random_number](alien_h, alien_w, fleet_h, fleet_w, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_h: int, alien_w: int, fleet_h: int, fleet_w: int, x_offset: int,
                                y_offset: int):
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def _create_pyramid_fleet(self, alien_h: int, alien_w: int, fleet_h: int, fleet_w: int, x_offset: int, y_offset: int):
        n = fleet_h

        for i in range(n, 0, -1):
            leading_space = n - i
            aliens_per_row = 2 * i - 1
            row_y = (n-i) * alien_h + y_offset

            for a in range(aliens_per_row):
                column = leading_space + a
                if 0 <= column < fleet_w:
                    current_x = column * alien_w + x_offset
                    self._create_alien(current_x, row_y)


    def calculate_offsets(self, alien_h: int, alien_w: int, fleet_h: int, fleet_w: int,
                          screen_w: int) -> tuple[int, int]:
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h) -> tuple[int, int]:
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int) -> None:
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
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    def check_destroyed_status(self):
        return not self.fleet