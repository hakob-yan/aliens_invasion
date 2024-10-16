import sys
import pygame
from settings import  Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.display.set_caption('Alien Invasion')
        self.settings=Settings()
        self.bg_color = self.settings.bg_color
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.ship =Ship(self)


    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
                if event.key==pygame.K_LEFT:
                    self.ship.moving_left=True


            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        """Start the main Loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)




ai = AlienInvasion()
ai.run_game()
