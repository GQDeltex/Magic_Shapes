import pygame
import constants

class SpriteSheet():
    sprite_sheet = None
    
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.COLORKEY)
        return image
    
class TextToScreen(object):
    def __init__(self, msg, color, y_displace, font, screen):
        self.textSurf, self.textRect = self.text_objects(msg, color, font)
        self.textRect.center = (constants.SCREEN_WIDTH/2), (constants.SCREEN_HEIGHT/2) + y_displace
        screen.blit(self.textSurf, self.textRect)

    def text_objects(self, text, color, size):
        textSurface = size.render(text, True, color)
        return textSurface, textSurface.get_rect()  

class Mystery_tools(object):
    def __init__(self, x, y):
            self.rect = pygame.Rect((x*32), (y*32), 32, 32)
            self.rect.x = (x*32)
            self.rect.y = (y*32)