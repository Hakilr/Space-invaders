import pygame
import sys
from ship import Ship
from bullet import Bullet, fire_bullet, update_bullets, draw_bullets
from settings import Settings
from alien import Alien

class Space_Invaders:
    def __init__(self):
        pygame.init()
        
        # Initialize settings
        self.settings = Settings()
        
        # Set up the display
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption(self.settings.CAPTION)
        
        # Create ship instance
        self.ship = Ship("images/ship.bmp", self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT, self.settings)
        
        # Create a single alien instance
        self.alien = Alien("images/invader1.bmp", self.settings.SCREEN_WIDTH, 50)
        
        # Create sprite group for bullets
        self.bullets = pygame.sprite.Group()
        
        self.clock = pygame.time.Clock()
        self.running = True
    
    def _check_keydown_events(self, event):
        # spacebar to fire bullets
        if event.key == pygame.K_SPACE:
            fire_bullet(self.bullets, self)
    
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
            update_bullets(self.bullets)
            
            # Fill the screen
            self.screen.fill(self.settings.BG_COLOUR)
            
            # Draw the ship
            self.ship.draw(self.screen)
            
            # Draw the alien
            self.alien.draw(self.screen)
            
            # Draw bullets
            draw_bullets(self.bullets)

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)
        
        pygame.quit()
        sys.exit()

si = Space_Invaders()
si.run()

