import pygame
from pygame.locals import *
import random

class Boss(object):
    def __init__(self,name,positionx,positiony,spawnpositonx,spawnpositiony,chunkx,chunky):
        self.name = name
        self.positionx = positionx
        self.positiony = positiony
        self.spawnpositionx = spawnpositonx
        self.spawnpositony = spawnpositiony
        self.chunkx = chunkx
        self.chunky = chunky

        self.posx = positionx
        self.posy = positiony

        self.spawned = False
        self.agro = False

        self.movement_Speed = 1
        self.agro_range = 90
        self.attack_range = 20
        self.attack_damage = 30
        self.attack_speed = 105
        self.life = 1000
        self.max_life = 1000

        self.attack_timer = 0
        self.has_attacked = False
        self.is_alive = True 
        self.realanimationtimer = 1
        self.dauerderFrames = 10
        self.animation = "move"
        self.move_frames = 4
        self.attack_frames = 5
        self.death_frames = 8
        self.pixel = 0
        self.moves = ["Nord","NordOst","SüdOst","Süden","Osten","SüdWest","Westen","NordWest"]
        

    def check_agro(self,player_posx,player_posy):
        Abstand_x = abs(self.posx - player_posx)
        Abstand_y = abs(self.posy - player_posy)

        #print("X Abstand zum player: "+str(Abstand_x))
        #print("Y Abstand zum Player: "+str(Abstand_y))

        if Abstand_x <= self.agro_range and Abstand_y <= self.agro_range:
            self.agro = True

        else:
            self.agro = False 

    def die(self):
        self.is_alive = False

    def recieve_damage(self,damage):
        
        self.life = self.life - damage
        if self.life <= 0 and self.is_alive == True:
            self.die()
            self.animation = "die"
            

    def move(self,player_posx, player_posy,playerchunkx,playerchunky,chunkwidth,chunkheight):
        #print("Ich habe gerade "+str(self.life)+" Leben")
        self.check_spawn(playerchunkx,playerchunky)
        self.check_agro(player_posx,player_posy)

        if self.spawned == True and self.agro == False and self.is_alive == True:
            self.animation = "move"
            Richtung = random.choice(self.moves)
            if Richtung == "Nord":
                self.posx	= self.posx
                self.posy = self.posy - self.movement_Speed
        
            elif Richtung == "NordOst":
                self.posx = self.posx + (self.movement_Speed/2)
                self.posy = self.posy - (self.movement_Speed/2)
        
            elif Richtung == "Osten":
                self.posx = self.posx + self.movement_Speed
                self.posy = self.posy
        
            elif Richtung == "SüdOst":
                self.posx = self.posx + (self.movement_Speed/2)
                self.posy = self.posy + (self.movement_Speed/2)

            elif Richtung == "Süden":
                self.posx = self.posx
                self.posy = self.posy + self.movement_Speed

            elif Richtung == "SüdWest":
                self.posx = self.posx - (self.movement_Speed/2)
                self.posy = self.posy + (self.movement_Speed/2)

            elif Richtung == "Westen":
                self.posx = self.posx - self.movement_Speed
                self.posy = self.posy

            elif Richtung == "NordWest":
                self.posx = self.posx - (self.movement_Speed/2)
                self.posy = self.posy - (self.movement_Speed/2)
            #print("MEineX: "+str(self.posx)+" MeineY: "+str(self.posy))
            if self.posx <= 0:
                print("Ich bin oben angestoßen")
                self.posx = chunkwidth - 1
            elif self.posx > chunkwidth:
                print("Ich bin unten angestoßen")
                self.posx = 1

            if self.posy <= 0:
                self.posy = chunkheight - 1
                print("Ich bin rechts angestoßen")
            elif self.posy > chunkheight:
                print("Ich bin links angestoßen")
                self.posy = 1

        if self.agro == True and self.is_alive == True:
            self.animation = "attack"
            
            if player_posx < self.posx:
                self.posx = self.posx - self.movement_Speed
                #print("1")
            elif player_posx > self.posx:
                self.posx = self.posx + self.movement_Speed
                #print("2")
            if player_posy < self.posy:
                self.posy = self.posy - self.movement_Speed
                #print("3")
            elif player_posy > self.posy:
                self.posy = self.posy + self.movement_Speed
                #print("4")
            
        return(self.posx,self.posy)

    def check_spawn(self,x,y):
        if self.chunkx == x and self.chunky == y:
            if self.spawned == False:
                self.spawned = True
                self.posx = self.spawnpositionx
                self.posy = self.spawnpositony
                print("gegner gespawnt")
        else:
            self.spawned = False
            self.posx = self.positionx
            self.posy = self.positiony

        if self.is_alive == False and self.realanimationtimer > 48:
            self.posx = 9000
            self.posy = 9000

    def checke_entfernung(self,player_posx,player_posy):
        Abstand_x = abs(self.posx - player_posx)
        Abstand_y = abs(self.posy - player_posy)
        return(Abstand_x,Abstand_y)

    def how_attack_damage(self,player_posx,player_posy):
        Damage = 0
        Abstand_x = abs(self.posx - player_posx)
        Abstand_y = abs(self.posy - player_posy)
        if self.has_attacked == False:
            if Abstand_x <= self.attack_range and Abstand_y <= self.attack_range:
                Damage = self.attack_damage
                self.has_attacked = True
        elif self.has_attacked == True:
            self.attack_timer = self.attack_timer + 1
            Damage = 0
            if self.attack_timer > self.attack_speed:
                self.attack_timer = 0
                self.has_attacked = False
        #print("Self.attacktimer = "+str(self.attack_timer))
        self.attack_timer = self.attack_timer+1
        return(Damage)

    def animate(self):
        self.realanimationtimer = self.realanimationtimer+1
        #print("Realanimationtimer: "+str(self.realanimationtimer))
        if self.animation == "move":
            if self.realanimationtimer <= 10:
                self.actualframe = "move_01"
                self.pixel = 0
            elif self.realanimationtimer <=20:
                self.actualframe = "move_02"
                self.pixel = 1
            elif self.realanimationtimer <=30:
                self.actualframe = "move_03"
                self.pixel = 2
            elif self.realanimationtimer <=40:
                self.actualframe = "move_04"
                self.pixel = 3
            elif self.realanimationtimer >40:
                self.realanimationtimer = 1 

        if self.animation == "attack":
            if self.realanimationtimer <= 10:
                self.actualframe = "attack_01"
                self.pixel = 4
            elif self.realanimationtimer <= 20:
                self.actualframe = "attack_02"
                self.pixel = 5
            elif self.realanimationtimer <= 30:
                self.actualframe = "attack_03"
                self.pixel = 6
            elif self.realanimationtimer <= 40:
                self.actualframe = "attack_04"
                self.pixel = 7
            elif self.realanimationtimer <= 50:
                self.actualframe = "attack_05"
                self.pixel = 8
            elif self.realanimationtimer >50:
                self.realanimationtimer = 1

        if self.animation == "die":
            if self.realanimationtimer <= 10:
                self.actualframe = "die_01"
                self.pixel = 9
            elif self.realanimationtimer <= 20:
                self.actualframe = "die_02"
                self.pixel = 10
            elif self.realanimationtimer <= 30:
                self.actualframe = "die_03"
                self.pixel = 11
            elif self.realanimationtimer <= 40:
                self.actualframe = "die_04"
                self.pixel = 12
            elif self.realanimationtimer <= 50:
                self.actualframe = "die_05"
                self.pixel = 13
            elif self.realanimationtimer <= 60:
                self.actualframe = "die_06"
                self.pixel = 14
            elif self.realanimationtimer <= 70:
                self.actualframe = "die_07"
                self.pixel = 15
            elif self.realanimationtimer <= 80:
                self.actualframe = "die_08"
                self.pixel = 16
            elif self.realanimationtimer >80:
                self.realanimationtimer = 1
                self.die()

        return(self.pixel)

