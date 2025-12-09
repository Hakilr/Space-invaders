import random
import sys
import pygame
from pygame.sprite import Sprite, Group

ALIEN_BULLET_WIDTH = 4
ALIEN_BULLET_HEIGHT = 10
ALIEN_TYPE_1 = 1
ALIEN_TYPE_2 = 2
ALIEN_TYPE_3 = 3
ALIEN_TYPE_1_ROWS = 2
ALIEN_TYPE_2_ROWS = 4
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


class Settings:
    """Game settings container."""

    def __init__(self) -> None:
        # Alien movement
        self.alien_speed_x = 0.6
        self.alien_drop_y = 20

        # Alien bullets
        self.alien_bullet_color = (255, 255, 0)
        self.alien_bullet_speed = 1.4
        self.alien_bullet_chance = 0.0002  # per frame, per alien


class Alien(Sprite):
    """Represents a single alien unit."""

    def __init__(
        self,
        settings: Settings,
        x: int,
        y: int,
        alien_type: int,
    ):
        super().__init__()
        self.settings = settings

        # Load the alien images
        if alien_type == ALIEN_TYPE_1:
            self.image = pygame.image.load("images/invader1.bmp").convert()
        elif alien_type == ALIEN_TYPE_2:
            self.image = pygame.image.load("images/invader2.bmp").convert()
        else:
            self.image = pygame.image.load("images/invader3.bmp").convert()

        self.image.set_colorkey((0, 0, 0))


        # Apply color tint based on alien type
        color_map = {
            ALIEN_TYPE_1: COLOR_RED,
            ALIEN_TYPE_2: COLOR_GREEN,
            ALIEN_TYPE_3: COLOR_BLUE,
        }
        tint_color = color_map.get(alien_type)
        if tint_color:
            self.image.fill(tint_color, special_flags=pygame.BLEND_RGBA_MULT)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)

        # 1 for moving right, -1 for moving left
        self.move_direction = 1

    def update(self, horizontal_speed: float) -> bool:
        """Move horizontally and report if a screen edge was hit."""
        self.x += horizontal_speed * self.move_direction
        self.rect.x = self.x

        hit_edge = False
        # Edge detection removed - no screen boundaries
        return hit_edge

    def drop_and_reverse(self) -> None:
        """Move the alien down and reverse its horizontal direction."""
        self.rect.y += self.settings.alien_drop_y
        self.move_direction *= -1

    def shoot(self, bullets_group: Group) -> None:
        """Create a new bullet from the alien's position."""
        bullet = AlienBullet(
            self.settings, self.rect.centerx, self.rect.bottom
        )
        bullets_group.add(bullet)


class AlienBullet(Sprite):
    # bullet shot by an alien

    def __init__(self, settings: Settings, x: int, y: int):
        super().__init__()
        self.settings = settings

        self.image = pygame.Surface((ALIEN_BULLET_WIDTH, ALIEN_BULLET_HEIGHT))
        self.image.fill(self.settings.alien_bullet_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.y = float(self.rect.y)

    def update(self) -> None:
        # Move the bullet downward
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y


class SpaceInvader:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.aliens: Group["Alien"] = Group()
        self.alien_bullets: Group["AlienBullet"] = Group()

        self._create_alien_grid()
        self.clock = pygame.time.Clock()

    # Create fleet

    def _create_alien_grid(self) -> None:
        """Create a grid of aliens."""
        # Temporary alien to get width/height
        temp_alien = Alien(self.settings, 0, 0, ALIEN_TYPE_1)
        alien_width = temp_alien.rect.width
        alien_height = temp_alien.rect.height
        temp_alien.kill()


        horizontal_spacing = 1.3 * alien_width
        vertical_spacing = 1.4 * alien_height

        # Horizontal layout - fixed number of aliens
        number_aliens_x = 10

        # Vertical layout: enough rows to show all three types
        number_rows = 6

        for row in range(number_rows):
            for col in range(number_aliens_x):
                if row < ALIEN_TYPE_1_ROWS:
                    alien_type = ALIEN_TYPE_1
                elif row < ALIEN_TYPE_2_ROWS:
                    alien_type = ALIEN_TYPE_2
                else:
                    alien_type = ALIEN_TYPE_3

                x = alien_width + int(horizontal_spacing * col)
                y = alien_height + int(vertical_spacing * row)

                alien = Alien(self.settings, x, y, alien_type)
                self.aliens.add(alien)

    def _current_alien_speed(self) -> float:
        """Return the current horizontal speed, scaling with remaining aliens."""
        base_speed = self.settings.alien_speed_x

        # Speed up slightly as aliens are destroyed (never below base_speed)
        total = max(1, len(self.aliens))
        speed_factor = 1.0 + (0.5 * (1.0 - total / 60.0))
        return base_speed * speed_factor

    def _update_aliens(self) -> None:
        """Update alien positions, handle edges, and random shooting."""
        if not self.aliens:
            return

        edge_hit = False
        current_speed = self._current_alien_speed()

        # Move aliens and detect edge hits
        for alien in self.aliens.sprites():
            if alien.update(current_speed):
                edge_hit = True

            # Random shooting
            if random.random() < self.settings.alien_bullet_chance:
                alien.shoot(self.alien_bullets)

        # If any alien hit an edge, drop fleet and reverse direction
        if edge_hit:
            for alien in self.aliens.sprites():
                alien.drop_and_reverse()

    def _update_bullets(self) -> None:
        self.alien_bullets.update()

    # ---------------------------------------------------------------------
    # Main loop
    # ---------------------------------------------------------------------

    def run(self) -> None:
        """Main loop for the demo game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._update_aliens()
            self._update_bullets()

            self.clock.tick(60)


def main() -> None:
    """Entry point to run the game."""
    game = SpaceInvader()
    game.run()


if __name__ == "__main__":
    main()