from state import State
from globals import *
from eventmanager import EventManager
import pygame

class Credits(State):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen

        self.font = pygame.font.Font(None, 36)

        self.credits_title = self.font.render('Credits', True, (0, 0, 0))
        self.credits_title_rect = self.credits_title.get_rect() 
        self.credits_title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        self.thanks_text = self.font.render('Thanks to Corbin for his help!', True, (0, 0, 0))
        self.thanks_text_rect = self.thanks_text.get_rect()
        self.thanks_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.return_text = self.font.render('Return', True, (0, 0, 0))
        self.return_text_rect = self.return_text.get_rect()
        self.return_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5) 

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.game.game_state_stack.states)
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
        self.screen.blit(self.credits_title, self.credits_title_rect)
        self.screen.blit(self.thanks_text, self.thanks_text_rect)
        self.screen.blit(self.return_text, self.return_text_rect)
