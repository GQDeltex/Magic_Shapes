import pygame
import constants
import socket
from time import sleep

class Client():
    def __init__(self,Adress=(constants.IP, constants.PORT)):
        self.Adress = Adress
    def sendData(self,Message):
        self.s = socket.socket()
        self.s.connect(self.Adress)
        self.s.send(str(Message))
    def getData(self):
        self.s = socket.socket()
        self.s.connect(self.Adress)
        return  self.s.recv(20)

class Server():
    def __init__(self,Adress=('',constants.PORT),MaxClient=1):
        print "Creating socket"
        self.s = socket.socket()
        print "Binding Adress"
        self.s.bind(Adress)
        print "Set to listen"
        self.s.listen(MaxClient)
        sleep(0.5)

    def getData(self):
        #print "Accept Connection"
        self.Client, self.Adr=(self.s.accept())
        #print "Recieving Data"
        back = self.Client.recv(20)
        #print "Successfull recieved:" + str(back)
        return back

    def sendData(self, Message):
        #print "Accept Connection"
        self.Client, self.Adr=(self.s.accept())
        #print "Sending Message:" + str(Message)
        self.Client.send(str(Message))

class locmake():
    def __init__(self):
        pass

    def getLocation(self, eingabe):
        eingabe = eingabe.translate(None, "() ") #Klammern entfernen
        self.x, self.y, self.dir, self.level, self.current = eingabe.split(",") #Am Komma aufteilen
        self.x = int(self.x) #Nummern aus Strings machen
        self.y = int(self.y) #No.2
        self.dir = self.dir.translate(None, " '' "" ") #Klammern entfernen
        self.current = int(self.current)
        self.level = int(self.level)
        print "|X:" + str(self.x) + " |Y:" + str(self.y) + " |D:" + str(self.dir) + " |L:" + str(self.level) + " |C:" + str(self.current)
        return self.x, self.y, self.dir, self.level, self.current #Ausgeben


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
        textSurf, textRect = self.text_objects(msg, color, font)
        textRect.center = (constants.SCREEN_WIDTH/2), (constants.SCREEN_HEIGHT/2) + y_displace
        screen.blit(textSurf, textRect)

    def text_objects(self, text, color, size):
        textSurface = size.render(text, True, color)
        return textSurface, textSurface.get_rect()

class Mystery_tools(object):
    def __init__(self, x, y):
            self.rect = pygame.Rect((x*32), (y*32), 32, 32)
            self.rect.x = (x*32)
            self.rect.y = (y*32)
