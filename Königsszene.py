import pygame
from pygame.locals import *
import random
import itertools

class Dialog(object):
    def __init__(self,Name,Dialognummer):
        self.Name = Name
        self.nr = Dialognummer
        self.Farbe = (175,255,200)
        self.showable = True
        self.Timer = 0
        self.Chatnummer = 0
        self.myfont = pygame.font.SysFont('Arial', 20)
        self.Chatbox = Rect((20,516), (984,50))
        
        if Name == "König":
            self.IMG = pygame.image.load("Assets/König_idle_01.png")
            if Dialognummer == 1:
                self.Texte = ["Sie sind also derjenige, über den mein General gesprochen hat. Er","sagte, Sie seien mit der Empfehlung des Kapitäns in Alsef","gekommen. Sie scheinen ein Maß an Stärke zu haben, auf das wir uns","möglicherweise verlassen können. Sehr gut, ich werde Ihnen sagen,","was gerade passiert. Die Dämonen haben begonnen, ihre Invasion","auszuweiten, und auf dem Berg Labsiam wurde ein mächtiger Dämon ","gesichtet. Ich möchte, dass du dort in den Tempel gehst, wo du als","nächstes hingehen musst. Möge die Stärke unserer Göttin dich","beschützen."] 
    def show(self,screen):

        if self.showable == True:
            pygame.draw.rect(screen,self.Farbe,self.Chatbox)
            self.Timer = self.Timer + 1
            if self.Timer <= 100 :
                self.Text = self.myfont.render(self.Texte[0], False, (0, 0, 0))

            elif self.Timer <= 200 :
                self.Text = self.myfont.render(self.Texte[1], False, (0, 0, 0))

            elif self.Timer <= 300 :
                self.Text = self.myfont.render(self.Texte[2], False, (0, 0, 0))
            
            elif self.Timer <= 400 :
                self.Text = self.myfont.render(self.Texte[3], False, (0, 0, 0))

            elif self.Timer <= 500 :
                self.Text = self.myfont.render(self.Texte[4], False, (0, 0, 0))

            elif self.Timer <= 600 :
                self.Text = self.myfont.render(self.Texte[5], False, (0, 0, 0))

            elif self.Timer <= 700 :
                self.Text = self.myfont.render(self.Texte[6], False, (0, 0, 0))

            elif self.Timer <= 800 :
                self.Text = self.myfont.render(self.Texte[7], False, (0, 0, 0))

            elif self.Timer <= 900 :
                self.Text = self.myfont.render(self.Texte[8], False, (0, 0, 0))

            elif self.Timer > 1000 :
                self.showable = False

            screen.blit(self.Text,(200,530))
            posx = 20
            posy = 516 - 20
            screen.blit(self.IMG,(posx,posy))

class Königsszene(object):
    def __init__(self):
        self.name = "nervige Bugs"
        self.showed = False
        self.animationtimer = 0

        self.IMG1 = pygame.image.load("Assets/König_idle_01.png")
        self.IMG2 = pygame.image.load("Assets/König_idle_02.png")
        self.IMG3 = pygame.image.load("Assets/König_idle_03.png")
        self.IMG4 = pygame.image.load("Assets/König_idle_04.png")
        self.IMG5 = pygame.image.load("Assets/König_idle_05.png")
        self.animate_cycle = [self.IMG1,self.IMG2,self.IMG3,self.IMG4,self.IMG5]
        self.actual_image = self.IMG1
        self.cycle = itertools.cycle(self.animate_cycle)
        next(self.cycle)

        self.pos_x = 28*32
        self.pos_y = 13*32
        self.chunkx = 39
        self.chunky = 10
        self.Dialog = Dialog("König",1)

    def start_Scene(self, screen, chunkx, chunky):
        
        if self.showed == False:
            if self.chunkx == chunkx and self.chunky == chunky:
                self.Dialog.show(screen)
                self.animationtimer = self.animationtimer + 1
                if self.animationtimer % 10 == 0:
                    self.actual_image = next(self.cycle)
                screen.blit(self.actual_image,(self.pos_x,self.pos_y))

    def activate_questes(self):
        activate_Quest = False
        if self.Dialog.showable == False:
            activate_Quest = True
        
        return(activate_Quest)



        