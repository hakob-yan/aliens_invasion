import sys
import pygame
from settings import  Settings
from ship import Ship
from bullet import  Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.display.set_caption('Alien Invasion')
        self.settings=Settings()
        self.bg_image = self.settings.bg_image
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.ship =Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self,event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_UP:
                self.ship.moving_top = True
            if event.key == pygame.K_DOWN:
                self.ship.moving_bottom = True
            if event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key==pygame.K_q:
                sys.exit()
    def _check_keyup_events(self,event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            if event.key == pygame.K_UP:
                self.ship.moving_top = False
            if event.key == pygame.K_DOWN:
                self.ship.moving_bottom = False
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                  self._check_keyup_events(event)
    def _update_screen(self):
        self.  screen.blit(self.bg_image, (0, 0))
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def run_game(self):
        """Start the main Loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            self._update_bullets()





ai = AlienInvasion()
ai.run_game()
