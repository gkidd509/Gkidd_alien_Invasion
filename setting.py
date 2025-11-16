from pathlib import Path

class Settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_width: int = 1280
        self.screen_height: int = 720
        self.FPS = 60
        self.bg_file = Path.cwd() / 'assets' / 'images' / 'Starbasesnow.png'
