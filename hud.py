import pygame.font
# from alien_invasion import AlienInvasion
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:

class HUD:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.HUD_font_size)
        self.padding = 25
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_w * 0.85, self.settings.ship_h * 0.85
            ))
        self.life_image = pygame.transform.rotate(self.life_image, -90)
        self.life_rect = self.life_image.get_rect()
    


    def update_scores(self):
        self._update_max_score()
        self._update_score()
        self._update_hi_score()
        padding_between = 25
        self.score_rect.midright = (
            self.hi_score_rect.left - padding_between, self.hi_score_rect.centery
        )
        self.max_score_rect.midleft = (
            self.hi_score_rect.right + padding_between, self.max_score_rect.centery
        )

    def _update_score(self):
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        hi_score_str = f'Hi-Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx,self.padding)

    def update_level(self):
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, 
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()

        self.level_rect.bottom = self.boundaries.bottom - 8
        self.level_rect.right = self.boundaries.right - 20

    def _draw_lives(self):
        bar_height = self.settings.bar_h
        bar_top = self.boundaries.bottom - bar_height

        current_x = self.padding
        current_y = bar_top + (bar_height - self.life_rect.height) // 2
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        self._draw_bar()
        self.screen.blit(self.hi_score_image,self.hi_score_rect)
        self.screen.blit(self.max_score_image,self.max_score_rect)
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self._draw_lives()

    def _draw_bar(self):
        bar_height = self.settings.bar_h
        bar_line_height = self.settings.bar_top_line_h

        bar_rect = pygame.Rect(
            0,
            self.boundaries.bottom - bar_height,
            self.boundaries.width,
            bar_height
        )
        pygame.draw.rect(self.screen, (0,0,0), bar_rect)
        pygame.draw.rect(self.screen, (150, 35, 185), pygame.Rect(bar_rect.x, bar_rect.y, bar_rect.width, bar_line_height))