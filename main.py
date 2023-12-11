# main.py
import pygame
import sys
from globals import *
from scenes.mainmenu.mainmenu import MainMenu
from eventmanager import EventManager
from statestack import StateStack

'''
    # Game class
    # This class is the main class of the game. It handles the game loop and the game states.
'''
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen
        self.clock = pygame.time.Clock() # Set the clock
        self.running = True 
        self.state = None 
        self.player = None
        self.game_state_stack = StateStack(self) # Create a state stack
        self.event_manager = EventManager()
        self.event_manager.register_listener(self.game_state_stack) # Register the state stack as a listener

    def update(self):
        self.event_manager.poll_events() # Poll events
        self.game_state_stack.handle_events(EventManager.events) # Handle events

        self.game_state_stack.update() # Update the state stack
    
    def draw(self):
        self.game_state_stack.render(self.screen) # Render the state stack
        pygame.display.update() # Update the display

    def close(self):
        pygame.quit()
        sys.exit()
    
    def handle_events(self):
        events = pygame.event.get() # Get all events
        for event in events: # Iterate through events
            if event.type == pygame.QUIT: # If the user quits
                self.running = False # Set running to false
                return
        for state in reversed(self.game_state_stack.states): # Iterate through the states in reverse in the stack
            if state.handle_events(events): # If the state handles the events, break
                break
    
    def run(self):
        self.game_state_stack.push(MainMenu) # Initialize the game state stack with the main menu

        # Main game loop
        while self.running:
            self.handle_events() 
            self.update() 
            self.draw() 
            self.clock.tick(FPS) 

        self.close()

if __name__ == "__main__":
    game = Game()
    game.run()
