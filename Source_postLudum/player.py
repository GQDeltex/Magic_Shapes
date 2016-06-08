import pygame
import constants
import Animation
from Utils import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
    
    change_x = 0
    change_y = 0
    
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_m_1 = []
    
    direction = "R"
    
    level = None    

    # -- Methods
    def __init__(self, x, y):
        """ Constructor function """
        self.character_level = 0
        self.maxlevel = 13
        self.lifes = 3
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.sprite_sheet = SpriteSheet("Game-Files/Images/texturepack.png")
        
        #Magic Level 1
        image = self.sprite_sheet.getImage(0, 256, 32, 32)
        self.walking_frames_m_1.append(image)
        image = self.sprite_sheet.getImage(32, 256, 32, 32)
        self.walking_frames_m_1.append(image)
        
        self.image = self.walking_frames_m_1[0]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = "R"
        self.anim = Animation.Animation(10)
        self.animmyst = Animation.Animation(5)
        self.time = 0
        self.current = 0
        
        self.jump_sound = pygame.mixer.Sound("Game-Files/Sounds/Jump.wav")
        self.jump_sound.set_volume(constants.effect_volume)
        self.magic_sound = pygame.mixer.Sound("Game-Files/Sounds/Magic.wav")
        self.magic_sound.set_volume(constants.effect_volume)
    
    def level_up(self):
        self.character_level += 1
        self.walking_frames_r = []
        self.walking_frames_l = []
        image = self.sprite_sheet.getImage(((self.character_level - 1) * 32), 0, 32, 32)
        self.walking_frames_r.append(image)
        image = self.sprite_sheet.getImage(((self.character_level - 1) * 32), 0, 32, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
    
    def level_reset(self):
        self.character_level = 1
        self.walking_frames_r = []
        self.walking_frames_l = []
        image = self.sprite_sheet.getImage(((self.character_level - 1) * 32), 0, 32, 32)
        self.walking_frames_r.append(image)
        image = self.sprite_sheet.getImage(((self.character_level - 1) * 32), 0, 32, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)        
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
        if self.direction == "R":
            self.image = self.anim.update(self.walking_frames_r)
        elif self.direction == "M":
            self.image = self.animmyst.update(self.walking_frames_m_1)
        else:
            self.image = self.anim.update(self.walking_frames_l)            
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.jump_sound.set_volume(constants.effect_volume)
        self.jump_sound.play()
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
