import pygame
from state import State
from globals import *
from eventmanager import EventManager

class Settings(State):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen

        self.font = pygame.font.Font(None, 36)
        self.settings_title = self.font.render('Settings', True, (0, 0, 0))
        self.settings_title_rect = self.settings_title.get_rect() 
        self.settings_title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        self.return_text = self.font.render('Return', True, (0, 0, 0))
        self.return_text_rect = self.return_text.get_rect()
        self.return_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # gets mouse position
                if self.return_text_rect.collidepoint(mouse_pos):
                    self.game.game_state_stack.pop()
                    return True
            return False
    def update(self):
        self.handle_events(EventManager.events)
    def render(self, screen):
        self.draw()
    def draw(self):
        self.screen.fill('grey')
        self.screen.blit(self.settings_title, self.settings_title_rect)
        self.screen.blit(self.return_text, self.return_text_rect)

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
