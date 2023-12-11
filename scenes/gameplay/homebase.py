import pygame
from globals import *
from sprite import Entity, Mob
from states.scenestates.gameplayscenestates.gameplayscenestate import GamePlaySceneState
from texturedata import solo_texture_data, atlas_texture_data
from eventmanager import EventManager
from pausemenustate import PauseMenu

class HomeBase(GamePlaySceneState):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.game = game
        self.sprites.add(self.game.player)

         # textures
        self.textures = self.gen_solo_textures()
        self.textures.update(self.gen_atlas_textures('assets/atlas.png'))

        Mob([self.sprites, self.enemy_group], self.textures['zombie_static'], (800, -500), parameters={
                                                                                            'block_group':self.blocks,
                                                                                            'player':self.player,
                                                                                            'damage': 5,
                                                                                            'health': 2
                                                                                            })
        self.gen_world()

    def enter(self):
        # Add the player to the sprites group
        self.player.set_block_group(self.blocks)
        self.player.set_enemy_group(self.enemy_group)
    
    def exit(self):
        pass

    def gen_solo_textures(self) -> dict:
        return super().gen_solo_textures()

    def gen_atlas_textures(self, filepath):
        return super().gen_atlas_textures(filepath)
    
    def gen_world(self):
        heightmap = []
        for y in range(40):
            height = 5
            heightmap.append(height)
        for x in range(len(heightmap)):
            for y in range(heightmap[x]):
                y_offset = 5-y + 6
                Entity([self.sprites, self.blocks], self.textures['dirt'], (x*TILESIZE,y_offset*TILESIZE), name='dirt')
    def handle_events(self, events):
        self.player.handle_events(events)
        self.inventory.handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.game_state_stack.push(PauseMenu)
                    return True
            return False
        
    def draw(self):
        super().draw()
                
    def update(self):
        self.handle_events(EventManager.events)
        self.sprites.update()
        self.inventory.update()
        self.player_stats.update()
    def render(self, screen):
        self.game.screen.fill('lightblue')
        self.inventory.draw()
        self.player_stats.draw()
        self.sprites.draw(self.player, self.game.screen)
