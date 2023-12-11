import pygame

class EventManager:
    def __init__(self) -> None:
        self.listeners = []
        EventManager.events = pygame.event.get()
    def register_listener(self, listener):
        self.listeners.append(listener)
    def poll_events(self):
        self.events = pygame.event.get()
        for listener in self.listeners:
            listener.handle_events(self.events)
    @staticmethod
    def keydown(key):
        for event in EventManager.events:
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False
    
    @staticmethod
    def clicked(leftright = 1) -> bool: # 1 - left click, 3 - right click
        for event in EventManager.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == leftright: # left click
                    return True
        return False
    
    def clicked_any() -> bool:
        for event in EventManager.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False