import pygame

from pygame.locals import *
from Chunkloader2 import Chunk

import ast
from The_Zenaria_Chronicle_II import The_Zenaria_Chronicle_II
import pygame as pg

class InputBox:
    
    def __init__(self, x, y, w, h, text=''):
        FONT = pg.font.SysFont("Arial", 32)
        COLOR_INACTIVE = pg.Color('lightskyblue3')
        COLOR_ACTIVE = pg.Color('dodgerblue2')
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self,event):
        FONT = pg.font.SysFont("Arial", 32)
        COLOR_INACTIVE = pg.Color('lightskyblue3')
        COLOR_ACTIVE = pg.Color('dodgerblue2')
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


class Launcher(object):
    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.StandartAssets=['StandartAssets/Brucke.png','StandartAssets/Gras.png','StandartAssets/laubbaum_1.png','StandartAssets/Laubbaum_2.png','StandartAssets/Laubbaum_3.png','StandartAssets/Schild.png','StandartAssets/Stein.png','StandartAssets/Water_Sea_frame_1.png','StandartAssets/Water_Sea_frame_2.png','StandartAssets/Water_Sea_frame_3.png','StandartAssets/Water_Fluss_frame_1.png','StandartAssets/Water_Fluss_frame_2.png','StandartAssets/Water_Fluss_frame_3.png','StandartAssets/Water_Fluss_frame_4.png','StandartAssets/Water_Fluss_frame_5.png','StandartAssets/Water_Fluss_frame_6.png','StandartAssets/Gras.png','StandartAssets/Durchsichtig.png']
        self.Chunk_X = 99
        self.Chunk_Y = 99
        self.screenwidth = 1024
        self.screenheight = 576

        self.logowidth = 780
        self.logoheight = 563
        self.logoplacement_width = int((self.screenwidth-self.logowidth)/2)
        self.logoplacement_heigth = int((self.screenheight-self.logoheight)/2)
        self.real_logoplacement_height = int(self.logoplacement_heigth - 10)

        self.text1_width = 20
        self.text1_height = self.screenheight -32-20
        #Buttons
        self.play_button_width_dimension = 200
        self.play_button_height_dimension = 100
        self.play_button_heigth = self.screenheight - 120
        self.play_button_width = int((self.screenwidth-self.play_button_width_dimension)/2)
        self.play_button = pygame.Rect((self.play_button_width,self.play_button_heigth),(self.play_button_width_dimension,self.play_button_height_dimension))

        self.playbuttontext_height = self.play_button_heigth+32
        self.playbuttontext_width = self.play_button_width+10

        

        self.font1 = pygame.font.SysFont('Arial',32)
        self.font2 = pygame.font.SysFont('Arial', 35)
        self.screen = pygame.display.set_mode((self.screenwidth,self.screenheight))
        pygame.display.set_caption("The Zenaria Launcher")
        self.icon = pygame.image.load('Assets\logo.png')
        pygame.display.set_icon(self.icon)

        self.running = True
        self.Chunk2 = Chunk(self.screenwidth,self.screenheight)
        self.Current_Chunk2 = self.Chunk2.load_chunk(99,99)
        
        self.Brucke = pygame.image.load('Assets/Brucke.png')
        self.Gras = pygame.image.load('Assets/Gras.png')
        self.Laubbaum1 = pygame.image.load('Assets/laubbaum_1.png')
        self.Laubbaum2 = pygame.image.load('Assets/Laubbaum_2.png')
        self.Laubbaum3 = pygame.image.load('Assets/Laubbaum_3.png')
        self.Schild = pygame.image.load('Assets/Schild.png')
        self.Stein = pygame.image.load('Assets/Stein.png')
        self.Wasser_Ozean0 = pygame.image.load('Assets/Water_Sea_frame_1.png')
        self.Wasser_Ozean1 = pygame.image.load('Assets/Water_Sea_frame_2.png')
        self.Wasser_Ozean2 = pygame.image.load('Assets/Water_Sea_frame_3.png')
        self.Gras_Küste = pygame.image.load('Assets/Gras.png')
        self.Durchsichtig = pygame.image.load('Assets/Durchsichtig.png')
        self.Wasser_Fluss0 = pygame.image.load('Assets/Water_Fluss_frame_1.png')
        self.Wasser_Fluss1 = pygame.image.load('Assets/Water_Fluss_frame_2.png')
        self.Wasser_Fluss2 = pygame.image.load('Assets/Water_Fluss_frame_3.png')
        self.Wasser_Fluss3 = pygame.image.load('Assets/Water_Fluss_frame_4.png')
        self.Wasser_Fluss4 = pygame.image.load('Assets/Water_Fluss_frame_5.png')
        self.Wasser_Fluss5 = pygame.image.load('Assets/Water_Fluss_frame_6.png')
        self.Laubbaum1 = pygame.image.load('Assets/laubbaum_1.png')
        self.Laubbaum2 = pygame.image.load('Assets/Laubbaum_2.png')
        self.Laubbaum3 = pygame.image.load('Assets/Laubbaum_3.png')
        self.Assets= [self.Brucke,self.Gras,self.Laubbaum1,self.Laubbaum2,self.Laubbaum3,self.Schild,self.Stein]
        self.Wateranmiationtimer = 0
        self.Flussanimationtimer = 0
        self.anpassung = 0
        self.clicked = False
        self.Fenster = "Launcher"
        self.savegame_nr = 0
        self.savegame_button_action1 = "leer"
        self.savegame_button_action2 = "leer"
        self.savegame_button_action3 = "leer"
        self.ausgewählte_Klasse = ""
        self.textinput = InputBox(self.screenwidth-510,10,500,100,"")
    
    

    def fill_Background(self):
        screenwidth = self.screenwidth
        screenheight = self.screenheight
        Gras = self.Assets[1]
        while screenwidth > -32:
            
            while screenheight > -32:
                self.screen.blit(Gras,(screenwidth,screenheight))
                screenheight = screenheight - 32
            screenwidth = screenwidth-32
            screenheight = self.screenheight
    def load_new_chunk2(self):
        self.fill_Background()
        Current_Chunk = self.Chunk2.load_chunk(self.Chunk_X,self.Chunk_Y)
        #print("Derzeitiger Chunk: "+str(self.Chunk_X)+" / "+str(self.Chunk_Y))
        #print(Current_Chunk)
        i = 0
        j = -1
        for a in Current_Chunk:
                #print(a)
                j = j+1
                if j == 18:
                    i = i+1
                    j = 0
                Gegenstand = a[0]
                Gegenstand_x = int(a[1])
                #print("Gegenstand_x "+str(Gegenstand_x))
                Gegenstand_y = int(a[2])
                #print("Gegenstand_y "+str(Gegenstand_y))
                if Gegenstand_x != 0:
                    Gegenstand_x = Gegenstand_x + self.anpassung*i
                if Gegenstand_y == 0:
                    Gegenstand_y = Gegenstand_y 
                else:
                    Gegenstand_y = Gegenstand_y + self.anpassung*j
                Gegenstand = str(Gegenstand)
                #print("Gegenstand_x nach anpassung "+str(Gegenstand_x))
                #print("Gegenstand_y nach anpassung "+str(Gegenstand_y))
                #print(Gegenstand)
                if Gegenstand == "Wasser_Ozean" and self.Wateranmiationtimer <=10:
                    Gegenstand = self.Wasser_Ozean0
                    self.Wateranmiationtimer = self.Wateranmiationtimer + 1
                elif Gegenstand == "Wasser_Ozean" and self.Wateranmiationtimer  <=20:
                    Gegenstand = self.Wasser_Ozean1
                    self.Wateranmiationtimer = self.Wateranmiationtimer+1
                elif Gegenstand == "Wasser_Ozean" and self.Wateranmiationtimer <= 30:
                    Gegenstand = self.Wasser_Ozean2
                    self.Wateranmiationtimer = self.Wateranmiationtimer + 1
                    if self.Wateranmiationtimer == 30:
                        self.Wateranmiationtimer = 0
                elif Gegenstand == "Gras_Kuste":
                    Gegenstand = self.Gras
                if Gegenstand == "Wasser_Fluss" and self.Flussanimationtimer <= 10:
                    Gegenstand = self.Wasser_Fluss0
                    self.Flussanimationtimer = self.Flussanimationtimer+1
                if Gegenstand == "Wasser_Fluss" and self.Flussanimationtimer <= 20:
                    Gegenstand = self.Wasser_Fluss1
                    self.Flussanimationtimer = self.Flussanimationtimer+1
                if Gegenstand == "Wasser_Fluss" and self.Flussanimationtimer <= 30:
                    Gegenstand = self.Wasser_Fluss2
                    self.Flussanimationtimer = self.Flussanimationtimer+1
                if Gegenstand == "Wasser_Fluss" and self.Flussanimationtimer <= 40:
                    Gegenstand = self.Wasser_Fluss3
                    self.Flussanimationtimer = self.Flussanimationtimer+1
                if Gegenstand == "Wasser_Fluss" and self.Flussanimationtimer <= 50:
                    Gegenstand = self.Wasser_Fluss4
                    self.Flussanimationtimer = self.Flussanimationtimer+1
                if Gegenstand == "Wasser_Fluss" and self.Flussanimationtimer <= 60:
                    Gegenstand = self.Wasser_Fluss5
                    self.Flussanimationtimer = self.Flussanimationtimer+1
                    if self.Flussanimationtimer == 60:
                        self.Flussanimationtimer = 0
                if Gegenstand == "Wald_Laub":
                    Gegenstand = self.Laubbaum1
                self.screen.blit(Gegenstand,(Gegenstand_x,Gegenstand_y))
    
    #draws your text on the wished surface
    def draw_text(self,text, font, color,surface, x,y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj, textrect)

    def paint_logo(self):
        self.screen.blit(self.icon,(self.logoplacement_width,self.real_logoplacement_height))
    
    def paint_play_button(self):
        UPTODATEORANGE = (255,127,36)
        WHITE = (0,0,0)
        pygame.draw.rect(self.screen,UPTODATEORANGE, self.play_button) 
        self.draw_text('Play Game',self.font2, WHITE, self.screen,self.playbuttontext_width ,self.playbuttontext_height )

    def savegames_editor(self):
        self.screen.fill((0,0,0))
        self.load_new_chunk2()
        GREY = (153, 153, 102)
        WHITE = (255,255,255)
        font2 = pygame.font.SysFont('Arial', 15)
        font3 = pygame.font.SysFont('Arial', 30)
        savegameheight = int((self.screenheight-40)/3)
        savegamewidth = int(self.screenwidth/3)
        savegame1 = pygame.Rect((10,10),(savegamewidth,savegameheight))
        savegame2 = pygame.Rect((10,savegameheight+20),(savegamewidth,savegameheight))
        savegame3 = pygame.Rect((10,2*savegameheight+30),(savegamewidth,savegameheight))
        pygame.draw.rect(self.screen, GREY, savegame1)
        pygame.draw.rect(self.screen, GREY, savegame2)
        pygame.draw.rect(self.screen, GREY, savegame3)
        self.actual_Savegame1 = open("Savegames/savegame_1.txt").read()
        self.actual_Savegame2 = open("Savegames/savegame_2.txt").read()
        self.actual_Savegame3 = open("Savegames/savegame_3.txt").read()
        self.button = pygame.Rect((savegamewidth+50,self.screenheight-110),(300,100))
        if self.actual_Savegame1 != "":
                self.actual_Savegame1 = ast.literal_eval(self.actual_Savegame1)
                actualSavegame1text = "Savegame vorhanden"
                self.savegame_button_action1 = "Laden"
        else:
            actualSavegame1text = "leeres Savegame"
            self.savegame_button_action1 = "Neu"
        self.draw_text(actualSavegame1text,font2, WHITE,self.screen, 12, int(savegameheight+10-20) )
        if self.actual_Savegame2 != "":
                self.actual_Savegame2 = ast.literal_eval(self.actual_Savegame2)
                actualSavegame2text = "Savegame vorhanden"
                self.savegame_button_action2 = "Laden"
        else:
            actualSavegame2text = "leeres Savegame"
            self.savegame_button_action2 = "Neu"
        self.draw_text(actualSavegame2text,font2, WHITE,self.screen, 12, int(2*savegameheight+20-20) )
        if self.actual_Savegame3 != "":
                self.actual_Savegame3 = ast.literal_eval(self.actual_Savegame3)
                actualSavegame3text = "Savegame vorhanden"
                self.savegame_button_action3 = "Laden"
        else:
            actualSavegame3text = "leeres Savegame"
            self.savegame_button_action3 = "Neu"
        self.draw_text(actualSavegame3text,font2, WHITE,self.screen, 12, int(3*savegameheight+30-20) )
        self.draw_text("Savegame 1",font3, WHITE,self.screen, 12, 12 )
        self.draw_text("Savegame 2",font3, WHITE,self.screen, 12, savegameheight+22 )
        self.draw_text("Savegame 3",font3, WHITE,self.screen, 12, 2*savegameheight+32 )
        if savegame1.collidepoint((self.mx,self.my)):
            if self.clicked == True:
               #print("Savegame1")
               self.savegame_nr = 1
        if savegame2.collidepoint((self.mx,self.my)):
            if self.clicked == True:
               #print("Savegame2")
               self.savegame_nr = 2
        if savegame3.collidepoint((self.mx,self.my)):
            if self.clicked == True:
               #print("Savegame3")
               self.savegame_nr = 3
        #savegamestats = pygame.Rect((self.screenwidth-10-savegamewidth,10),(savegamewidth,2.5*savegameheight))
        #pygame.draw.rect(self.screen, GREY, savegamestats)

        if self.savegame_nr == 1 and self.savegame_button_action1 == "Laden":
            playername = self.actual_Savegame1[4]
            player_current_health = self.actual_Savegame1[7]
            player_current_mana = self.actual_Savegame1[8]
            player_max_health = self.actual_Savegame1[9]
            player_max_mana = self.actual_Savegame1[10]
            player_gold = self.actual_Savegame1[11]
            player_exp = self.actual_Savegame1[12]
            player_all_exp = self.actual_Savegame1[13]
            player_strenght = self.actual_Savegame1[14]
            player_lvl = self.actual_Savegame1[15]
            player_klasse = self.actual_Savegame1[16]

        elif self.savegame_nr == 2 and self.savegame_button_action2 == "Laden":
            playername = self.actual_Savegame2[4]
            player_current_health = self.actual_Savegame2[7]
            player_current_mana = self.actual_Savegame2[8]
            player_max_health = self.actual_Savegame2[9]
            player_max_mana = self.actual_Savegame2[10]
            player_gold = self.actual_Savegame2[11]
            player_exp = self.actual_Savegame2[12]
            player_all_exp = self.actual_Savegame2[13]
            player_strenght = self.actual_Savegame2[14]
            player_lvl = self.actual_Savegame2[15]
            player_klasse = self.actual_Savegame2[16]

        elif self.savegame_nr == 3 and self.savegame_button_action3 == "Laden":
            playername = self.actual_Savegame3[4]
            player_current_health = self.actual_Savegame3[7]
            player_current_mana = self.actual_Savegame3[8]
            player_max_health = self.actual_Savegame3[9]
            player_max_mana = self.actual_Savegame3[10]
            player_gold = self.actual_Savegame3[11]
            player_exp = self.actual_Savegame3[12]
            player_all_exp = self.actual_Savegame3[13]
            player_strenght = self.actual_Savegame3[14]
            player_lvl = self.actual_Savegame3[15]
            player_klasse = self.actual_Savegame3[16]

        else:
            playername = ""
            player_current_health =""
            player_current_mana = ""
            player_max_health = ""
            player_max_mana = ""
            player_gold = ""
            player_exp = ""
            player_all_exp = ""
            player_strenght = ""
            player_lvl = ""
            player_klasse = ""
        if playername != "":
            savegamestats = pygame.Rect((self.screenwidth-10-savegamewidth,10),(savegamewidth,int(2.5*savegameheight)))
            pygame.draw.rect(self.screen, GREY, savegamestats)
            self.draw_text("Charaktername: "+str(playername),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,12)
            self.draw_text("Maximales Leben: "+str(player_max_health),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,30)
            self.draw_text("aktuelles Leben: "+str(player_current_health),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,48)
            self.draw_text("Maximales Mana: "+str(player_max_mana),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,66)
            self.draw_text("aktuelles Mana: "+str(player_current_mana),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,84)
            self.draw_text("Gold: "+str(player_gold),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,102)
            self.draw_text("Stärke: "+str(player_strenght),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,120)
            self.draw_text("LVL: "+str(player_lvl),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,138)
            self.draw_text("insgesamt XP: "+str(player_all_exp),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,156)
            self.draw_text("insgesamt XP LVL : "+str(player_exp),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,174)
            self.draw_text("Klasse: "+str(player_klasse),font2, WHITE,self.screen, self.screenwidth-10-savegamewidth,192)
            
            pygame.draw.rect(self.screen, GREY, self.button)
            self.draw_text("Load Savegame",font3, WHITE,self.screen, savegamewidth+80,self.screenheight-70)

        elif self.savegame_nr != 0 and playername == "" :
            
            pygame.draw.rect(self.screen, GREY, self.button)
            self.draw_text("New Game",font3, WHITE,self.screen, savegamewidth+80,self.screenheight-70)

        if self.button.collidepoint((self.mx,self.my)) and playername != "" and self.savegame_nr != 0:
            if self.clicked == True:
               #print("WHY?")
               GAME = The_Zenaria_Chronicle_II(1024,576,self.savegame_nr)
               self.running = False
        if self.button.collidepoint((self.mx,self.my)) and playername == "" and self.savegame_nr != 0:
            if self.clicked == True:
               self.Fenster = "New Savegame"
               
    def new_savegame(self):
        
        self.screen.fill((0,0,0))
        self.load_new_chunk2()
        GREY = (153, 153, 102)
        WHITE = (255,255,255)
        font2 = pygame.font.SysFont('Arial', 15)
        font3 = pygame.font.SysFont('Arial', 30)
        savegameheight = int((self.screenheight-40)/3)
        savegamewidth = int(self.screenwidth/3)
        savegame1 = pygame.Rect((10,10),(savegamewidth,savegameheight))
        savegame2 = pygame.Rect((10,savegameheight+20),(savegamewidth,savegameheight))
        savegame3 = pygame.Rect((10,2*savegameheight+30),(savegamewidth,savegameheight))
        pygame.draw.rect(self.screen, GREY, savegame1)
        pygame.draw.rect(self.screen, GREY, savegame2)
        pygame.draw.rect(self.screen, GREY, savegame3)
        self.draw_text("Krieger",font3, WHITE,self.screen, 12, 12 )
        self.draw_text("Barbar",font3, WHITE,self.screen, 12, savegameheight+22 )
        self.draw_text("Mönch/Paladin",font3, WHITE,self.screen, 12, 2*savegameheight+32 )
        self.draw_text("Bald verfügbar",font2, WHITE,self.screen, 12, int(2*savegameheight+20-20) )
        self.draw_text("Bald verfügbar",font2, WHITE,self.screen, 12, int(3*savegameheight+30-20) )
        if savegame1.collidepoint((self.mx,self.my)):
            if self.clicked == True:
               #print("Savegame1")
               self.ausgewählte_Klasse = "Krieger"
        if savegame2.collidepoint((self.mx,self.my)):
            if self.clicked == True:
               #print("Savegame2")
               self.ausgewählte_Klasse = "Krieger"
        if savegame3.collidepoint((self.mx,self.my)):
            if self.clicked == True:
               #print("Savegame3")
               self.ausgewählte_Klasse = "Krieger"
        pygame.draw.rect(self.screen, GREY, self.button)
        self.draw_text("Start Game",font3, WHITE,self.screen, savegamewidth+80,self.screenheight-70)
        self.textinput.draw(self.screen)
        #self.textinput.handle_event()
        if self.button.collidepoint((self.mx,self.my)) and self.ausgewählte_Klasse != "":
            if self.clicked == True:
               #print("WHY?")
               self.save()
               GAME = The_Zenaria_Chronicle_II(1024,576,self.savegame_nr)
               self.running = False
               
    def save(self):
        self.savegame = []
        active_quests = []
        self.savegame.append(10)
        self.savegame.append(10)
        self.savegame.append("Assets/player.jpg")
        self.savegame.append(active_quests)
        self.savegame.append(self.textinput.text)
        self.savegame.append(20*32)
        self.savegame.append(13*32)
        self.savegame.append(100)
        self.savegame.append(100)
        self.savegame.append(100)
        self.savegame.append(100)
        self.savegame.append(0)
        self.savegame.append(0)
        self.savegame.append(0)
        self.savegame.append(1)
        self.savegame.append(0)
        self.savegame.append(self.ausgewählte_Klasse)
        print(self.savegame)
        datei = open('Savegames/savegame_'+str(self.savegame_nr)+'.txt','a')
        datei.write(str(self.savegame))
    def play(self):

        while self.running == True:
            self.mx,self.my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                self.textinput.handle_event(event)
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicked = False
            if self.Fenster =="Launcher":
                self.load_new_chunk2()
                self.paint_logo()
                self.paint_play_button()
                if self.play_button.collidepoint((self.mx,self.my)):
                    if self.clicked == True:
                        print("Game started")
                        self.Fenster = "Savegames"
            if self.Fenster == "Savegames":
                self.savegames_editor()
            if self.Fenster == "New Savegame":
                self.new_savegame()
            pygame.display.update()
Launcher = Launcher()
Launcher.play()
