import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the spaceship'''

    def __init__(self, pi_settings, screen, ship):
        '''Creat a bullet object at the ship's position'''
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0,0, pi_settings.bullet_width, pi_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.color = pi_settings.bullet_color
        self.speed = pi_settings.bullet_speed

    def update(self):
        '''Move the bullet up the scree'''
        # Update the decimal position of the bullet.
        self.y -= self.speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)