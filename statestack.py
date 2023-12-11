class StateStack:
    def __init__(self, game) -> None:
        self.game = game
        self.states = []
    def push(self, state_class):
        new_state = state_class(self.game)
        new_state.enter()
        self.states.append(new_state)
    def pop(self):
        self.states[-1].exit()
        return self.states.pop()
    def change_state(self, new_state):
        # Pop the current state (if any)
        if self.states:
            self.states.pop()
        # Push the new state onto the stack
        self.push(new_state)
    def handle_events(self, events):
        if self.states:
            self.states[-1].handle_events(events)
    def update(self):
        if self.states:
            self.states[-1].update()
    def draw(self, screen):
        if self.states:
            self.states[-1].render(screen)