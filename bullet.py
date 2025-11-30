import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    """Class to manage bullets"""

    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = self.settings.bullet_color


    #create bullet and set position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = si_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # Move bullet & update position.
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
        # Remove bullet if it goes off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect)