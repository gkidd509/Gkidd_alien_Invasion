from pathlib import Path

class Settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_width: int = 1280
        self.screen_height: int = 720
        self.FPS = 60
        self.bg_file = Path.cwd() / 'assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
