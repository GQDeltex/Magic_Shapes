import pygame

class TileType(object):
    def __init__(self, name, start_x, start_y, width, height):
        self.name = name
        self.rect = pygame.Rect(start_x, start_y, width, height)        