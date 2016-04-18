import pygame
import constants
import platforms
import Tilemap

class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
    level_start_x = 32
    level_start_y = 544    
    def __init__(self, player, level, menu):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = list()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.map = Tilemap.Tilemap(self.platform_list, level, menu)
        self.mystery_list = self.map.mystery_list
        self.finish_list = self.map.finish_list
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(constants.BLUE)
 
        # Draw all the sprite lists that we have
        self.map.render(screen)
        self.enemy_list.draw(screen)