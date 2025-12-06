import random
import pygame
from ship import Ship
from bullet import fire_bullet, fire_alien_bullet, update_bullets, draw_bullets


class BulletManager:
    # Manages all bullet operations
    
    def __init__(self, si_game):
        self.si_game = si_game
        self.bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
    
    def fire_player_bullet(self):
        fire_bullet(self.bullets, self.si_game)
    
    def fire_alien_bullet(self, alien):
        if alien and self.si_game.game_manager.should_fire_alien_bullet():
            fire_alien_bullet(self.alien_bullets, alien, self.si_game)
    
    def update(self):
        update_bullets(self.bullets)
        update_bullets(self.alien_bullets)
    
    def draw(self):
        draw_bullets(self.bullets)
        draw_bullets(self.alien_bullets)


class GameManager:
    # Manages game state, collisions
    
    def __init__(self, settings, screen_width, screen_height):
        self.settings = settings
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ship_lives = 3
    
    def check_bullet_alien_collisions(self, bullets, alien):
        # Check if bullets hit the alien
        if alien:
            colliding_bullets = [bullet for bullet in bullets if bullet.rect.colliderect(alien.rect)]
            if colliding_bullets:
                for bullet in colliding_bullets:
                    bullets.remove(bullet)
                return None  # Alien dies
        return alien
    
    def check_alien_bullet_ship_collisions(self, alien_bullets, ship):
        # Check if alien bullets hit the ship
        if ship:
            colliding_bullets = [bullet for bullet in alien_bullets if bullet.rect.colliderect(ship.rect)]
            if colliding_bullets:
                for bullet in colliding_bullets:
                    alien_bullets.remove(bullet)
                self.ship_lives -= 1
                if self.ship_lives > 0:
                    # Respawn the ship
                    return Ship("images/ship.bmp", self.screen_width, self.screen_height, self.settings)
                else:
                    # No lives left, game over
                    return None
        return ship
    
    def should_fire_alien_bullet(self):
        # Determine if alien should fire based on probability
        firing_probability = 1 / 120
        return random.random() < firing_probability
    
    def is_game_over(self):
        # Check if game is over
        return self.ship_lives <= 0

