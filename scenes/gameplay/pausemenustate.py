import pygame
from state import State
from globals import *
from eventmanager import EventManager
import scenes.mainmenu.mainmenu

class PauseMenu(State):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen

        self.font = pygame.font.Font(None, 36)
        self.return_text = self.font.render('Return', True, (0, 0, 0))
        self.return_text_rect = self.return_text.get_rect()
        self.return_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 

        self.pause_title = self.font.render('Paused', True, (0, 0, 0))
        self.pause_title_rect = self.pause_title.get_rect() 
        self.pause_title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        self.main_menu_text = self.font.render('Main Menu', True, (0, 0, 0))
        self.main_menu_text_rect = self.main_menu_text.get_rect()
        self.main_menu_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # gets mouse position
                if self.return_text_rect.collidepoint(mouse_pos):
                    self.game.game_state_stack.pop()
                elif self.main_menu_text_rect.collidepoint(mouse_pos):
                    self.game.game_state_stack.pop()
                    self.game.game_state_stack.change_state(scenes.mainmenu.mainmenu.MainMenu)
                '''
                elif self.main_menu_text_rect.collidepoint(mouse_pos):
                    # Save Data
                    # Pop all States below
                    # Push mainmenu state
                '''
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state_stack.pop()
    def update(self):
        self.handle_events(EventManager.events)
    def render(self, screen):
        self.draw()
        pygame.display.update()
    def draw(self):
        self.screen.blit(self.pause_title, self.pause_title_rect)
        self.screen.blit(self.return_text, self.return_text_rect)
        self.screen.blit(self.main_menu_text, self.main_menu_text_rect)
