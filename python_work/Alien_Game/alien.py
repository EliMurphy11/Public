import sys

import pygame

class AlienInvasion:
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("alien Invasion")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start the main loop for the game."""
        


