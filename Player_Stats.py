import pygame
from pygame.locals import *
from UI import UI
from Minimap import minimap

class Player_Stats(object):
    def __init__(self,screenwidth,screenheight,gameheight):

        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.gameheight = gameheight
        self.UI = UI()
        self.myfont = pygame.font.SysFont('Arial', 20)
        self.GREY = (153, 153, 102)
        self.BLACK = (0,0,0)
        self.GREEN = (0, 153, 51)
        self.GREEN2 = (102, 255, 102)
        self.BLUE = (0, 0, 255)
        self.BLUE2 = (0, 102, 255)
        self.RED = (255,0,0)
        self.RED2 = (255, 51, 0)

        self.Einheit = self.screenwidth / 32
        self.EinheitBar = self.Einheit - 10
        self.Start = self.screenheight + 10 
        self.Ende = self.gameheight - 10 
        self.Barwidth = (self.screenwidth - 40)-14*self.Einheit
        self.Barleft = 7*self.Einheit+20
        self.Abstand = 50
        self.IMG = pygame.image.load("Assets/Sword_Icon.png")

        self.Mapwidth = 7*int(self.Einheit)
        self.Mapheight = int(self.Ende - self.Start)-2
        self.Abilitie1 = Rect((self.Barleft+2*self.Einheit+ self.Abstand,self.Start),(self.Einheit*2,self.Einheit*2))
        self.Abilitie2 = Rect((self.Barleft+4*self.Einheit+self.Abstand+15,self.Start),(self.Einheit*2,self.Einheit*2))
        self.Abilitie3 = Rect((self.Barleft+6*self.Einheit+self.Abstand+30,self.Start),(self.Einheit*2,self.Einheit*2))
        self.Abilitie4 = Rect((self.Barleft+8*self.Einheit+self.Abstand+45,self.Start),(self.Einheit*2,self.Einheit*2))

        self.Q = Rect((self.Barleft,self.Start),(self.Einheit*2,self.Einheit*2))
        #print("X:"+str(self.Barleft))
        #print("Y:"+str(self.Start))
        self.E = Rect((self.Barleft+self.Barwidth-2*self.Einheit,self.Start),(self.Einheit*2,self.Einheit*2))
        #print("X:"+str(self.Barleft+self.Barwidth-2*self.Einheit))
        #print("Y:"+str(self.Start))
        self.Leben = Rect((self.Barleft,self.gameheight-12-self.EinheitBar-self.EinheitBar-5-self.EinheitBar-5),(self.Barwidth,self.EinheitBar))
        self.Mana = Rect((self.Barleft,self.gameheight-12-self.EinheitBar-self.EinheitBar-5),(self.Barwidth,self.EinheitBar))
        self.XP = Rect((self.Barleft,self.gameheight-12-self.EinheitBar),(self.Barwidth,self.EinheitBar))
        self.Background = Rect((0,self.screenheight),(self.screenwidth,self.gameheight-self.screenheight))
        self.Quest = Rect((10,self.Start),(7*int(self.Einheit),int(self.Ende - self.Start)-2))
        self.Map = Rect((int((self.screenwidth-10)-(self.Einheit*7)),self.Start),(7*int(self.Einheit),int(self.Ende - self.Start)-2))

        self.minimap = minimap()



    def draw_stats(self,player,screen,chunkx,chunky):
        self.screen = screen
        self.player = player
        pygame.draw.rect(self.screen, self.BLACK, self.Background)
        pygame.draw.rect(self.screen, self.GREY, self.Quest)
        pygame.draw.rect(self.screen, self.GREY, self.Map)
        pygame.draw.rect(self.screen,self.GREEN2,self.XP)
        pygame.draw.rect(self.screen,self.BLUE2,self.Mana)
        pygame.draw.rect(self.screen,self.RED2,self.Leben)
        pygame.draw.rect(self.screen,self.GREY,self.Q)
        pygame.draw.rect(self.screen,self.GREY,self.E)
        pygame.draw.rect(self.screen,self.GREY,self.Abilitie1)
        pygame.draw.rect(self.screen,self.GREY,self.Abilitie2)
        pygame.draw.rect(self.screen,self.GREY,self.Abilitie3)
        pygame.draw.rect(self.screen,self.GREY,self.Abilitie4)
        self.screen.blit(self.IMG,(716,586))
        Steuerungstext1 = self.myfont.render("Ctrl", False, (255, 255, 255))
        Steuerungstext2 = self.myfont.render("Q", False, (255, 255, 255))
        self.screen.blit(Steuerungstext1,(716,586+22))

        HealthMulti = self.UI.calculate_Health(self.player.max_health,self.player.current_health)
        #print("HealthMulti: "+str(HealthMulti))
        Leben2 = Rect((self.Barleft,self.gameheight-12-self.EinheitBar-self.EinheitBar-5-self.EinheitBar-5),(self.Barwidth*HealthMulti,self.EinheitBar))
        pygame.draw.rect(self.screen,self.RED,Leben2)
        #self.player.damaged(1)

        ManaMulti = self.UI.calculate_Mana(self.player.max_mana,self.player.current_mana)
        Mana2 = Rect((self.Barleft,self.gameheight-12-self.EinheitBar-self.EinheitBar-5),(self.Barwidth*ManaMulti,self.EinheitBar))
        pygame.draw.rect(self.screen,self.BLUE,Mana2)
        #self.player.use_abilitie_1()

        XPMulti = self.UI.calculate_XP(self.player.lvl,self.player.exp_multi,self.player.exp)
        XP2 = Rect((self.Barleft,self.gameheight-12-self.EinheitBar),(self.Barwidth*XPMulti,self.EinheitBar))
        pygame.draw.rect(self.screen,self.GREEN,XP2)
        #self.player.get_exp(100)

        Healthtext = self.myfont.render('HP: '+str(self.player.current_health)+" / "+str(self.player.max_health), False, (255, 255, 255))
        Manatext = self.myfont.render('MP: '+str(self.player.current_mana)+" / "+str(self.player.max_mana), False, (255, 255, 255))
        XPtext = self.myfont.render('XP: '+str(self.player.exp)+" / "+str(self.player.lvl*self.player.exp_multi), False, (255, 255, 255))
        self.screen.blit(Healthtext,(self.Barleft+20,self.gameheight-12-self.EinheitBar-self.EinheitBar-5-self.EinheitBar-5))
        self.screen.blit(Manatext,(self.Barleft+20,self.gameheight-12-self.EinheitBar-self.EinheitBar-5))
        self.screen.blit(XPtext,(self.Barleft+20,self.gameheight-12-self.EinheitBar))
    

        Charaktername = self.myfont.render('Name: '+str(self.player.name), False, (255, 255, 255)) 
        Charakterstrenght = self.myfont.render('Stärke: '+str(self.player.strenght), False, (255, 255, 255)) 
        Charakterlvl = self.myfont.render('LVL: '+str(self.player.lvl), False, (255, 255, 255)) 
        Charakterallxp = self.myfont.render('Allxp: '+str(self.player.all_exp), False, (255, 255, 255)) 
        Charaktergold = self.myfont.render('Gold: '+str(self.player.gold), False, (255, 255, 255)) 
        Charakterklasse = self.myfont.render('Klasse: '+str(self.player.charakterclass), False, (255, 255, 255)) 
        self.screen.blit(Charaktername,(12,self.Start))
        self.screen.blit(Charakterstrenght,(12,self.Start+20))
        self.screen.blit(Charakterlvl,(12,self.Start+40))
        self.screen.blit(Charakterallxp,(12,self.Start+60))
        self.screen.blit(Charaktergold,(12,self.Start+80))
        self.screen.blit(Charakterklasse,(12,self.Start+100))



        
        self.minimap.paint_minimap((self.screenwidth-10)-(self.Einheit*7),self.Start,chunkx,chunky,self.screen)

        posxminimap = int(self.player.pos_x/(self.screenwidth/self.Mapwidth))
        posyminimap = int(self.player.pos_y/(self.screenheight/self.Mapheight))
        mapplayerleft = int((self.screenwidth-10)-(self.Einheit*7))+posxminimap
        mapplayertop = self.Start+posyminimap
        self.minimap.paint_player(mapplayerleft,mapplayertop,self.screen,self.BLACK)