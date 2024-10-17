import pygame

class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_image = pygame.image.load('images/space.jpg')
        self.ship_speed=15
        self.bullet_speed=2.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(255,0,0,0)
        self.bullets_allowed = 3
