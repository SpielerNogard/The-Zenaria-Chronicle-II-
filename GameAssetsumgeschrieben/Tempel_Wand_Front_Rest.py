import pygame


class Tempel_Wand_Front_Rest(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Tempel Wand Front Rest.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))




        
