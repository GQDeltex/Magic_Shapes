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
        
        self.screen = screen
        
    def Game_Over(self, caption = "Game Over!", addinfo = ""):
        gameOver = True
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main()
                    if event.key == pygame.K_ESCAPE:
                        gameOver = False
                        pygame.quit()
                        sys.exit()
            self.screen.fill(constants.WHITE)
            TextToScreen(caption, constants.GREEN, -150, self.bigfont, self.screen)
            TextToScreen("Press Space to play again or Escape to Quit", constants.BLACK, 10, self.smallfont, self.screen)
            TextToScreen(addinfo, constants.RED, -30, self.smallfont, self.screen)
            pygame.display.flip()
    
    def Level_screen(self, level):
        self.screen.fill(constants.WHITE)
        TextToScreen(("Level:" + str(level)), constants.GREEN, -150, self.bigfont, self.screen)
        pygame.display.flip()
        sleep(2)
    
    def credits(self):   
        credits = True
        while credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        credits = False
            self.screen.fill(constants.WHITE)
            TextToScreen("Credits", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Code: Peter", constants.BLACK, -30, self.smallfont, self.screen)
            TextToScreen("Art: Malin, Madita, Peter", constants.BLACK, 10, self.smallfont, self.screen)
            TextToScreen("Sound & Music: Malin, Madita", constants.BLACK, 50, self.smallfont, self.screen)
            TextToScreen("Made for Ludum Dare 35", constants.BLACK, 90, self.smallfont, self.screen)
            TextToScreen("Esc to get back to the Main Menu", constants.BLACK, 180, self.smallfont, self.screen)
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
                    if event.key == pygame.K_ESCAPE:
                        credits = False
            self.screen.fill(constants.WHITE)
            TextToScreen("How to play", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Grab the blue boxes to shapeshift", constants.BLACK, -30, self.mediumfont, self.screen)
            TextToScreen("Jump to the End of the Level", constants.BLACK, 10, self.mediumfont, self.screen)
            TextToScreen("to get to the next Level!", constants.BLACK, 50, self.mediumfont, self.screen)
            TextToScreen("Esc to get back to the Main Menu", constants.BLACK, 180, self.smallfont, self.screen)
            pygame.display.flip()
    
    
    def intro(self):
        intro_bg = pygame.mixer.music.load("Game-Files/Sounds/Intro.wav")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.5)
        bg = pygame.image.load("Game-Files/Images/background_menu.png")
        bg_rect = bg.get_rect()
        intro = True 
        is_selected = False
        selected = 1
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if not selected - 1 == 0:
                            selected -= 1
                    if event.key == pygame.K_DOWN:
                        if not selected + 1 == 5:
                            selected += 1
                    if event.key == pygame.K_RETURN:
                        if start_select == True:
                            constants.ISINTRO = False
                            intro = False
                        elif help_select == True:
                            self.Help()
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
            if selected == 4:
                exit_button = constants.RED
                exit_select = True
            else:
                exit_button = constants.BLACK
                exit_select = True
            if selected == 3:
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
            self.screen.blit(bg, bg_rect)
            TextToScreen("Welcome to this Game!", constants.BLACK, -150, self.bigfont, self.screen)
            TextToScreen("Start", start_button, -30, self.mediumfont, self.screen)
            TextToScreen("How to play", help_button, 10, self.mediumfont, self.screen)
            TextToScreen("Credits", credit_button, 50, self.mediumfont, self.screen)
            TextToScreen("Exit", exit_button, 90, self.mediumfont, self.screen)
            pygame.display.flip()
        pygame.mixer.music.stop()    