import pygame
import sys
from ship import Ship
from settings import Settings
from alien import Alien
from gamemanager import GameManager, BulletManager


class EventHandler:
    # Handles all keyboard input and events
    
    def __init__(self, si_game):
        self.si_game = si_game
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.si_game.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self.si_game.bullet_manager.fire_player_bullet()
    
    def handle_continuous_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.si_game.ship.move_left()
        if keys[pygame.K_RIGHT]:
            self.si_game.ship.move_right()


class DrawingManager:
    # Handles all drawing operations
    
    def __init__(self, si_game):
        self.si_game = si_game
    
    def draw(self):
        # Fill the screen
        self.si_game.screen.fill(self.si_game.settings.BG_COLOUR)
        
        # Draw the ship
        if self.si_game.ship:
            self.si_game.ship.draw(self.si_game.screen)
        
        # Draw the alien
        if self.si_game.alien:
            self.si_game.alien.draw(self.si_game.screen)
        
        # Draw bullets
        self.si_game.bullet_manager.draw()


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
            
            # Check if game is over
            if self.game_manager.is_game_over():
                self.running = False
            
            # Draw everything
            self.renderer.draw()

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)
        
        pygame.quit()
        sys.exit()

si = Space_Invaders()
si.run()

