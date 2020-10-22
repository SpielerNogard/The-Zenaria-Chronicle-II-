import pygame
import random

class TeleportingDoor(object):
    def __init__(self,spawnchunkx,spawnchunky,posx,posy,zielchunkx,zielchunky,zielposx,zielposy):
        self.spawnchunkx = spawnchunkx
        self.spawnchunky = spawnchunky

        self.spawnposx = posx
        self.spawnposy = posy

        self.posx = -9000
        self.posy = -9000

        self.zielchunkx = zielchunkx
        self.zielchunky = zielchunky

        self.zielposx = zielposx
        self.zielposy = zielposy

        self.door1 = pygame.image.load("Assets/door1.png")
        self.door2 = pygame.image.load("Assets/door2.png")
        self.door3 = pygame.image.load("Assets/door3.png")
        self.door4 = pygame.image.load("Assets/door4.png")

        self.all_doors= [self.door1,self.door2,self.door3,self.door4]

        self.image = random.choice(self.all_doors)
        self.teleporting_range = 64

        self.chunkx = 0
        self.chunky = 0


    def check_teleport(self,playerposx,playerposy,chunkx,chunky,screen):
        self.chunkx = chunkx
        self.chunky = chunky
        self.playerposx = playerposx
        self.playerposy = playerposy
        if self.spawnchunkx == chunkx and self.spawnchunky == chunky:
            self.posx = self.spawnposx
            self.posy = self.spawnposy
        else:
            self.posx = -9000
            self.posy = -9000
        screen.blit(self.image,(self.posx,self.posy))
        Abstand_x = abs(self.posx - playerposx)
        Abstand_y = abs(self.posy - playerposy)
        #print("Abstand X: "+str(Abstand_x))
        #print("Abstand Y: "+str(Abstand_y))
        if Abstand_x <= self.teleporting_range and Abstand_y <= self.teleporting_range:
            self.chunkx = self.zielchunkx
            self.chunky = self.zielchunky
            self.playerposx = self.zielposx
            self.playerposy = self.zielposy
            print("Player teleportiert")

        return(self.chunkx,self.chunky,self.playerposx,self.playerposy)

