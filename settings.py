from pathlib import Path

class Settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w: int = 1280
        self.screen_h: int = 720
        self.FPS = 60
        """
        Background credits:
        Name: Space Background
        Author: drakzlin
        Link: https://opengameart.org/content/space-background-7
        """
        self.bg_file = Path.cwd() / 'assets' / 'images' / 'bg_space_seamless.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        """
        Ship sprite credits:
        Pack name: Various Spaceship models
        Author: Sypher Zent
        Link: https://opengameart.org/content/various-spaceship-models
        """
        self.ship_file = Path.cwd() / 'assets' / 'images' / 'cooler_ship.png'
        self.ship_w = 40
        self.ship_h = 60
        """
        Laser image was taken from the "beams" image found in the assets folder included with the starter project.
        """
        self.bullet_file = Path.cwd() / 'assets' / 'images' / 'laser_bulb_fire.png'
        """
        Laser sound credits:
        Pack name: Space Battle Game Sounds (AstroMenace)
        Author: Michael Kurinnoy
        link: https://opengameart.org/content/space-battle-game-sounds-astromenace
        """
        self.laser_sound = Path.cwd() / 'assets' / 'sound' / 'weaponfire6.wav'
        """
        Impact sound credits:
        Sound name: Short Impact
        Author: Soundsnap
        Link: https://opengameart.org/content/short-impact
        """
        self.impact_sound = Path.cwd() / 'assets' / 'sound' / 'shortimpact.wav'

        """
        Alien ship sprite credits:
        Pack name: Various Spaceship models
        Author: Sypher Zent
        Link: https://opengameart.org/content/various-spaceship-models
        """
        self.alien_file = Path.cwd() / 'assets' / 'images' / 'drone_1_blue.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        """
        Font Credits:
        Name: Conthrax
        Author: Typodermic Fonts
        Link: https://www.dafont.com/conthrax.font
        """
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Conthrax' / 'Conthrax-SemiBold.otf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale