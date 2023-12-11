# mainemnu.py is the main menu of the game. It is the first thing the player sees when they open the game.
import pygame
from scenestate import SceneState
from globals import *
from eventmanager import EventManager
from testscene import TestScene
from settings import Settings
from credits import Credits

class MainMenuSceneState(SceneState):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen

        self.font = pygame.font.Font(None, 36) 
        self.play_text = self.font.render('Play', True, (0, 0, 0)) 
        self.play_text_rect = self.play_text.get_rect() 
        self.play_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.settings_text = self.font.render('Settings', True, (0, 0, 0))
        self.settings_text_rect = self.settings_text.get_rect()
        self.settings_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50) 

        self.credits_text = self.font.render('Credits', True, (0, 0, 0))
        self.credits_text_rect = self.credits_text.get_rect()
        self.credits_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)  

        self.quit_text = self.font.render('Quit', True, (0, 0, 0))
        self.quit_text_rect = self.quit_text.get_rect()
        self.quit_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)  

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicks
                mouse_pos = pygame.mouse.get_pos()  # gets mouse position
                if self.play_text_rect.collidepoint(mouse_pos):
                    self.game.state_stack.change_state(TestScene)
                    return True
                elif self.settings_text_rect.collidepoint(mouse_pos):
                    self.game.state_stack.push(Settings)
                    return True
                elif self.credits_text_rect.collidepoint(mouse_pos):
                    self.game.state_stack.push(Credits)
                    return True
                elif self.quit_text_rect.collidepoint(mouse_pos):
                    self.game.close()
                    return True
            return False
        
    def update(self):
        self.handle_events(EventManager.events)

    def render(self, screen):
        self.draw()
        pygame.display.update()

    def draw(self):
        self.screen.fill('grey')
        self.draw_text("Main Menu", self.font, 'black', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        self.draw_text("Play", self.font, 'black', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.draw_text("Settings", self.font, 'black', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        self.draw_text("Credits", self.font, 'black', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        self.draw_text("Quit", self.font, 'black', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
