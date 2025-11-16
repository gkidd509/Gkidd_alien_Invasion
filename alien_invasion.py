import sys
import pygame
from setting import Settings

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

    def run_game(self):
        # Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg, (0,0))
            pygame.display.flip()
            self.clock.tick(self.setting.FPS)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
