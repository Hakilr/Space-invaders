import pygame
import sys
from ship import Ship
from settings import Settings
from alien import Alien
from gamemanager import GameManager, BulletManager, EventHandler, DrawingManager


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
        
        # Create game manager
        self.game_manager = GameManager(self.settings, self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT)
        
        # Create bullet manager
        self.bullet_manager = BulletManager(self)
        
        # Create event handler and renderer
        self.event_handler = EventHandler(self)
        self.renderer = DrawingManager(self)
        
        self.clock = pygame.time.Clock()
        self.running = True
    
    def reset_game(self):
        # Reset game state
        self.ship = Ship("images/ship.bmp", self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT, self.settings)
        self.alien = Alien("images/invader1.bmp", self.settings.SCREEN_WIDTH, 50)
        self.game_manager.ship_lives = 3
        self.bullet_manager.bullets.empty()
        self.bullet_manager.alien_bullets.empty()
    
    def run(self):
        while self.running:
            # Handle events
            self.event_handler.handle_events()
            
            # Handle continuous movement
            self.event_handler.handle_continuous_movement()
            
            # Update bullets
            self.bullet_manager.update()
            
            # Randomly fire alien bullets
            self.bullet_manager.fire_alien_bullet(self.alien)
            
            # Check collisions
            self.alien = self.game_manager.check_bullet_alien_collisions(self.bullet_manager.bullets, self.alien)
            self.ship = self.game_manager.check_alien_bullet_ship_collisions(self.bullet_manager.alien_bullets, self.ship)
            
            # Check if game is over (after collision checks)
            if self.game_manager.is_game_over(self.alien):
                # Show game over screen
                self.renderer.draw_game_over()
                pygame.display.flip()
                self.clock.tick(self.settings.FPS)
                continue
            
            # Draw everything
            self.renderer.draw()

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)
        
        pygame.quit()
        sys.exit()

si = Space_Invaders()
si.run()

