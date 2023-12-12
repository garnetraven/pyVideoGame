from globals import *

atlas_texture_data = {
    'dirt':{'type':'block', 'size':(TILESIZE, TILESIZE), 'position': (0, 0)},
    'grass':{'type':'block', 'size':(TILESIZE, TILESIZE), 'position': (1, 0)},
    'stone':{'type':'block', 'size':(TILESIZE, TILESIZE), 'position': (2, 0)},
    'wood_log':{'type':'block', 'size':(TILESIZE, TILESIZE), 'position': (3, 0)},
    'gold':{'type':'block', 'size':(TILESIZE, TILESIZE), 'position': (4, 0)},
    'silver':{'type':'block', 'size':(TILESIZE, TILESIZE), 'position': (5, 0)}
}
player_texture_data = {
    'player_static':{'type':'player', 'file_path':'assets/player.png', 'size':(TILESIZE*2, TILESIZE*3)},
}
solo_texture_data = {
    'player_static':{'type':'player', 'file_path':'assets/player.png', 'size':(TILESIZE*2, TILESIZE*3)},
    'zombie_static':{'type':'enemy', 'file_path':'assets/zombie.png', 'size':(TILESIZE*2, TILESIZE*3)},
    'skeleton_static':{'type':'enemy', 'file_path':'assets/skeleton.png', 'size':(TILESIZE*2, TILESIZE*3)},
    'sword':{'type':'weapon', 'file_path':'assets/sword.png', 'size':(TILESIZE, TILESIZE)},
    'pickaxe':{'type':'tool', 'file_path':'assets/pickaxe.png', 'size':(TILESIZE, TILESIZE)},
    'health_potion':{'type':'potion', 'file_path':'assets/health_potion.png', 'size':(TILESIZE, TILESIZE)}
}