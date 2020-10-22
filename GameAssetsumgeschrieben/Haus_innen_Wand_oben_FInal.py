import pygame


class Haus_innen_Wand_oben_FInal(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Haus_innen_Wand_oben_FInal.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))




        
