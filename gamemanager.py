import random
import pygame
from ship import Ship
from bullet import fire_bullet, fire_alien_bullet, update_bullets, draw_bullets


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
            if self.si_game.game_manager.is_game_over(self.si_game.alien):
                # Restart game if game is over
                self.si_game.reset_game()
            else:
                # Fire bullet during normal gameplay
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
        # Initialize font for lives counter
        self.font = pygame.font.Font(None, 36)
    
    def draw_lives_counter(self):
        # Draw the lives counter in the top-left corner
        lives_text = f"Lives: {self.si_game.game_manager.ship_lives}"
        lives_surface = self.font.render(lives_text, True, (255, 255, 255))
        lives_rect = lives_surface.get_rect()
        lives_rect.topleft = (10, 10)
        self.si_game.screen.blit(lives_surface, lives_rect)
    
    def draw_game_over(self):
        self.si_game.screen.fill(self.si_game.settings.BG_COLOUR)
        
        center_x = self.si_game.settings.SCREEN_WIDTH // 2
        center_y = self.si_game.settings.SCREEN_HEIGHT // 2
        
        # Game over text
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(center_x, center_y - 30))
        self.si_game.screen.blit(text, rect)
        
        # Restart instruction
        text = self.font.render("Press SPACE to restart", True, (255, 255, 255))
        rect = text.get_rect(center=(center_x, center_y + 30))
        self.si_game.screen.blit(text, rect)
    
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
        
        # Draw lives counter
        self.draw_lives_counter()


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
    
    def is_game_over(self, alien=None):
        # Check if game is over (ship has no lives or alien is killed)
        return self.ship_lives <= 0 or alien is None