class Lifebar(object):
    def __init__(self):
        self.RED = (255,0,0)
        self.RED2 = (255, 51, 0)
        self.visible = True

    def paint_Lifebar(self,screen,max_health,current_health,name):
        #Rect((left, top), (width, height)) -> Rect
        if self.visible == True:
            Leben1 = Rect((200,20), (612,30))
            healthpercent = self.calculate_Health(max_health,current_health)
            Leben2 = Rect((200,20), (int(612*healthpercent),30))
            pygame.draw.rect(screen,self.RED2,Leben1)
            pygame.draw.rect(screen,self.RED,Leben2)
            myfont = pygame.font.SysFont('Arial', 20)
            Healthtext = myfont.render(str(name)+": "+str(current_health)+"/"+str(max_health), False, (255, 255, 255))
            screen.blit(Healthtext,(210,22))
    def switch_visible(self):
        self.visible = False
    def calculate_Health(self,max_health,current_health):
        healthpercent = current_health/max_health
        if healthpercent > 1:
            healthpercent = 1
        if healthpercent < 0:
            healthpercent = 0
        return(healthpercent)  

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
        
        if Name == "Meraloren":
            self.IMG = pygame.image.load("Assets/Boss_Attack_03.png")
            if Dialognummer == 1:
                self.Texte = ["Du bist also derjenige, der meine Schergen getötet hat ... Um so", "weit zu kommen, um mir gegenüberzutreten, musst du sofort erledigt", "werden, damit du unsere Invasion nicht behindern kannst! "] 
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
            
            elif self.Timer > 300 :
                self.showable = False

            screen.blit(self.Text,(200,530))
            posx = 20
            posy = 516 - 20
            screen.blit(self.IMG,(posx,posy))



        
