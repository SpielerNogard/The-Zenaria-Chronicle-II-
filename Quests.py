import pygame
from pygame.locals import *

from Aufgaben import Aufgaben
#(name,beschreibung,gegenstand1,gegenstand2,gegenstand3,gegenstand1_max,gegenstand2_max,gegenstand3_max,chunkx,chunky,spawnposx,spawnposy,gold,xp):
class Quests(object):
    def __init__(self):
        #self.Quest1 = Aufgaben("Der Kapitän","Finde den Kapitän und spreche mit ihm","der Kapitän","","",1,0,0,10,10,32,448,10,0)
        #self.Quest2 = Aufgaben("Die Geschichte","Hören sie dem Kapitän zu","Die Geschichte","","",1,0,0,10,11,800,320,10,0)
        #self.Quest3 = Aufgaben("Die Questboards","Aktiviere das Questboard","Das Questboard","","",1,0,0,11,11,224,320,10,0)
        self.Quest4 = Aufgaben("Holz für Brena","Sammle Holz und bringe es nach Brena","Slime","Holzscheite","",10,10,0,11,12,224,320,10,10,12,16)
        self.Quest5 = Aufgaben("Kleber für Kapitän","Töte Schleime für Klebstoff","Slime","klebriger Schleim","",10,20,0,13,15,320,448,100,100,14,14)
        self.Quest6 = Aufgaben("Ein Freund","Begib dich nach Volen","Wolf","Wolfspelz","",7,5,0,12,16,800,288,100,100,13,5)
        self.Quest7 = Aufgaben("Der König","Begib dich zum Schloss","Schloss","König","",1,1,0,13,3,512,448,100,100,12,0)
        self.Quest8 = Aufgaben("Die Dämonen","Begib dich zum Tempel","kleine Dämonen","Tempel","",15,1,0,12,0,512,320,100,100,6,4)
        #self.Quest9 = Aufgaben("Die Prüfungen","Bestehe die 4 Prüfungen","Prüfungen","","",4,0,0,6,4,512,64,100,100)
        #self.Quest10 = Aufgaben("Dunkelheit","Löse das Rätsel und töte den Boss","Rätsel","Boss","",1,1,0,6,4,192,32,100,100)
        #self.Quest11 = Aufgaben("Echo","Löse das Rätsel und töte den Boss","Rätsel","Boss","",1,1,0,6,4,288,384,100,100)
        #self.Quest12 = Aufgaben("Sand","Löse das Rätsel und töte den Boss","Rätsel","Boss","",1,1,0,6,4,674,448,100,100)
        #self.Quest13 = Aufgaben("Rauch","Löse das Rätsel und töte den Boss","Rätsel","Boss","",1,1,0,5,4,928,32,100,100)
        #self.Quest14 = Aufgaben("Hinklo","Treffe den Bürgermeister von Hinklo","Bürgermeister","","",1,0,0,6,6,928,320,100,100)
        self.Quest15 = Aufgaben("Der Guy","Töte den mächtigen Dämonen","Dämon","","",1,0,0,5,6,64,352,100,100,4,6)


        self.screenwidth = 1024
        self.screenheight = 576
        self.allQuests = [self.Quest4,self.Quest5,self.Quest6,self.Quest7,self.Quest8,self.Quest15]
        self.active_Quests=[]
        self.Questboard = pygame.image.load("Assets/questboard.png")
        self.QuestionMark = pygame.image.load("Assets/questionmark.png")
        self.ExclamationMark = pygame.image.load("Assets/exclamationmark.png")

        self.Questwindow = False

    def give_goal(self):
        Ziel_x = 9999
        Ziel_y = 9999
        if self.active_Quests != []:
            die_Quest = self.active_Quests[0]
            Ziel_x = die_Quest.zielchunkx
            Ziel_y = die_Quest.zielchunky

        return(Ziel_x,Ziel_y)
    def check_spawn(self,playerchunkx,playerchunky,screen,playerposx,playerposy,player,Questwindow,enter_pressed):
        self.Questwindow = Questwindow
        myfont = pygame.font.SysFont('Arial', 30)
        for a in self.allQuests:
            if a.chunkx == playerchunkx and a.chunky == playerchunky:
                a.spawn()

            else: 
                a.despawn()

            if a.is_active == True:
                screen.blit(self.QuestionMark,(a.currentposx+32,a.currentposy-32))
                screen.blit(self.Questboard,(a.currentposx,a.currentposy))
            else:
                screen.blit(self.ExclamationMark,(a.currentposx+32,a.currentposy-32))
                screen.blit(self.Questboard,(a.currentposx,a.currentposy))
            finished = a.check_finished()
            if finished == True and a.already_claimed == False:
                a.claim()
                player.get_exp(a.xp)
                player.get_gold(a.gold)
            if a.already_claimed == True:
                if a in self.active_Quests:
                    self.active_Quests.remove(a)
            a.check_position(playerposx,playerposy)
            if Questwindow == True and a.near_enough == True:
                GREY = (153, 153, 102)
                Questwindow = Rect((100,100),(self.screenwidth-200,self.screenheight-200))
                pygame.draw.rect(screen, GREY, Questwindow)
                Questname = myfont.render(str(a.name), False, (255, 255, 255))
                Questbeschreibung = myfont.render(str(a.beschreibung), False, (255, 255, 255))
                Queststep1 = myfont.render(str(a.gegenstand1)+" "+str(a.gegenstand1_current)+"/"+str(a.gegenstand1_max), False, (255, 255, 255))
                Queststep2 = myfont.render(str(a.gegenstand2)+" "+str(a.gegenstand2_current)+"/"+str(a.gegenstand2_max), False, (255, 255, 255))
                annehmen = myfont.render("Zum annehmen ENTER drücken", False, (255, 255, 255))
                screen.blit(Queststep1,(150,350))
                screen.blit(Queststep2,(150,400))
                screen.blit(annehmen,(self.screenwidth/2-200,430))
                screen.blit(Questname,(self.screenwidth/2-100,100))
                screen.blit(Questbeschreibung,(150,150))
                if enter_pressed == True:
                    a.activate_Quest()
                    if not a in self.active_Quests:
                        self.active_Quests.append(a)
                    self.Questwindow = False
                elif self.Questwindow == True and a.near_enough == False:
                    self.Questwindow  = False
            for a in self.active_Quests:
                    print(a.name)

            #screen.blit(self.Questboard,(a.currentposx,a.currentposy))

    def activate_this_quest(self,name):
        for a in self.allQuests:
            if a.name == name:
                a.activate_Quest()
                if not a in self.active_Quests:
                        self.active_Quests.append(a)

    def Quest_Stats(self,screen,screenwidth,gameheight):
        myfont = pygame.font.SysFont('Arial', 30)
        GREY = (153, 153, 102)
        BLACK = (0,0,0)
        Start = screenwidth
        Höhe = gameheight
        Breite = 400
        Background = Rect((Start,0),(Breite,Höhe))
        pygame.draw.rect(screen,GREY,Background)
        quest = myfont.render("Active Quests", False, (255, 255, 255))
        screen.blit(quest,(Start+10,10))
        i = 0
        for a in self.active_Quests:
            name = myfont.render(str(a.name), False, (255, 255, 255))
            screen.blit(name,(Start+10,(50)+(150*i)))
            if a.gegenstand1 != "":
                Queststep1 = myfont.render(str(a.gegenstand1)+" "+str(a.gegenstand1_current)+"/"+str(a.gegenstand1_max), False, (255, 255, 255))
                screen.blit(Queststep1,(Start+50,(90)+(150*i)))
            if a.gegenstand2 != "":
                Queststep2 = myfont.render(str(a.gegenstand2)+" "+str(a.gegenstand2_current)+"/"+str(a.gegenstand2_max), False, (255, 255, 255))
                screen.blit(Queststep2,(Start+50,(125)+(150*i)))
            if a.gegenstand3 != "":
                Queststep3 = myfont.render(str(a.gegenstand3)+" "+str(a.gegenstand3_current)+"/"+str(a.gegenstand3_max), False, (255, 255, 255))
                screen.blit(Queststep3,(Start+50,(160)+(150*i)))
            i = i+1
            
            

    def Give_Drops_to_Quest(self,Drops):
        for a in self.active_Quests:
            a.check_Drops(Drops)
            
        
    

    