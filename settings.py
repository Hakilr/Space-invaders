class Settings:
    # Settings for Space Invaders
    def __init__(self):
        # Screen settings
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.BG_COLOUR = (0, 0, 0)
        self.FPS = 60
        self.CAPTION = "Space Invaders"
        
        # Ship settings
        self.ship_speed = 5
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_speed = 5.0
        self.bullets_allowed = 3

