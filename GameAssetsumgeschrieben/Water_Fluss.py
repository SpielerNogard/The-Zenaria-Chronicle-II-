import pygame
import itertools

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




        
