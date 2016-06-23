import pygame
import Tileset
import wall_tools
from Utils import Mystery_tools
import levels
import os

class Tilemap(object):
    def __init__(self, walls, level, menu):
        self.tiles = list()
        self.tiles = []
        self.mystery_list = list()
        self.finish_list = list()
        self.danger_list = list()
        
        l = [0]
        
        map_dest = "Game-Files/Maps/"
        
        self.tileset = Tileset.Tileset("Game-Files/Images/texturepack.png", 32, 32)
        self.tileset.add_tile("grass", 0, 32)
        self.tileset.add_tile("air", 0, 64)
        self.tileset.add_tile("stone", 0, 160)
        self.tileset.add_tile("dirt", 0, 96)
        self.tileset.add_tile("dirt-grass", 0, 128)
        self.tileset.add_tile("finish", 0, 192)
        self.tileset.add_tile("mystery", 0, 224)
        self.tileset.add_tile("spikes", 0, 288)
        
        self.width = 24
        self.height = 19
        
        if os.path.isfile(os.path.join(map_dest, str(level)+".txt")):
            l = []
            l = [line.strip() for line in open(os.path.join(map_dest, str(level)+".txt")).readlines()]
            self.height = len(l)
            self.width = len(l[0])
        else:
            menu.Game_Over(caption = "Finished!", addinfo = "You Finished the Game, Congratulations!")

        for i in range(0, len(l)):
            self.tiles.append(list())
            for j in range(0, len(l[0])):
                try:
                    r = l[i][j]
                except:
                    r = None
                if r == 'g':
                    wall = wall_tools.Wall_tiles(j, i)
                    walls.append(wall)                      
                    self.tiles[i].append("grass")
                elif r == 's':
                    wall = wall_tools.Wall_tiles(j, i)
                    walls.append(wall)
                    self.tiles[i].append("stone")
                elif r == 'd':
                    wall = wall_tools.Wall_tiles(j, i)
                    walls.append(wall)
                    self.tiles[i].append("dirt")
                elif r == 'm':
                    wall = wall_tools.Wall_tiles(j, i)
                    walls.append(wall)
                    self.tiles[i].append("dirt-grass")
                elif r == 'u':
                    myst = Mystery_tools(j, i)
                    self.mystery_list.append(myst)
                    self.tiles[i].append("mystery")
                elif r == 'z':
                    finito = Mystery_tools(j, i)
                    self.finish_list.append(finito)                    
                    self.tiles[i].append("finish")
                elif r == 'p':
                    levels.Level.level_start_x = (j * 32)
                    levels.Level.level_start_y = (i * 32)
                    self.tiles[i].append("air")
                elif r == 'f':
					danger = Mystery_tools(j, i)
					self.danger_list.append(danger)
					self.tiles[i].append("spikes")
                else:
                    self.tiles[i].append("air")
       
    def render(self, screen):
        for y in range(0, int(screen.get_height() / self.tileset.tile_height) +1):
            if y >= self.height or y < 0:
                continue
            line = self.tiles[y]
            for x in range(0, int(screen.get_width() / self.tileset.tile_width) +1):
                if x >= self.width or x < 0:
                    continue
                tilename = line[x]
                tile = self.tileset.get_tile(tilename)
                if tile is not None:
                    screen.blit(self.tileset.image, (x * self.tileset.tile_width, y * self.tileset.tile_height), tile.rect)
