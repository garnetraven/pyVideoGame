import pygame
from globals import *
from states.scenestates.gameplayscenestates.gameplayscenestate import GamePlaySceneState
from sprite import Entity, Mob
from texturedata import solo_texture_data, atlas_texture_data
from opensimplex import OpenSimplex
from eventmanager import EventManager
from scenes.gameplay.pausemenustate import PauseMenu

class TestScene(GamePlaySceneState):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.game = game

        Mob([self.sprites, self.enemy_group], self.textures['zombie_static'], (800, -500), parameters={
                                                                                            'block_group':self.blocks,
                                                                                            'player':self.player,
                                                                                            'damage': 5,
                                                                                            'health': 2
                                                                                            })
        Mob([self.sprites, self.enemy_group], self.textures['skeleton_static'], (900, -500), parameters={
                                                                                            'block_group':self.blocks,
                                                                                            'player':self.player,
                                                                                            'damage': 5,
                                                                                            'health': 2
                                                                                            })
        
        self.gen_world()

    def enter(self):
        super().enter()
        # Add the player to the sprites group
    
    def exit(self):
        pass

    def gen_solo_textures(self) -> dict:
        return super().gen_solo_textures()

    def gen_atlas_textures(self, filepath):
        return super().gen_atlas_textures(filepath)
    
    def gen_world(self):
        noise_generator = OpenSimplex(seed=17383726)

        heightmap = []
        for y in range(100):
            noise_value = noise_generator.noise2(y * 0.05, 0)
            height = int((noise_value + 1) * 4 + 6)
            heightmap.append(height)

        for x in range(len(heightmap)):
            for y in range(heightmap[x]):
                y_offset = 5-y + 6
                block_type = 'dirt'
                if y == heightmap[x] - 1:
                    block_type = 'grass'
                if y < heightmap[x] - 5:
                    block_type = 'stone'
                Entity([self.sprites, self.blocks], self.textures[block_type], (x*TILESIZE,y_offset*TILESIZE), name=block_type)
    
    def handle_events(self, events):
        self.player.handle_events(events)
        self.inventory.handle_events(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state_stack.push(PauseMenu)
                    return True
            return False
        
    def update(self):
        self.handle_events(EventManager.events)
        self.sprites.update()
        self.inventory.update()
        self.player_stats.update()

    def draw(self):
        super().draw()

    def render(self, screen):
        self.game.screen.fill('lightblue')
        self.inventory.draw()
        self.player_stats.draw()
        self.sprites.draw(self.player, self.game.screen)