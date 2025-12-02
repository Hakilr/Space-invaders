import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    # class to manage bullets

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


def fire_bullet(bullets, si_game):
    # Create a new bullet and add it to the bullets group
    if len(bullets) < si_game.settings.bullets_allowed:  # Limit bullets on screen
        new_bullet = Bullet(si_game)
        bullets.add(new_bullet)


def update_bullets(bullets):
        # Update position of bullets and get rid of old bullets
    bullets.update()


def draw_bullets(bullets):
    # Draw bullets on the screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()


class AlienBullet(Sprite):
    def __init__(self, alien, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = alien.rect.midbottom
        
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y
        
        if self.rect.top > self.settings.SCREEN_HEIGHT:
            self.kill()
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def fire_alien_bullet(alien_bullets, alien, si_game):
    if len(alien_bullets) < si_game.settings.bullets_allowed:
        new_bullet = AlienBullet(alien, si_game)
        alien_bullets.add(new_bullet)