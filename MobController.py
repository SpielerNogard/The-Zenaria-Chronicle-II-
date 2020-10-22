import pygame
import random
from Gegner import MOB

class MobController(object):
    def __init__(self):
        self.Slime1 = MOB("Klaus","Slime",9000,9000,32,32,14,14,"Nord")
        self.Slime2 = MOB("Klaus","Slime",9000,9000,64,192,14,14,"NordOst")
        self.Slime3 = MOB("Klaus","Slime",9000,9000,160,384,14,14,"Osten")
        self.Slime4 = MOB("Klaus","Slime",9000,9000,512,32,14,14,"SüdOst")
        self.Slime5 = MOB("Klaus","Slime",9000,9000,480,416,14,14,"Süden")
        self.Slime6 = MOB("Klaus","Slime",9000,9000,480,416,14,14,"SüdWest")
        self.Slime7 = MOB("Klaus","Slime",9000,9000,480,416,14,14,"Westen")
        self.Slime8 = MOB("Klaus","Slime",9000,9000,480,416,14,14,"NordWest")

        self.Slime9 = MOB("Klaus","Slime",9000,9000,32,32,14,13,"Nord")
        self.Slime10 = MOB("Klaus","Slime",9000,9000,64,192,14,13,"NordOst")
        self.Slime11 = MOB("Klaus","Slime",9000,9000,160,384,14,13,"Osten")
        self.Slime12 = MOB("Klaus","Slime",9000,9000,512,32,14,13,"SüdOst")
        self.Slime13 = MOB("Klaus","Slime",9000,9000,480,416,14,13,"Süden")
        self.Slime14 = MOB("Klaus","Slime",9000,9000,480,416,14,13,"SüdWest")
        self.Slime15 = MOB("Klaus","Slime",9000,9000,480,416,14,13,"Westen")
        self.Slime16 = MOB("Klaus","Slime",9000,9000,480,416,14,13,"NordWest")

        self.Slime17 = MOB("Klaus","Slime",9000,9000,32,32,16,13,"Nord")
        self.Slime18 = MOB("Klaus","Slime",9000,9000,64,192,16,13,"NordOst")
        self.Slime19 = MOB("Klaus","Slime",9000,9000,160,384,16,13,"Osten")
        self.Slime20 = MOB("Klaus","Slime",9000,9000,512,32,16,13,"SüdOst")
        self.Slime21 = MOB("Klaus","Slime",9000,9000,480,416,16,13,"Süden")
        self.Slime22 = MOB("Klaus","Slime",9000,9000,480,416,16,13,"SüdWest")
        self.Slime23 = MOB("Klaus","Slime",9000,9000,480,416,16,13,"Westen")
        self.Slime24 = MOB("Klaus","Slime",9000,9000,480,416,16,13,"NordWest")

        self.Slime25 = MOB("Klaus","Slime",9000,9000,32,32,15,13,"Nord")
        self.Slime26 = MOB("Klaus","Slime",9000,9000,64,192,15,13,"NordOst")
        self.Slime27 = MOB("Klaus","Slime",9000,9000,160,384,15,13,"Osten")
        self.Slime28 = MOB("Klaus","Slime",9000,9000,512,32,15,13,"SüdOst")
        self.Slime29 = MOB("Klaus","Slime",9000,9000,480,416,15,13,"Süden")
        self.Slime30 = MOB("Klaus","Slime",9000,9000,480,416,15,13,"SüdWest")
        self.Slime31 = MOB("Klaus","Slime",9000,9000,480,416,15,13,"Westen")
        self.Slime32 = MOB("Klaus","Slime",9000,9000,480,416,15,13,"NordWest")
        
        self.Wolf1 = MOB("Klaus","Wolf",9000,9000,24*32,2*32,16,14,"Nord")
        self.Wolf2 = MOB("Klaus","Wolf",9000,9000,30*32,2*32,16,14,"NordOst")
        self.Wolf3 = MOB("Klaus","Wolf",9000,9000,31*32,6*32,16,14,"Osten")
        self.Wolf4 = MOB("Klaus","Wolf",9000,9000,21*32,7*32,16,14,"SüdOst")
        self.Wolf5 = MOB("Klaus","Wolf",9000,9000,15*32,11*32,16,14,"Süden")
        self.Wolf6 = MOB("Klaus","Wolf",9000,9000,23*32,11*32,16,14,"SüdWest")
        self.Wolf7 = MOB("Klaus","Wolf",9000,9000,30*32,11*32,16,14,"Westen")
        self.Wolf8 = MOB("Klaus","Wolf",9000,9000,30*32,16*32,16,14,"NordWest")

        self.Wolf9 = MOB("Klaus","Wolf",9000,9000,2*32,1*32,17,14,"Nord")
        self.Wolf10 = MOB("Klaus","Wolf",9000,9000,10*32,4*32,17,14,"NordOst")
        self.Wolf11 = MOB("Klaus","Wolf",9000,9000,16*32,9*32,17,14,"Osten")
        self.Wolf12 = MOB("Klaus","Wolf",9000,9000,19*32,15*32,17,14,"SüdOst")
        self.Wolf13 = MOB("Klaus","Wolf",9000,9000,12*32,16*32,17,14,"Süden")
        self.Wolf14 = MOB("Klaus","Wolf",9000,9000,8*32,10*32,17,14,"SüdWest")
        self.Wolf15 = MOB("Klaus","Wolf",9000,9000,2*32,10*32,17,14,"Westen")
        self.Wolf16 = MOB("Klaus","Wolf",9000,9000,3*32,15*32,17,14,"NordWest")

        self.Wolf17 = MOB("Klaus","Wolf",9000,9000,27*32,3*32,16,15,"Nord")
        self.Wolf18 = MOB("Klaus","Wolf",9000,9000,27*32,8*32,16,15,"NordOst")
        self.Wolf19 = MOB("Klaus","Wolf",9000,9000,19*32,11*32,16,15,"Osten")
        self.Wolf20 = MOB("Klaus","Wolf",9000,9000,19*32,5*32,16,15,"SüdOst")
        self.Wolf21 = MOB("Klaus","Wolf",9000,9000,12*32,9*32,16,15,"Süden")

        self.Wolf22 = MOB("Klaus","Wolf",9000,9000,2*32,2*32,17,15,"SüdWest")
        self.Wolf23 = MOB("Klaus","Wolf",9000,9000,10*32,2*32,17,15,"Westen")
        self.Wolf24 = MOB("Klaus","Wolf",9000,9000,20*32,2*32,17,15,"NordWest")

        self.Demon1 = MOB("Klaus","Dämon",9000,9000,20*32,2*32,10,10,"NordWest")
        

        self.Golem1 = MOB("Klaus","Golem",9000,9000,20*32,2*32,10,10,"Süden")

        self.Golem2  = MOB("Klaus","Golem",9000,9000,24*32,13*32,40,0,"Süden")
        self.Golem3  = MOB("Klaus","Golem",9000,9000,26*32,4*32,40,1,"Westen")
        self.Golem4  = MOB("Klaus","Golem",9000,9000,28*32,6*32,40,3,"Westen")
        self.Golem5  = MOB("Klaus","Golem",9000,9000,19*32,14*32,40,3,"Westen")
        
        self.Golem6 = MOB("Klaus","Golem",9000,9000,16*32,3*32,40,4,"NordWest")
        self.Golem7 = MOB("Klaus","Golem",9000,9000,14*32,6*32,41,4,"NordOst")
        self.Golem8 = MOB("Klaus","Golem",9000,9000,23*32,7*32,41,4,"NordOst")

        self.Golem9 = MOB("Klaus","Golem",9000,9000,9*32,14*32,41,3,"SüdOst")
        self.Golem10  = MOB("Klaus","Golem",9000,9000,5*32,6*32,41,3,"SüdOst")
        self.Golem11 = MOB("Klaus","Golem",9000,9000,21*32,4*32,41,3,"SüdOst")

        



        self.Slimerandom = MOB("Klaus","Slime",9000,9000,480,416,40,8,"NordWest")
        self.Wolfrandom = MOB("Klaus","Wolf",9000,9000,12*32,9*32,40,8,"Süden")
        self.Demonrandom = MOB("Klaus","Dämon",9000,9000,20*32,2*32,40,8,"NordWest")
        self.Golemrandom = MOB("Klaus","Golem",9000,9000,20*32,2*32,40,8,"Süden")

        #self.Slime1 = MOB("Klaus","Wolf",9000,9000,200,200,12,10,"Westen")
        self.Wolf_list1 = [self.Wolf1,self.Wolf2,self.Wolf3,self.Wolf4,self.Wolf5,self.Wolf6,self.Wolf7,self.Wolf8,self.Wolf9,self.Wolf10,self.Wolf11,self.Wolf12,self.Wolf13,self.Wolf14]
        self.Wolf_list2 = [self.Wolf15,self.Wolf16,self.Wolf17,self.Wolf18,self.Wolf19,self.Wolf20,self.Wolf21,self.Wolf22,self.Wolf23,self.Wolf24]
        self.Slime_list1=[self.Slime1,self.Slime2,self.Slime3,self.Slime4,self.Slime5,self.Slime6,self.Slime7,self.Slime8,self.Slime9,self.Slime10,self.Slime11,self.Slime12,self.Slime13,self.Slime14,self.Slime15]
        self.Slime_list2 = [self.Slime16,self.Slime17,self.Slime18,self.Slime19,self.Slime20,self.Slime21,self.Slime22,self.Slime23,self.Slime24,self.Slime25,self.Slime26,self.Slime27,self.Slime28,self.Slime29,self.Slime30,self.Slime31,self.Slime32]
        self.Golem_list1 = [self.Golem2,self.Golem3,self.Golem4,self.Golem5,self.Golem6,self.Golem7,self.Golem8,self.Golem9,self.Golem10,self.Golem11]

        self.random_list1 = [self.Slimerandom,self.Wolfrandom,self.Demonrandom,self.Golemrandom]
        self.all_enemies = self.Slime_list1 + self.Slime_list2 + self.Wolf_list1 + self.Wolf_list2 + self.Golem_list1 + self.random_list1

        self.slime_move_01 = pygame.image.load("Assets/slime_move_01.png")
        self.slime_move_02 = pygame.image.load("Assets/slime_move_02.png")
        self.slime_move_01_red = pygame.image.load("Assets/slime_move_01_red.png")
        self.slime_move_02_red = pygame.image.load("Assets/slime_move_02_red.png")

        self.slime_attack_01 = pygame.image.load("Assets/slime_attack_01.png")
        self.slime_attack_02 = pygame.image.load("Assets/slime_attack_02.png")
        self.slime_attack_03 = pygame.image.load("Assets/slime_attack_03.png")
        self.slime_attack_04 = pygame.image.load("Assets/slime_attack_04.png")
        self.slime_attack_05 = pygame.image.load("Assets/slime_attack_05.png")
        self.slime_attack_01_red = pygame.image.load("Assets/slime_attack_01_red.png")
        self.slime_attack_02_red = pygame.image.load("Assets/slime_attack_02_red.png")
        self.slime_attack_03_red = pygame.image.load("Assets/slime_attack_03_red.png")
        self.slime_attack_04_red = pygame.image.load("Assets/slime_attack_04_red.png")
        self.slime_attack_05_red = pygame.image.load("Assets/slime_attack_05_red.png")

        self.slime_death_01 =  pygame.image.load("Assets/slime_death_01.png")
        self.slime_death_02 = pygame.image.load("Assets/slime_death_02.png")
        self.slime_death_03 = pygame.image.load("Assets/slime_death_03.png")
        self.slime_death_04 = pygame.image.load("Assets/slime_death_04.png")
        self.slime_death_05 = pygame.image.load("Assets/slime_death_05.png")
        
        self.slime_animation = [self.slime_move_01,self.slime_move_02,self.slime_attack_01,self.slime_attack_02,self.slime_attack_03,self.slime_attack_04,self.slime_attack_05,self.slime_death_01,self.slime_death_02,self.slime_death_03,self.slime_death_04,self.slime_death_05]

        self.wolf_move_01 = pygame.image.load("Assets/Wolf_Walking_01.png")
        self.wolf_move_02 = pygame.image.load("Assets/Wolf_Walking_02.png")
        self.wolf_move_01_red = pygame.image.load("Assets/Wolf_red_Walking_01.png")
        self.wolf_move_02_red = pygame.image.load("Assets/Wolf_red_Walking_02.png")

        self.wolf_attack_01 = pygame.image.load("Assets/Wolf_Attack_01.png")
        self.wolf_attack_02 = pygame.image.load("Assets/Wolf_Attack_02.png")
        self.wolf_attack_03 = pygame.image.load("Assets/Wolf_Attack_03.png")
        self.wolf_attack_04 = pygame.image.load("Assets/Wolf_Attack_04.png")
        self.wolf_attack_05 = pygame.image.load("Assets/Wolf_Attack_05.png")

        self.wolf_attack_01_red = pygame.image.load("Assets/Wolf_red_Attack_01.png")
        self.wolf_attack_02_red = pygame.image.load("Assets/Wolf_red_Attack_02.png")
        self.wolf_attack_03_red = pygame.image.load("Assets/Wolf_red_Attack_03.png")
        self.wolf_attack_04_red = pygame.image.load("Assets/Wolf_red_Attack_04.png")
        self.wolf_attack_05_red = pygame.image.load("Assets/Wolf_red_Attack_05.png")

        self.wolf_death_01 =  pygame.image.load("Assets/Wolf_Death_01.png")
        self.wolf_death_02 = pygame.image.load("Assets/Wolf_Death_02.png")
        self.wolf_death_03 = pygame.image.load("Assets/Wolf_Death_03.png")
        self.wolf_death_04 = pygame.image.load("Assets/Wolf_Death_04.png")
        self.wolf_death_05 = pygame.image.load("Assets/Wolf_Death_05.png")
        self.wolf_animation = [self.wolf_move_01,self.wolf_move_02,self.wolf_attack_01,self.wolf_attack_02,self.wolf_attack_03,self.wolf_attack_04,self.wolf_attack_05,self.wolf_death_01,self.wolf_death_02,self.wolf_death_03,self.wolf_death_04,self.wolf_death_05]

        self.demon_move_01 = pygame.image.load("Assets/Small_Demon_Walking_01.png")
        self.demon_move_02 = pygame.image.load("Assets/Small_Demon_Walking_02.png")
        

        self.demon_attack_01 = pygame.image.load("Assets/Small_Demon_Attack_01.png")
        self.demon_attack_02 = pygame.image.load("Assets/Small_Demon_Attack_02.png")
        self.demon_attack_03 = pygame.image.load("Assets/Small_Demon_Attack_03.png")
        self.demon_attack_04 = pygame.image.load("Assets/Small_Demon_Attack_04.png")
        self.demon_attack_05 = pygame.image.load("Assets/Small_Demon_Attack_05.png")

        self.demon_death_01 =  pygame.image.load("Assets/Small_Demon_Death_01.png")
        self.demon_death_02 = pygame.image.load("Assets/Small_Demon_Death_02.png")
        self.demon_death_03 = pygame.image.load("Assets/Small_Demon_Death_03.png")
        self.demon_death_04 = pygame.image.load("Assets/Small_Demon_Death_04.png")
        self.demon_death_05 = pygame.image.load("Assets/Small_Demon_Death_05.png")
        self.demon_animation = [self.demon_move_01,self.demon_move_02,self.demon_attack_01,self.demon_attack_02,self.demon_attack_03,self.demon_attack_04,self.demon_attack_05,self.demon_death_01,self.demon_death_02,self.demon_death_03,self.demon_death_04,self.demon_death_05]
        
        self.golem_move_01 = pygame.image.load("Assets/Golem_Walking_01.png")
        self.golem_move_02 = pygame.image.load("Assets/Golem_Walking_02.png")
        

        self.golem_attack_01 = pygame.image.load("Assets/Golem_Attack_01.png")
        self.golem_attack_02 = pygame.image.load("Assets/Golem_Attack_02.png")
        self.golem_attack_03 = pygame.image.load("Assets/Golem_Attack_03.png")
        self.golem_attack_04 = pygame.image.load("Assets/Golem_Attack_04.png")
        self.golem_attack_05 = pygame.image.load("Assets/Golem_Attack_05.png")

        self.golem_death_01 =  pygame.image.load("Assets/Golem_Death_01.png")
        self.golem_death_02 = pygame.image.load("Assets/Golem_Death_02.png")
        self.golem_death_03 = pygame.image.load("Assets/Golem_Death_03.png")
        self.golem_death_04 = pygame.image.load("Assets/Golem_Death_04.png")
        self.golem_death_05 = pygame.image.load("Assets/Golem_Death_05.png")
        self.golem_animation = [self.golem_move_01,self.golem_move_02,self.golem_attack_01,self.golem_attack_02,self.golem_attack_03,self.golem_attack_04,self.golem_attack_05,self.golem_death_01,self.golem_death_02,self.golem_death_03,self.golem_death_04,self.golem_death_05]

        self.Random_Timer = 0
        self.gestorbene_Gegner = []
    def enemies(self,player,chunkx,chunky,screen,controll):
        self.gestorbene_Gegner = []
        for a in self.all_enemies:
            if controll == True:
                pos_x,pos_y = a.checke_entfernung(player.pos_x,player.pos_y)
                if pos_x <= player.attack_range and pos_y <= player.attack_range:
                    damage_done = player.attack()
                    Drops = a.recieve_damage(damage_done)
                    if Drops != "":
                        self.gestorbene_Gegner.append(Drops)
                        for b in self.gestorbene_Gegner:
                            print(b)
                    #print("Der folgende Gegner ist diesen Frame gestorben: "+str(Drops))
                    #print("Sie haben "+str(damage_done)+" Damage gemacht")

                    
            posx,posy = a.move(player.pos_x,player.pos_y,chunkx,chunky,1024,576)
            Damage = a.how_attack_damage(player.pos_x,player.pos_y)
            player.damaged(Damage)
            frame,attacked = a.animate()
            Sprite = self.Animate_Enemy(frame,a.klasse)
            screen.blit(Sprite,(posx,posy))

    def Animate_Enemy(self,frame,klasse):
        if klasse == "Slime":
            Sprite = self.slime_animation[frame]
        if klasse == "Wolf":
            Sprite = self.wolf_animation[frame]
        if klasse == "Dämon":
            Sprite = self.demon_animation[frame]
        if klasse == "Golem":
            Sprite = self.golem_animation[frame]
        return(Sprite)

    def random_spawner(self,player,chunkx,chunky):
        self.Random_Timer = self.Random_Timer + 1
        zahl = 300 - player.lvl
        if zahl < 60:
            zahl = 60
        if self.Random_Timer % zahl == 0:
            Gegner_Klassen_mit_gewichten = ["Slime","Slime","Slime","Slime","Wolf","Wolf","Wolf","Wolf","Dämon","Golem"]
            Richtungen = ["Nord","NordOst","SüdOst","Süden","Osten","SüdWest","Westen","NordWest"]
            random_enemie = MOB("Klaus",random.choice(Gegner_Klassen_mit_gewichten),9000,9000,player.pos_x + 60,player.pos_y + 60,chunkx,chunky,random.choice(Richtungen))
            self.all_enemies.append(random_enemie)

