from globals import *
from player import Player
import pygame

class PlayerStats:
    def __init__(self, app, player) -> None:
        self.app = app
        self.player = player
        self.screen = app.screen

        self.font = pygame.font.Font(None, 30)
    def update(self):
        pass
    def draw(self):
        self.health_text = self.font.render(f'Health: {str(self.player.health)}', True, "black")
        self.screen.blit(self.health_text, (10,75))
