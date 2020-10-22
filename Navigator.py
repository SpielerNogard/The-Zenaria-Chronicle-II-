import pygame

class Navigator(object):
    def __init__(self):
        self.Pfeil_oben = pygame.image.load("Assets/Pfeil_oben.png")
        self.Pfeil_unten = pygame.image.load("Assets/Pfeil_unten.png")
        self.Pfeil_rechts = pygame.image.load("Assets/Pfeil_rechts.png")
        self.Pfeil_links = pygame.image.load("Assets/Pfeil_links.png")

        self.Pfeil_oben_links = pygame.image.load("Assets/Pfeil_oben_links.png")
        self.Pfeil_oben_rechts = pygame.image.load("Assets/Pfeil_oben_rechts.png")
        self.Pfeil_unten_links = pygame.image.load("Assets/Pfeil_unten_links.png")
        self.Pfeil_unten_rechts = pygame.image.load("Assets/Pfeil_unten_rechts.png")

        self.nichts = pygame.image.load("Assets/Durchsichtig.png")

        self.IMG = self.nichts


    def navigiere(self,screen,actual_chunkx,actual_chunky,zielx,ziely):
        
        if zielx != 9999 and zielx != 9999:
            if actual_chunkx < zielx and actual_chunky < ziely:
                self.IMG = self.Pfeil_unten_rechts

            elif actual_chunkx > zielx and actual_chunky < ziely:
                self.IMG = self.Pfeil_unten_links

            elif actual_chunkx < zielx and actual_chunky > ziely:
                self.IMG = self.Pfeil_oben_rechts

            elif actual_chunkx > zielx and actual_chunky > ziely:
                self.Pfeil_oben_links

            elif actual_chunkx < zielx:
                self.IMG = self.Pfeil_rechts

            elif actual_chunkx > zielx:
                self.IMG = self.Pfeil_links

            elif actual_chunky < ziely:
                self.IMG = self.Pfeil_unten

            elif actual_chunky > ziely:
                self.IMG = self.Pfeil_oben

            else:
                self.IMG = self.nichts

        if zielx == 9999 and ziely == 9999:
            self.IMG = self.nichts
        screen.blit(self.IMG,(480,20))

