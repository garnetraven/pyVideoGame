import pygame
from inventory import Inventory
from camera import Camera
from playerstats import PlayerStats
from states.scenestates.scenestate import SceneState
from player import Player
from texturedata import solo_texture_data, atlas_texture_data
from globals import *

class GamePlaySceneState(SceneState):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.game.event_manager.register_listener(self)

        # textures
        self.textures = self.gen_solo_textures()
        atlas_textures = self.gen_atlas_textures('assets/atlas.png')
        if atlas_textures is not None:
            self.textures.update(atlas_textures)

        # sprite groups
        self.blocks = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.group_list: dict[str, pygame.sprite.Group] = {
            'block_group':self.blocks,
            'enemy_group':self.enemy_group
        }

        # inventory
        self.inventory = Inventory(self.game, self.textures)

        # camera
        self.sprites = Camera()
        self.group_list['sprites'] = self.sprites
        
        if self.game.player is None:
            self.game.player = Player([self.sprites], self.textures['player_static'], (600, 300),
                                      parameters={
                                          'group_list': self.group_list,
                                          'textures': self.textures,
                                          'inventory': self.inventory,
                                          'health': 100
                                      })
        self.player = self.game.player

        self.player_stats = PlayerStats(self.game, self.player)


    def gen_solo_textures(self) -> dict:
        textures = {}

        for name, data in solo_texture_data.items():
            textures[name] = pygame.transform.scale(pygame.image.load(data['file_path']).convert_alpha(), (data['size']))

        return textures
    
    def gen_atlas_textures(self, filepath):
        textures = {}
        atlas_img = pygame.transform.scale(pygame.image.load(filepath).convert_alpha(), (TILESIZE*16, TILESIZE*16))

        for name, data in atlas_texture_data.items():
            textures[name] = pygame.Surface.subsurface(atlas_img, pygame.Rect(data['position'][0]*TILESIZE, 
                                                                              data['position'][1]*TILESIZE,
                                                                              data['size'][0], 
                                                                              data['size'][1]))
        
        return textures
    
    def enter(self):
        pass
    def exit(self):
        pass
    def update(self):
        pass
    def handle_events(self, events):
        pass
    def draw(self):
        pass
    def render(self, screen):
        pass