class Boss_Fight(object):
    def __init__(self,chunkx,chunky):
        self.chunkx = chunkx
        self.chunky = chunky
        self.started = False
        self.Lifebar = Lifebar()
        self.Boss = Boss("Meraloren",9000,9000,200,200,39,12)
        self.Dialog = Dialog("Meraloren",1)

        self.Boss_move01 = pygame.image.load("Assets/Boss_Walking_01.png")
        self.Boss_move02 = pygame.image.load("Assets/Boss_Walking_02.png")
        self.Boss_move03 = pygame.image.load("Assets/Boss_Walking_03.png")
        self.Boss_move04 = pygame.image.load("Assets/Boss_Walking_04.png")

        self.Boss_attack01 = pygame.image.load("Assets/Boss_Attack_01.png")
        self.Boss_attack02 = pygame.image.load("Assets/Boss_Attack_02.png")
        self.Boss_attack03 = pygame.image.load("Assets/Boss_Attack_03.png")
        self.Boss_attack04 = pygame.image.load("Assets/Boss_Attack_04.png")
        self.Boss_attack05 = pygame.image.load("Assets/Boss_Attack_05.png")

        self.Boss_death01 = pygame.image.load("Assets/Boss_Death_01.png")
        self.Boss_death02 = pygame.image.load("Assets/Boss_Death_02.png")
        self.Boss_death03 = pygame.image.load("Assets/Boss_Death_03.png")
        self.Boss_death04 = pygame.image.load("Assets/Boss_Death_04.png")
        self.Boss_death05 = pygame.image.load("Assets/Boss_Death_05.png")
        self.Boss_death06 = pygame.image.load("Assets/Boss_Death_06.png")
        self.Boss_death07 = pygame.image.load("Assets/Boss_Death_07.png")
        self.Boss_death08 = pygame.image.load("Assets/Boss_Death_08.png")

        self.Boss_IMG = [self.Boss_move01,self.Boss_move02,self.Boss_move03,self.Boss_move04,self.Boss_attack01,self.Boss_attack02,self.Boss_attack03,self.Boss_attack04,self.Boss_attack05,self.Boss_death01,self.Boss_death02,self.Boss_death03,self.Boss_death04,self.Boss_death05,self.Boss_death06,self.Boss_death07,self.Boss_death08]

    def check_pos(self,chunkx,chunky):
        if self.chunkx == chunkx and self.chunky == chunky:
            self.started = True

    def fight(self,screen,player,chunkx,chunky,controll):
        self.check_pos(chunkx,chunky)
        if self.started == True:
            self.Lifebar.paint_Lifebar(screen,self.Boss.max_life,self.Boss.life,self.Boss.name)
            posx,posy = self.Boss.move(player.pos_x, player.pos_y,chunkx,chunky,1024,576)
            pixel = self.Boss.animate()
            #print("Boss Position: "+str(posx)+"/"+str(posy))
            if controll == True:
                pos_x,pos_y = self.Boss.checke_entfernung(player.pos_x,player.pos_y)
                if pos_x <= player.attack_range and pos_y <= player.attack_range:
                    damage_done = player.attack()
                    self.Boss.recieve_damage(damage_done)
            Damage = self.Boss.how_attack_damage(player.pos_x,player.pos_y)
            player.damaged(Damage)
            if self.Boss.life <= 0:
                self.Lifebar.switch_visible()
            self.Dialog.show(screen)

            screen.blit(self.Boss_IMG[pixel],(posx,posy))