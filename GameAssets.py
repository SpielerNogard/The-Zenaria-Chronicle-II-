import pygame
import itertools

class Altar(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Altare.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Bergwand(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Bergwand_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Bergweg_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Bergweg_oben_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Bergweg_unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Bergweg_unten_finale.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Bergweg_Zenter(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Bergweg_Zenter_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Brucke(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Brucke.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))
class Dirt_Weg(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Dirt_weg.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Door1(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/door1.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Door2(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/door2.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Door3(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/door3.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Door4(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/door4.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Dummy(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Dummy_Try_2.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Durchsichtig(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Durchsichtig.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Exclamation_Mark(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/exclamationmark.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Fackel(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Fackel.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Firtree(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/firtree-Sheet.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class fountain(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/fountain-Sheet.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Grass(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Gras.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_innen_Wand_Ecke_links_oben_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_Ecke_links_oben_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_innen_Wand_Ecke_links_unten_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_Ecke_links_unten_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_innen_Wand_Ecke_recht_unten_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_Ecke_recht_unten_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_innen_Wand_Ecke_rechts_oben_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_Ecke_rechts_oben_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_innen_Wand_links_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_links_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))
class Haus_innen_Wand_oben_FInal(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_oben_FInal.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_innen_Wand_rechts_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_rechts_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Haus_innen_Wand_unten_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_unten_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Haus_Wand_Visible__Front__Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_Wand_Visible__Front__Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Höhleneingang(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Höhleneingang_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class House1(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/house1.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class House2(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/house2.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class House3(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/house3.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class House4(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/house4.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Boden(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Boden.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast_Wand_Ecke_Links_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand Ecke links oben.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Wand_Ecke_Links_Unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand Ecke links unten.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

     
class Palast_Wand_Ecke_Rechts_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand Ecke rechts oben.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Wand_Ecke_Rechts_Unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand Ecke rechts unten.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Wand_Front_Rest(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand Front Rest.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast_Wand_Front_Verbindung_Zum_Boden(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast wand front Verbindung zum Boden.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast_Wand_Links(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast wand links.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Wand_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand Oben.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast_Wand_Rechts(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand rechts.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast_Wand_unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast Wand unten.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast_außen_Palast.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Tor(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast_außen_Tor.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Treppe(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast_außen_Treppe.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Palast_Wand(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast_außen_Wand_Basis.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Palast_Wand_Top(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Palast_außen_Wand_Top.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))
    
class questboard(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/questboard.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class QuestionMark(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/questionmark.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Regal_Final_(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Regal_Final_.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Sand(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Sand.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Schild(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Schild.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Schwarzes_Rechteck(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/SchwarzRechteck.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class StatdtWeg(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Stadt_weg.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))



class Stein(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Stein.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Stuhl_Final_links_schauend(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Stuhl_Final_links_schauend.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Stuhl_Final_rechts_schauend(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Stuhl_Final_rechts_schauend.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Boden(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Boden.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Tempel_Wand_Ecke_Links_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Ecke links oben.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))



class Tempel_Wand_Ecke_Links_Unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Ecke links unten.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Wand_Ecke_Rechts_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Ecke rechts oben.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Wand_Ecke_Rechts_Unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Ecke rechts unten.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Wand_Front_Rest(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Front Rest.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Wand_Front_Verbindung_Zum_Boden(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel wand front Verbindung zum Boden.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Wand_Links(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Links.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tempel_Wand_Oben(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Oben.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Tempel_Wand_Rechts(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Rechts.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Tempel_Wand_Unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Unten.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))


class Temple(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/TempleOutside.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tisch_Final(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tisch_Final.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Tree(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/laubbaum_1.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))



class Water_Fluss(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Water_Fluss_frame_1.png")
        self.IMG2 = pygame.image.load("Assets/Water_Fluss_frame_2.png")
        self.IMG3 = pygame.image.load("Assets/Water_Fluss_frame_3.png")
        self.IMG4 = pygame.image.load("Assets/Water_Fluss_frame_4.png")
        self.IMG5 = pygame.image.load("Assets/Water_Fluss_frame_5.png")
        self.IMG6 = pygame.image.load("Assets/Water_Fluss_frame_6.png")
        


        self.dauer_der_frames = 5
        self.animationtimer = 0
        self.animate_cycle = [self.IMG1,self.IMG2,self.IMG3,self.IMG4,self.IMG5,self.IMG6]

        self.cycle = itertools.cycle(self.animate_cycle)
        self.actual_image = self.IMG1
        next(self.cycle)

    def paint(self,screen,pos_x,pos_y):
        self.animationtimer = self.animationtimer + 1
        if self.animationtimer == self.dauer_der_frames:
            self.animationtimer = 0
            self.actual_image = next(self.cycle)
        screen.blit(self.actual_image,(pos_x,pos_y))
        
class Water_Sea(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Water_Sea_frame_1.png")
        self.IMG2 = pygame.image.load("Assets/Water_Sea_frame_2.png")
        self.IMG3 = pygame.image.load("Assets/Water_Sea_frame_3.png")
        self.dauer_der_frames = 5
        self.animationtimer = 0
        self.animate_cycle = [self.IMG1,self.IMG2,self.IMG3]

        self.cycle = itertools.cycle(self.animate_cycle)
        self.actual_image = self.IMG1
        next(self.cycle)

    def paint(self,screen,pos_x,pos_y):
        self.animationtimer = self.animationtimer + 1
        if self.animationtimer == self.dauer_der_frames:
            self.animationtimer = 0
            self.actual_image = next(self.cycle)
        screen.blit(self.actual_image,(pos_x,pos_y))

class Zaun(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Zaun_fertig.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class cave_bottommiddle(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/cave_bottommiddle.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class Cave_floor(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Cave_floor.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class cave_leftwall(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/cave_leftwall.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class cave_topmiddle(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/cave_topmiddle.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))

class cave_rightwall(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/cave_rightwall.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))
    





        









        



