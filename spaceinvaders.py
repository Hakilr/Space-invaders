import pygame
import sys
from ship import Ship
from bullet import Bullet

class Settings:
    """Settings for Space Invaders"""
    def __init__(self):
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_speed = 5.0

class Space_Invaders:
    def __init__(self):
        pygame.init()
        
        # Set up the display
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        
        self.COLOUR = (0, 0, 0)
        
        # Initialize settings
        self.settings = Settings()
        
        # Create ship instance
        self.ship = Ship("images/ship.bmp", self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
        # Create sprite group for bullets
        self.bullets = pygame.sprite.Group()
        
        self.clock = pygame.time.Clock()
        self.running = True
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < 3:  # Limit bullets on screen
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()
    
    def _draw_bullets(self):
        """Draw bullets on the screen."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
    def run(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
            
            # continuous movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.ship.move_left()
            if keys[pygame.K_RIGHT]:
                self.ship.move_right()
            
            # Update bullets
            self._update_bullets()
            
            # Fill the screen
            self.screen.fill(self.COLOUR)
            
            # Draw the ship
            self.ship.draw(self.screen)
            
            # Draw bullets
            self._draw_bullets()

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

si = Space_Invaders()
si.run()

