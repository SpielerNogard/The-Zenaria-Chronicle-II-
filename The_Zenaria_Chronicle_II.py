import pygame
from pygame.locals import *
from PIL import Image
from UI import UI
import ast


from Charakter import charakter
from gameworld import gameworld
from Player_Stats import Player_Stats
from Collisionen import Collisionen
from MobController import MobController
from Quests import Quests
from Teleporting_Doors import TeleportingDoor
from Teleporting_Höhle import TeleportingHöhle
from Droptable import Droptable
from MusicController import MusicController
from XPController import XPController
from FakeDoors import FakeDoors
from Boss_Fight import Boss_Fight
from Königsszene import Königsszene
from Heilflasche import Heilflasche
from PlayerAnimator import PlayerAnimator
from Navigator import Navigator
class The_Zenaria_Chronicle_II(object):
    def __init__(self, screenwidth, screenheight, savegame_nr):
        pygame.init()
        pygame.font.init()

        self.running = True
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.gameheight = self.screenheight + 176
        self.gamewidth = self.screenwidth + 400
        self.savegame_nr = savegame_nr

        self.screen = pygame.display.set_mode((self.gamewidth,self.gameheight))
        pygame.display.set_caption("The Zenaria Chronicle II")
        self.icon = pygame.image.load("Assets/logo.png")
        self.clock = pygame.time.Clock()
        
        self.playerX_change = 0
        self.playerY_change = 0
        self.player_movement_speed = 8
        self.attack_range = 20


        self.is_Space = False
        self.enter_pressed = False
        self.Questwindow = False
        self.controll = False

        self.load_game()
        self.savegame = []
        self.loading_screen()
        self.UI = UI()
        self.stats = Player_Stats(self.screenwidth,self.screenheight,self.gameheight)
        self.colide = Collisionen()
        self.Quests = Quests()
        self.MobController = MobController()
        #spawnchunkx,spawnchunky,posx,posy,zielchunkx,zielchunky,zielposx,zielposy
        #self.door1 = TeleportingDoor(10,10,200,200,11,10,200,200)
        #self.Höhle1 = TeleportingHöhle(40,0,16*32,2*32,39,12,14*32,4*32)
        #Häuser
        #self.door1 = TeleportingDoor(10,10,32,13*32,40,4,17*32,8*32)
        self.door1 = TeleportingDoor(12,0,20*32,10*32,39,11,26*32,4*32)
        self.door2 = TeleportingDoor(10,10,11*32,7*32,39,0,15*32,14*32)
        self.door3 = TeleportingDoor(10,10,20*32,7*32,39,0,15*32,14*32)

        self.door4 = TeleportingDoor(11,10,3*32,6*32,39,1,15*32,14*32)
        self.door5 = TeleportingDoor(11,10,12*32,6*32,39,1,15*32,14*32)
        self.door6 = TeleportingDoor(11,10,24*32,8*32,39,1,15*32,14*32)

        self.door7 = TeleportingDoor(10,11,20*32,10*32,39,2,15*32,14*32)

        self.door8 = TeleportingDoor(11,11,15*32,13*32,39,3,15*32,14*32)
        self.door9 = TeleportingDoor(11,12,29*32,3*32,39,3,15*32,14*32)

        self.door9 = TeleportingDoor(12,10,10*32,5*32,40,4,17*32,8*32)

        self.door10 = TeleportingDoor(39,0,12*32,16*32,10,10,16*32,12*32)
        self.door11 = TeleportingDoor(39,1,12*32,16*32,10,10,16*32,12*32)
        self.door12 = TeleportingDoor(39,2,12*32,16*32,10,10,16*32,12*32)
        self.door13 = TeleportingDoor(39,3,12*32,16*32,10,10,16*32,12*32)
        self.door14 = TeleportingDoor(39,4,12*32,16*32,10,10,16*32,12*32)
        self.door15 = TeleportingDoor(39,5,12*32,16*32,10,10,16*32,12*32)
        self.door16 = TeleportingDoor(39,6,12*32,16*32,10,10,16*32,12*32)
        self.door16 = TeleportingDoor(39,7,12*32,16*32,10,10,16*32,12*32)
        self.door16 = TeleportingDoor(39,8,12*32,16*32,10,10,16*32,12*32)
        self.door16 = TeleportingDoor(39,9,12*32,16*32,10,10,16*32,12*32)

        self.fakedoor1 = FakeDoors(13,4,14*32,17*32,13,4,14*32,10*32)
        self.fakedoor2 = FakeDoors(15,4,16*32,17*32,15,4,16*32,10*32)
        self.fakedoor3 = FakeDoors(15,4,16*32,15*32,15,5,18*32,2*32)
        self.fakedoor4 = FakeDoors(13,4,14*32,15*32,13,5,14*32,1*32)

        self.fakedoor5 = FakeDoors(12,2,16*32,7*32,12,1,15*32,0*32)
        self.fakedoor6 = FakeDoors(12,2,15*32,3*32,12,2,15*32,10*32)

        self.Höhle1 = TeleportingHöhle(40,0,16*32,2*32,39,12,14*32,4*32)
        self.Höhle2 = TeleportingHöhle(4,6,30*32,12*32,40,4,16*32,10*32)

        self.all_Doors = [self.door1,self.Höhle1,self.Höhle2,self.door2,self.door3,self.door4,self.door5,self.door6,self.door7,self.door8,self.door9,self.door10,self.door11,self.door12,self.door13,self.door14,self.door15,self.door16,self.fakedoor1,self.fakedoor2,self.fakedoor3,self.fakedoor4,self.fakedoor5,self.fakedoor6]
        self.sounds = ["sb_vengeance.ogg","sb_jubilee.ogg","sb_wanderlust.ogg","sb_midsommar.ogg"]
        self.actual_song = 0
        self.next_song = 1
        self.Droptable = Droptable()
        self.MusicController = MusicController()
        self.XPController = XPController()
        self.Boss_Fight = Boss_Fight(39,12)
        self.Königsszene = Königsszene()
        
        self.world = gameworld()
        self.teleported = False
        self.W = False
        self.S = False
        self.A = False
        self.D = False
        self.Q = False
        self.PlayerAnimator = PlayerAnimator()
        self.Heilflasche = Heilflasche()
        self.Navigator = Navigator()
        self.play_game()

    def play_game(self):
        while self.running:
            self.screen.fill((75,105,47))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    #Player Movement
                    if event.key == pygame.K_w:
                        self.W = True
                    if event.key == pygame.K_s:
                        self.S = True
                    if event.key == pygame.K_a:
                        self.A = True
                    if event.key == pygame.K_d:
                        self.D = True
                    if event.key == pygame.K_q:
                        self.Q = True
                    
                    
                    if event.key == pygame.K_SPACE:
                        self.Questwindow = True
                        self.is_Space = True
                    if event.key == pygame.K_RETURN:
                        self.enter_pressed = True
                        
                    if event.key == pygame.K_LCTRL:
                        self.controll = True

                if event.type == pygame.KEYUP:
                    if event.key ==pygame.K_w:
                        self.W = False
                        
                    if event.key ==pygame.K_s:
                        self.S = False
                    if event.key ==pygame.K_d:
                        self.D = False
                    if event.key ==pygame.K_a:
                        self.A = False
                    if event.key == pygame.K_SPACE:
                        self.is_Space = False
                    if event.key == pygame.K_LCTRL:
                        self.controll = False
                    if event.key == pygame.K_q:
                        self.Q = False


            if self.W == False or self.S == False:
                self.playerX_change = 0
            if self.A == False or self.D == False:
                self.playerY_change = 0 

            if self.W == True:
                self.playerX_change = -self.player_movement_speed
            if self.S == True:
                self.playerX_change = self.player_movement_speed
            if self.A == True:
                self.playerY_change = -self.player_movement_speed
            if self.D == True:
                self.playerY_change = self.player_movement_speed  
            self.music_player()
            
            self.world.update_world(self.screen,self.Chunk_X,self.Chunk_Y)
            self.player_movement()
            self.check_doors()
            
            self.MobController.random_spawner(self.player,self.Chunk_X,self.Chunk_Y)
            self.MobController.enemies(self.player,self.Chunk_X,self.Chunk_Y,self.screen,self.controll)
            gestorbene_Gegner = self.MobController.gestorbene_Gegner
            Drops = self.Droptable.give_drops(gestorbene_Gegner)
            given_xp,givengold = self.XPController.Calculate_XP(gestorbene_Gegner)
            self.player.get_exp(given_xp)
            self.player.get_gold(givengold)
            self.Quests.Give_Drops_to_Quest(Drops)
            self.Quests.check_spawn(self.Chunk_X,self.Chunk_Y,self.screen,self.player.pos_x,self.player.pos_y,self.player,self.Questwindow,self.enter_pressed)
            self.stats.draw_stats(self.player,self.screen,self.Chunk_X,self.Chunk_Y)
            self.Heilflasche.drink_Flasche(self.player,self.Q,self.screen)
            self.Quests.Quest_Stats(self.screen,self.screenwidth,self.gameheight)
            self.Questwindow = self.Quests.Questwindow
            self.enter_pressed = False
            self.Navigiere_mich()
            self.Königsszene.start_Scene(self.screen,self.Chunk_X,self.Chunk_Y)
            test = self.Königsszene.activate_questes()
            if test == True:
                if self.teleported == False:
                    self.Quests.activate_this_quest("Die Dämonen")
                    self.Chunk_X = 12
                    self.Chunk_Y = 0
                    self.player.teleport_player(16*32,15*32)
                    self.teleported = True

            self.Boss_Fight.fight(self.screen,self.player,self.Chunk_X,self.Chunk_Y,self.controll)
            
            #print("Sie haben gerade "+str(int(self.clock.get_fps()))+" fps") 
            self.clock.tick(30)
            pygame.display.update()

    def loading_screen(self):
        self.logowidth = 780
        self.logoheight = 563
        self.logoplacement_width = int((self.gamewidth-self.logowidth)/2)
        self.logoplacement_heigth = int((self.gameheight-self.logoheight)/2)
        self.real_logoplacement_height = int(self.logoplacement_heigth - 10)
        self.myfont = pygame.font.SysFont('Arial', 50)
        self.icon = pygame.image.load('Assets\logo.png')
        self.screen.blit(self.icon,(self.logoplacement_width,self.real_logoplacement_height))
        self.White = (255, 255, 255)
        Loading_Text = self.myfont.render('Loading World: Please wait ......', False, (255, 255, 255))
        self.screen.blit(Loading_Text,(0,0))
        print("Loading screen gezeichnet")
        pygame.display.update()


    def music_player(self):
        self.MusicController.check_music(self.Chunk_X,self.Chunk_Y)
        self.next_song = self.MusicController.music
        if self.actual_song != self.next_song:
            self.actual_song = self.next_song
            pygame.mixer.music.load(self.sounds[self.actual_song])
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
    def player_movement(self):
        actual_chunk = self.world.give_me_my_chunk(self.Chunk_X,self.Chunk_Y)
        self.playerX_change,self.playerY_change = self.colide.check_Collisions(self.player.pos_x,self.player.pos_y,self.playerX_change,self.playerY_change,actual_chunk)
        playerx,playery = self.player.move(self.playerY_change,self.playerX_change)
        if playerx < 0:
            self.Chunk_X = self.Chunk_X - 1
            self.player.move( self.screenwidth - 1, 0)
            if self.Chunk_X < 0 :
                self.Chunk_X = 0
        if playerx > self.screenwidth:
            self.Chunk_X = self.Chunk_X + 1
            self.player.move(- self.screenwidth + 1 , 0)
            
        if playery < 0:
            self.Chunk_Y = self.Chunk_Y - 1
            self.player.move(0 , self.screenheight-1)
            if self.Chunk_Y < 0 :
                self.Chunk_Y = 0
        if playery > self.screenheight:
            self.Chunk_Y = self.Chunk_Y + 1
            self.player.move(0, - self.screenheight + 1 )
        self.check_teleport_player()
        PlayerIMG = self.PlayerAnimator.animate_player(self.W,self.A,self.S,self.D,self.controll)
        self.screen.blit(PlayerIMG,(playerx,playery))
    def load_game(self):
        SavegameName = "Savegames/savegame_"+str(self.savegame_nr)+".txt"
        self.actual_savegame = open(SavegameName).read()
        self.actual_savegame = ast.literal_eval(self.actual_savegame)
        self.Chunk_X = self.actual_savegame[0]
        self.Chunk_Y = self.actual_savegame[1]
        self.playerImg_string = self.actual_savegame[2]
        self.playerImg = pygame.image.load(self.playerImg_string)

        player_name = self.actual_savegame[4]
        player_pos_x  = self.actual_savegame[5]
        player_pos_y = self.actual_savegame[6]
        player_current_health = self.actual_savegame[7]
        player_current_mana = self.actual_savegame[8]
        player_max_health = self.actual_savegame[9]
        player_max_mana = self.actual_savegame[10]
        player_gold = self.actual_savegame[11]
        player_exp = self.actual_savegame[12]
        player_all_exp = self.actual_savegame[13]
        player_strenght = self.actual_savegame[14]
        player_lvl = self.actual_savegame[15]
        player_classe = self.actual_savegame[16]

        self.player = charakter(player_name,player_current_health,player_current_mana,player_gold,player_lvl,player_classe,player_pos_x,player_pos_y,player_max_health,player_max_health,player_all_exp,player_exp,player_strenght)

    def check_doors(self):
        for a in self.all_Doors:
            chunkx,chunky,posx,posy = a.check_teleport(self.player.pos_x,self.player.pos_y,self.Chunk_X,self.Chunk_Y,self.screen)
            self.Chunk_X = chunkx
            self.Chunk_Y = chunky
            self.player.teleport_player(posx,posy)
    
    def check_teleport_player(self):
        if self.player.need_teleport == True:
            if self.Chunk_X == 39 and self.Chunk_Y == 12:
                self.Chunk_X = 40
                self.Chunk_Y = 1
                self.player.teleport_player(26*32,4*32)
            
            else:
                self.Chunk_X = 10
                self.Chunk_Y = 10
                self.player.teleport_player(19*32,4*32)

        self.player.revived()
    
    def Navigiere_mich(self):
        x,y = self.Quests.give_goal()
        #print(str(x)+" "+str(y))
        self.Navigator.navigiere(self.screen,self.Chunk_X,self.Chunk_Y,x,y)


#GAME = The_Zenaria_Chronicle_II(1024,576,1)