import pygame
import constants
import levels
import sys
import menus
from player import Player
 
def main():
    """ Main Program """
    pygame.init()    
 
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    if constants.ISFULLSCREEN == True:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)
    
    menu = menus.Menus(screen)
 
    pygame.display.set_caption("Magic_Shapes")
    
    player = Player(32, 544)
 
    # Set the current level
    current_level_no = 1
    current_level = levels.Level(player, current_level_no, menu)
    player.level = current_level
    player.rect.x = current_level.level_start_x
    player.rect.y = current_level.level_start_y
    player.level_up()
 
    active_sprite_list = pygame.sprite.Group()
    
    active_sprite_list.add(player)
    # Loop until the user clicks the close button.
    done = False
    
    mystget = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    if constants.ISINTRO == True:
        menu.intro()
    
    bg_music_01 = pygame.mixer.music.load("Game-Files/Sounds/rock_and_roll.wav")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(constants.music_volume)
    
    uhh_sound = pygame.mixer.Sound("Game-Files/Sounds/Uhh.wav")
    uhh_sound.set_volume(constants.effect_volume)
    
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_ESCAPE:
                    menu.Pause_Menu()
                if event.key == pygame.K_F5:
                    mystget = False
                    current_level = levels.Level(player, current_level_no, menu)
                    player.rect.x = current_level.level_start_x
                    player.rect.y = current_level.level_start_y
                    player.level = current_level
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
        
        if pygame.sprite.spritecollide(player, current_level.mystery_list, False) and mystget == False:
            mystget = True
            if not player.character_level + 1 > player.maxlevel:
                player.direction = "M"
                player.magic_sound.set_volume(constants.effect_volume)
                player.magic_sound.play()
                player.level_up()
            else:
                player.direction = "M"
                player.magic_sound.set_volume(constants.effect_volume)
                player.magic_sound.play()
                player.level_reset()

        if pygame.sprite.spritecollide(player, current_level.danger_list, False):
            uhh_sound.set_volume(constants.effect_volume)
            uhh_sound.play()
            player.lifes -=1
            if player.lifes <= 0:
                player.lifes = 3
                menu.Game_Over("Game Over!", "You hurt yourself too often")
                mystget = False
                current_level_no = 1
                current_level = levels.Level(player, current_level_no, menu)
                player.rect.x = current_level.level_start_x
                player.rect.y = current_level.level_start_y
                player.level = current_level
            else:
                current_level = levels.Level(player, current_level_no, menu)
                player.rect.x = current_level.level_start_x
                player.rect.y = current_level.level_start_y
                player.level = current_level
                menu.Level_screen(current_level_no, player.lifes)
                    
        if pygame.sprite.spritecollide(player, current_level.finish_list, False) and mystget == True:
            current_level_no += 1
            mystget = False
            current_level = levels.Level(player, current_level_no, menu)
            player.rect.x = current_level.level_start_x
            player.rect.y = current_level.level_start_y
            player.level = current_level
            if current_level_no == 17:
                player.lifes = 100
                menu.Level_screen("Final Round", player.lifes)
            else:
                menu.Level_screen(current_level_no, player.lifes)
 
        # Update the player.
        active_sprite_list.update()
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.quit()
    sys.exit()
 
if __name__ == "__main__":
    main()
    sys.exit()
