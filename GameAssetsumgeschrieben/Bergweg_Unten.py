import pygame


class Bergweg_unten(object):
    def __init__(self):
        self.IMG1 = pygame.image.load("Assets/Bergweg_unten_finale.png")
        self.actual_image = self.IMG1
        

    def paint(self,screen,pos_x,pos_y):
        screen.blit(self.actual_image,(pos_x,pos_y))




        
