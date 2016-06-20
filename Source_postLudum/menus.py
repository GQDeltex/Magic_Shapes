import pygame
import constants
import os
import sys
from Utils import TextToScreen
from time import sleep
from Magic_Shapes import main

class Menus (object):
    def __init__(self, screen):
        if os.name == 'nt':
            self.default_font = "Comic Sans MS"
        else:
            self.default_font = "Ubuntu"
        self.smallfont = pygame.font.SysFont(self.default_font, 25)
        self.mediumfont = pygame.font.SysFont(self.default_font, 40)
        self.bigfont = pygame.font.SysFont(self.default_font, 55)
        self.wrong_sound = pygame.mixer.Sound("Game-Files/Sounds/wrong.wav")
        self.wrong_sound.set_volume(constants.effect_volume)
        self.screen = screen

    def Game_Over(self, caption = "Game Over!", addinfo = ""):
        gameOver = True
        is_selected = False
        selected = 1
        while gameOver:
            self.wrong_sound.set_volume(constants.effect_volume)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if not selected - 1 == 0:
                            selected -= 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_DOWN:
                        if not selected + 1 == 3:
                            selected += 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_RETURN:
                        if mainmenu_select == True:
                            constants.ISINTRO = True
                            gameOver = False
                            main()
                        if retry_select == True:
                            constants.ISINTRO = False
                            gameOver = False
            if selected == 1:
                retry_button = constants.RED
                retry_select = True
            else:
                retry_button = constants.BLACK
                retry_select = False
            if selected == 2:
                mainmenu_button = constants.RED
                mainmenu_select = True
            else:
                mainmenu_button = constants.BLACK
                mainmenu_select = False
            self.screen.fill(constants.WHITE)
            TextToScreen(caption, constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Retry", retry_button, 10, self.mediumfont, self.screen)
            TextToScreen("Main Menu", mainmenu_button, 50, self.mediumfont, self.screen)
            TextToScreen(addinfo, constants.GREEN, -30, self.mediumfont, self.screen)
            pygame.display.flip()

    def Level_screen(self, level, remain_lifes):
        self.screen.fill(constants.WHITE)
        TextToScreen(("Level:" + str(level)), constants.GREEN, -150, self.bigfont, self.screen)
        TextToScreen(("Remaining Lifes:" + str(remain_lifes)), constants.BLACK, -30, self.mediumfont, self.screen)
        pygame.display.flip()
        sleep(2)

    def credits(self):
        credits = True
        while credits:
            self.wrong_sound.set_volume(constants.effect_volume)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        credits = False
            self.screen.fill(constants.WHITE)
            TextToScreen("Credits", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Code: Peter, Marcel", constants.BLACK, -30, self.smallfont, self.screen)
            TextToScreen("Art: Malin, Madita, Peter", constants.BLACK, 10, self.smallfont, self.screen)
            TextToScreen("Sound & Music: Malin, Madita", constants.BLACK, 50, self.smallfont, self.screen)
            TextToScreen("Maps: Marcel, Malin, Madita", constants.BLACK, 90, self.smallfont, self.screen)
            TextToScreen("Made for Ludum Dare 35", constants.BLACK, 150, self.smallfont, self.screen)
            TextToScreen("Report Bugs at: gqdeltex@gmail.com", constants.BLUE, 190, self.smallfont, self.screen)
            TextToScreen("Return to get back to the Main Menu", constants.RED, 230, self.smallfont, self.screen)
            pygame.display.flip()

    def Help(self):
        credits = True
        while credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    credits = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        credits = False
            self.screen.fill(constants.WHITE)
            TextToScreen("How to play", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Grab the blue boxes to shapeshift", constants.BLACK, -30, self.mediumfont, self.screen)
            TextToScreen("Jump to the End of the Level", constants.BLACK, 10, self.mediumfont, self.screen)
            TextToScreen("to get to the next Level!", constants.BLACK, 50, self.mediumfont, self.screen)
            TextToScreen("Return to get back to the Main Menu", constants.RED, 180, self.smallfont, self.screen)
            pygame.display.flip()

    def Option_Menu(self):
        options = True
        selectable = 4
        selected = 1
        while options:
            self.wrong_sound.set_volume(constants.effect_volume)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if not selected - 1 == 0:
                            selected -= 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_DOWN:
                        if not selected + 1 == (selectable + 1):
                            selected += 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_RIGHT:
                        if volume_select == True:
                            if (constants.music_volume + 0.1) <= 1.0:
                                constants.music_volume += 0.1
                                pygame.mixer.music.set_volume(constants.music_volume)
                            else:
                                self.wrong_sound.play()
                        if effect_select == True:
                            if (constants.effect_volume + 0.1) <= 1.0:
                                constants.effect_volume += 0.1
                            else:
                                self.wrong_sound.play()
                        if fullscreen_select == True:
                            if constants.ISFULLSCREEN == False:
                                constants.ISFULLSCREEN = True
                                size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
                                screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                            else:
                                constants.ISFULLSCREEN = False
                                size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
                                screen = pygame.display.set_mode(size)
                    if event.key == pygame.K_LEFT:
                        if volume_select == True:
                            if (constants.music_volume - 0.1) >= 0.0:
                                constants.music_volume -= 0.1
                                pygame.mixer.music.set_volume(constants.music_volume)
                            else:
                                self.wrong_sound.play()
                        if effect_select == True:
                            if (constants.effect_volume - 0.1) >= 0.0:
                                constants.effect_volume -= 0.1
                            else:
                                self.wrong_sound.play()
                        if fullscreen_select == True:
                            if constants.ISFULLSCREEN == False:
                                constants.ISFULLSCREEN = True
                                size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
                                screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                            else:
                                constants.ISFULLSCREEN = False
                                constants.SCREEN_WIDTH = 800
                                constants.SCREEN_HEIGHT = 600
                                size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
                                screen = pygame.display.set_mode(size)
                    if event.key == pygame.K_RETURN:
                        if  back_select == True:
                            options = False
            if selected == 1:
                volume_button = constants.RED
                volume_select = True
            else:
                volume_button = constants.BLACK
                volume_select = False
            if selected == 4:
                back_button = constants.RED
                back_select = True
            else:
                back_button = constants.BLACK
                back_select = False
            if selected == 2:
                effect_button = constants.RED
                effect_select = True
            else:
                effect_button = constants.BLACK
                effect_select = False
            if selected == 3:
                fullscreen_button = constants.RED
                fullscreen_select = True
            else:
                fullscreen_button = constants.BLACK
                fullscreen_select = False
            self.screen.fill(constants.WHITE)
            TextToScreen("Options", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Music Volume: " + (str(int(constants.music_volume * 100)) + "%"), volume_button, 10, self.mediumfont, self.screen)
            TextToScreen("Effect Volume: " + (str(int(constants.effect_volume * 100)) + "%"), effect_button, 50, self.mediumfont, self.screen)
            TextToScreen("Fullscreen: " + str(constants.ISFULLSCREEN), fullscreen_button, 90, self.mediumfont, self.screen)
            TextToScreen("Back", back_button, 130, self.mediumfont, self.screen)
            pygame.display.flip()

    def Pause_Menu(self):
        pause = True
        selected = 1
        while pause:
            self.wrong_sound.set_volume(constants.effect_volume)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if not selected - 1 == 0:
                            selected -= 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_DOWN:
                        if not selected + 1 == 5:
                            selected += 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_RETURN:
                        if resume_select == True:
                            constants.ISINTRO = False
                            pause = False
                        elif retry_select == True:
                            constants.ISINTRO = False
                            pause = False
                            main()
                        elif option_select == True:
                            self.Option_Menu()
                        elif menu_select == True:
                            constants.ISINTRO = True
                            pause = False
                            main()
            if selected == 1:
                resume_button = constants.RED
                resume_select = True
            else:
                resume_button = constants.BLACK
                resume_select = False
            if selected == 3:
                option_button = constants.RED
                option_select = True
            else:
                option_button = constants.BLACK
                option_select = False
            if selected == 4:
                menu_button = constants.RED
                menu_select = True
            else:
                menu_button = constants.BLACK
                menu_select = False
            if selected == 2:
                retry_button = constants.RED
                retry_select = True
            else:
                retry_button = constants.BLACK
                retry_select = False
            self.screen.fill(constants.WHITE)
            TextToScreen("Game Paused", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Resume", resume_button, -30, self.mediumfont, self.screen)
            TextToScreen("Retry", retry_button, 10, self.mediumfont, self.screen)
            TextToScreen("Options", option_button, 50, self.mediumfont, self.screen)
            TextToScreen("Main Menu", menu_button, 90, self.mediumfont, self.screen)
            pygame.display.flip()

    def intro(self):
        intro_bg = pygame.mixer.music.load("Game-Files/Sounds/Intro.wav")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(constants.music_volume)
        bg = pygame.image.load("Game-Files/Images/background_menu.png")
        bg_rect = bg.get_rect()
        intro = True
        is_selected = False
        selected = 1
        while intro:
            self.wrong_sound.set_volume(constants.effect_volume)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if not selected - 1 == 0:
                            selected -= 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_DOWN:
                        if not selected + 1 == 6:
                            selected += 1
                        else:
                            self.wrong_sound.play()
                    if event.key == pygame.K_RETURN:
                        if start_select == True:
                            constants.ISINTRO = False
                            intro = False
                        elif help_select == True:
                            self.Help()
                        elif option_select == True:
                            self.Option_Menu()
                        elif credit_select == True:
                            self.credits()
                        elif exit_select == True:
                            pygame.quit()
                            sys.exit()
            if selected == 1:
                start_button = constants.RED
                start_select = True
            else:
                start_button = constants.BLACK
                start_select = False
            if selected == 5:
                exit_button = constants.RED
                exit_select = True
            else:
                exit_button = constants.BLACK
                exit_select = True
            if selected == 4:
                credit_button = constants.RED
                credit_select = True
            else:
                credit_button = constants.BLACK
                credit_select = False
            if selected == 2:
                help_button = constants.RED
                help_select = True
            else:
                help_button = constants.BLACK
                help_select = False
            if selected == 3:
                option_button = constants.RED
                option_select = True
            else:
                option_button = constants.BLACK
                option_select = False
            self.screen.blit(bg, bg_rect)
            TextToScreen("Welcome to this Game!", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Start", start_button, -30, self.mediumfont, self.screen)
            TextToScreen("How to play", help_button, 10, self.mediumfont, self.screen)
            TextToScreen("Options", option_button, 50, self.mediumfont, self.screen)
            TextToScreen("Credits", credit_button, 90, self.mediumfont, self.screen)
            TextToScreen("Exit", exit_button, 130, self.mediumfont, self.screen)
            pygame.display.flip()
        pygame.mixer.music.stop()
