import pygame


class Heilflasche(object):
    def __init__(self):
        self.activated = False
        self.timer = 0
        self.cooldown = 300
        self.IMG = pygame.image.load("Assets/Health_pot.png")
        self.myfont = pygame.font.SysFont('Arial', 20)

    def drink_Flasche(self,player,q,screen):
        screen.blit(self.IMG,(244,586))
        Steuerungstext = self.myfont.render("Q", False, (255, 255, 255))
        screen.blit(Steuerungstext,(244,586+22))
        if q == True:
            if self.activated == False:
                self.activated = True
            
        if self.activated == True:
            self.timer = self.timer + 1
            if self.timer > self.cooldown:
                self.activated = False
                self.timer = 0

        if self.timer == 1:
            max_life = player.max_health
            current_life = player.current_health
            multi = current_life/max_life

            Lebens_multi = 0.25 / multi

            Heilleben = int(((max_life/4)*Lebens_multi))
            player.heal(Heilleben)

        Countdown = self.cooldown - self.timer
        if Countdown < 300:
            Cooldowntext = self.myfont.render(str(Countdown), False, (255, 255, 255))
            screen.blit(Cooldowntext,(244,586+22))

        

