import pygame
from globals import * 
from eventmanager import EventManager
import math
import items

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface((TILESIZE*2, TILESIZE*3)), position: tuple, parameters: dict) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

        # parameters
        self.group_list, self.textures, self.block_group, self.inventory, self.enemy_group, self.health = (
            parameters['group_list'], 
            parameters['textures'], 
            parameters['group_list']['block_group'],
            parameters['inventory'], 
            parameters['group_list']['enemy_group'], 
            parameters['health']
        )

        self.velocity = pygame.math.Vector2()
        self.mass = 5
        self.terminal_velocity = self.mass * TERMINALVELOCITY

        # is grounded?
        self.grounded = True
    def handle_events(self, events):
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.block_handling(event)
                if event.button == 1:
                    self.attack()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.velocity.x = -1
                if event.key == pygame.K_d:
                    self.velocity.x = 1
                if not keys[pygame.K_a] and not keys[pygame.K_d]:
                    if self.velocity.x > 0:
                        self.velocity.x -= 0.1
                    elif self.velocity.x < 0:
                        self.velocity.x += 0.1
                        if abs(self.velocity.x) < 0.3:
                            self.velocity.x = 0
                if event.key == pygame.K_SPACE and self.grounded:
                    self.velocity.y = -PLAYERJUMPPOWER
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and not keys[pygame.K_d]:
                    self.velocity.x = 0
                elif event.key == pygame.K_d and not keys[pygame.K_a]:
                    self.velocity.x = 0
                elif event.key == pygame.K_a and keys[pygame.K_d]:
                    self.velocity.x = 1
                elif event.key == pygame.K_d and keys[pygame.K_a]:
                    self.velocity.x = -1

        if EventManager.clicked(1):
            for enemy in self.enemy_group:
                print('left click')
                distance = abs(math.sqrt((self.rect.x - enemy.rect.x)**2 + (self.rect.y - enemy.rect.y)**2))
                if enemy.rect.collidepoint(self.get_adjusted_mouse_position()) and (distance < TILESIZE*3):
                    current_item_name = self.inventory.slots[self.inventory.active_slot].name
                    if current_item_name in items.items and items.items[current_item_name].use_type == 'weapon':
                        self.inventory.slots[self.inventory.active_slot].attack(self, enemy)
    def attack(self):
        for enemy in self.enemy_group:
                        distance = abs(math.sqrt((self.rect.x - enemy.rect.x)**2 + (self.rect.y - enemy.rect.y)**2))
                        if enemy.rect.collidepoint(self.get_adjusted_mouse_position()) and (distance < TILESIZE*3):
                            current_item_name = self.inventory.slots[self.inventory.active_slot].name
                            if current_item_name in items.items and items.items[current_item_name].use_type == 'weapon':
                                self.inventory.slots[self.inventory.active_slot].attack(self, enemy)
    def move(self):
        self.velocity.y += GRAVITY * self.mass
        # terminal velocity check
        if self.velocity.y > self.terminal_velocity:
            self.velocity.y = self.terminal_velocity

        self.rect.x += self.velocity.x  * PLAYERSPEED # applying horizontal velocity
        self.check_collisions("horizonal")
        self.rect.y += self.velocity.y # applying vertical velocity
        self.check_collisions("vertical")
    def check_collisions(self, direction):
        if direction == "horizonal":
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x > 0: # moving right
                        self.rect.right = block.rect.left
                    if self.velocity.x < 0: # moving left
                        self.rect.left = block.rect.right
        elif direction == "vertical":
            collisions = 0
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.y > 0: # moving down
                        collisions += 1
                        self.grounded = True
                        self.rect.bottom = block.rect.top
                    if self.velocity.y < 0: # moving up
                        self.rect.top = block.rect.bottom
            if collisions > 0:
                self.grounded = True
            else:
                self.grounded = False

    def block_handling(self, event):
        placed = False
        collision = False
        mouse_pos = self.get_adjusted_mouse_position()

        for block in self.block_group:
            if block.rect.collidepoint(mouse_pos):
                collision = True
                current_item_name = self.inventory.slots[self.inventory.active_slot].name
                if current_item_name in items.items:
                    current_item_use_type = items.items[current_item_name].use_type
                else:
                    current_item_use_type = None                 
                if current_item_use_type == "tool" and pygame.mouse.get_pressed()[0]: # breaking the block
                    self.inventory.add_item(block)
                    block.kill()
            if pygame.mouse.get_pressed()[0]:
                if not collision:
                    placed = True
        if placed and not collision:
            self.inventory.use(self, self.get_block_pos(mouse_pos))

    def get_adjusted_mouse_position(self) -> tuple:
        mouse_pos = pygame.mouse.get_pos()

        player_offset = pygame.math.Vector2()
        player_offset.x = SCREEN_WIDTH / 2 - self.rect.centerx
        player_offset.y = SCREEN_HEIGHT / 1.6 - self.rect.centery

        return (mouse_pos[0] - player_offset.x, mouse_pos[1] - player_offset.y)
    def get_block_pos(self, mouse_pos: tuple):
        return (int((mouse_pos[0]//TILESIZE)*TILESIZE), int((mouse_pos[1]//TILESIZE)*TILESIZE))
    def update(self):
        self.handle_events(EventManager.events)
        self.move()
        self.block_handling(EventManager.events)

        if self.health <= 0:
            self.kill()