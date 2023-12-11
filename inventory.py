from globals import *
from items import *
from eventmanager import EventManager

class Inventory:
    def __init__(self, app, textures) -> None:
        self.app = app
        self.screen = app.screen
        self.textures = textures

        # create inventory slots 
        self.slots = []
        for index in range(10):
            self.slots.append(Item())
        self.slots[0] = SwordItem('sword', 1)
        self.slots[1] = ToolItem('pickaxe', 1)
        self.slots[2] = BlockItem('grass', 5)
        self.slots[3] = BlockItem('dirt', 3)
        self.slots[4] = BlockItem('gold', 5)
        self.slots[5] = BlockItem('wood_log', 5)
        self.slots[6] = BlockItem('stone', 5)

        self.active_slot = 0
        self.current_item = None

        # fonts
        self.font = pygame.font.Font(None, 30)
    def use(self, player, position):
        if self.slots[self.active_slot].name != "default":
            self.slots[self.active_slot].use(player, position)
    def add_item(self, item):
        first_available_slot = len(self.slots) # first empty slot
        target_slot = len(self.slots) # first slot of same name
        for index, slot in enumerate(self.slots):
            if slot.name == "default" and index < first_available_slot:
                first_available_slot = index
            if slot.name == item.name:
                target_slot = index
        if target_slot < len(self.slots):
            self.slots[target_slot].quantity += items[item.name].quantity   
        elif first_available_slot < len(self.slots):
            self.slots[first_available_slot] = items[item.name].item_type(item.name, items[item.name].quantity)
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    self.active_slot = 0
                if event.key == pygame.K_2: 
                    self.active_slot = 1
                if event.key == pygame.K_3: 
                    self.active_slot = 2
                if event.key == pygame.K_4: 
                    self.active_slot = 3
                if event.key == pygame.K_5: 
                    self.active_slot = 4
                if event.key == pygame.K_6: 
                    self.active_slot = 5
                if event.key == pygame.K_7: 
                    self.active_slot = 6
                if event.key == pygame.K_8: 
                    self.active_slot = 7
                if event.key == pygame.K_9: 
                    self.active_slot = 8
                if event.key == pygame.K_0: 
                    self.active_slot = 9

            self.current_item = self.slots[self.active_slot]
    def update(self):
        self.handle_events(EventManager.events)
    def draw(self):
        pygame.draw.rect(self.screen, "gray", pygame.Rect(0, 0, (TILESIZE *2)*len(self.slots), TILESIZE*2))

        x_offset = TILESIZE / 2
        y_offset = TILESIZE / 2

        for i in range(len(self.slots)):
            if i == self.active_slot:
                pygame.draw.rect(self.screen, "white", pygame.Rect(i*(TILESIZE*2), 0, TILESIZE*2, TILESIZE*2))
            pygame.draw.rect(self.screen, "black", pygame.Rect(i*(TILESIZE*2), 0, TILESIZE*2, TILESIZE*2), 2)
            if self.slots[i].name != "default":
                self.screen.blit(self.textures[self.slots[i].name], (x_offset + (TILESIZE*2)*i, y_offset))

                self.amount_text = self.font.render(str(self.slots[i].quantity), True, "black")
                self.screen.blit(self.amount_text, ((TILESIZE*2)*i + 3, 3))
        pygame.draw.rect(self.screen, "black", pygame.Rect(0, 0, (TILESIZE *2)*len(self.slots), TILESIZE*2), 4)

