import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    '''Initialize game and create a screen object.'''
    pygame.init()
    pi_settings = Settings()
    screen = pygame.display.set_mode((pi_settings.screen_width, pi_settings.screen_height))
    pygame.display.set_caption("Python Invaders")

    # Make a play button.
    play_button = Button(pi_settings, screen, "Play")

    # Create an instance to store game stats and create a scoreboard
    stats = GameStats(pi_settings)
    sb = Scoreboard(pi_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(pi_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens

    gf.create_fleet(pi_settings, screen, ship, aliens)

    #Start the main loop for the game
    while True:
        gf.check_events(pi_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(pi_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(pi_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(pi_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()