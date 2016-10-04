import pygame
import constants
import levels
import sys
import menus
import Utils
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

    if constants.MULTIPLAYER:
        if constants.SERVER:
            server = Utils.Server()
            pygame.display.set_caption("Magic_Shapes - Server")
        else:
            server = Utils.Client()
            pygame.display.set_caption("Magic_Shapes - Client")
    else:
        pygame.display.set_caption("Magic_Shapes - Singleplayer")
        server = None

    locmake = Utils.locmake()
    menu = menus.Menus(screen)

    player01 = Player(32, 544)
    player02 = Player(32, 544)

    # Set the current level
    current_level_no = 1
    player01.level_no = current_level_no
    player02.level_no = current_level_no
    max_level = 18
    current_level = levels.Level(player01, current_level_no, menu)
    player01.level = current_level
    player02.level = current_level
    player01.rect.x = current_level.level_start_x
    player02.rect.x = current_level.level_start_x
    player01.rect.y = current_level.level_start_y
    player02.rect.y = current_level.level_start_y
    player01.level_up()
    player02.level_up()

    active_sprite_list = pygame.sprite.Group()

    active_sprite_list.add(player01)
    active_sprite_list.add(player02)
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
                    player01.go_left()
                if event.key == pygame.K_RIGHT:
                    player01.go_right()
                if event.key == pygame.K_UP:
                    player01.jump()
                if event.key == pygame.K_ESCAPE:
                    menu.Pause_Menu()
                if event.key == pygame.K_F5:
                    mystget = False
                    current_level = levels.Level(player01, current_level_no, menu)
                    player01.rect.x = current_level.level_start_x
                    player02.rect.x = current_level.level_start_x
                    player01.rect.y = current_level.level_start_y
                    player02.rect.y = current_level.level_start_y
                    player01.level = current_level
                    player02.level = current_level

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player01.change_x < 0:
                    player01.stop()
                if event.key == pygame.K_RIGHT and player01.change_x > 0:
                    player01.stop()

        if pygame.sprite.spritecollide(player01, current_level.mystery_list, False) and mystget == False:
            mystget = True
            if not player01.character_level + 1 > player01.maxlevel:
                player01.direction = "M"
                player01.magic_sound.set_volume(constants.effect_volume)
                player01.magic_sound.play()
                player01.level_up()
            else:
                player01.direction = "M"
                player01.magic_sound.set_volume(constants.effect_volume)
                player01.magic_sound.play()
                player01.level_reset()

        if pygame.sprite.spritecollide(player01, current_level.danger_list, False):
            uhh_sound.set_volume(constants.effect_volume)
            uhh_sound.play()
            player01.lifes -=1
            if player01.lifes <= 0:
                player01.lifes = 3
                menu.Game_Over("Game Over!", "You hurt yourself too often")
                mystget = False
                current_level_no = 1
                player01.level_no = current_level_no
                current_level = levels.Level(player01, current_level_no, menu)
                player01.rect.x = current_level.level_start_x
                player01.rect.y = current_level.level_start_y
                player01.level = current_level
            else:
                current_level = levels.Level(player01, current_level_no, menu)
                player01.rect.x = current_level.level_start_x
                player01.rect.y = current_level.level_start_y
                player01.level = current_level
                menu.Level_screen(current_level_no, player01.lifes)

        if pygame.sprite.spritecollide(player01, current_level.finish_list, False) and mystget == True:
            current_level_no += 1
            player01.level_no = current_level_no
            mystget = False
            current_level = levels.Level(player01, current_level_no, menu)
            player01.rect.x = current_level.level_start_x
            player01.rect.y = current_level.level_start_y
            player01.level = current_level
            if current_level_no == max_level:
                player01.lifes = 100
                menu.Level_screen(current_level_no, player01.lifes)
            else:
                menu.Level_screen(current_level_no, player01.lifes)

        if constants.MULTIPLAYER:
            if constants.SERVER:
                server.sendData((player01.rect.x, player01.rect.y, player01.direction, player01.character_level, player01.level_no))
                back = server.getData()
                player02.rect.x, player02.rect.y, player02.direction, player02.character_level, player02.level_no = locmake.getLocation(back)
                player02.level_update()
            else:
                back = server.getData()
                player02.rect.x, player02.rect.y, player02.direction, player02.character_level, player02.level_no = locmake.getLocation(back)
                server.sendData((player01.rect.x, player01.rect.y, player01.direction, player01.character_level, player01.level_no))
                player02.level_update()
            if player01.level_no == player02.level_no:
                if not active_sprite_list.has(player02):
                    active_sprite_list.add(player02)
            else:
                if active_sprite_list.has(player02):
                    active_sprite_list.remove(player02)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        active_sprite_list.update()
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
