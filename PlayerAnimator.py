import pygame
import itertools

class PlayerAnimator(object):
    def __init__(self):
        self.timer = 0
        self.Idle_01 = pygame.image.load("Assets/Character_idle_01.png")
        self.Idle_02 = pygame.image.load("Assets/Character_idle_02.png")

        self.attack_01 = pygame.image.load("Assets/Character_Attack_01.png")
        self.attack_02 = pygame.image.load("Assets/Character_Attack_02.png")
        self.attack_03 = pygame.image.load("Assets/Character_Attack_03.png")
        self.attack_04 = pygame.image.load("Assets/Character_Attack_04.png")
        self.attack_05 = pygame.image.load("Assets/Character_Attack_05.png")

        self.walking_01 = pygame.image.load("Assets/Character_Walking_01.png")
        self.walking_02 = pygame.image.load("Assets/Character_Walking_02.png")

        self.Idle_01_left = pygame.image.load("Assets/Character_left_idle_01.png")
        self.Idle_02_left = pygame.image.load("Assets/Character_left_idle_02.png")

        self.attack_01_left = pygame.image.load("Assets/Character_left_Attack_01.png")
        self.attack_02_left = pygame.image.load("Assets/Character_left_Attack_02.png")
        self.attack_03_left = pygame.image.load("Assets/Character_left_Attack_03.png")
        self.attack_04_left = pygame.image.load("Assets/Character_left_Attack_04.png")
        self.attack_05_left = pygame.image.load("Assets/Character_left_Attack_05.png")

        self.walking_01_left = pygame.image.load("Assets/Character_left_Walking_01.png")
        self.walking_02_left = pygame.image.load("Assets/Character_left_Walking_02.png")


        self.idle_animationcycle = [self.Idle_01,self.Idle_02]
        self.attack_animationcycle = [self.attack_01,self.attack_02,self.attack_03,self.attack_04,self.attack_05]
        self.walking_animationcycle = [self.walking_01,self.walking_02]

        self.idle_animationcycle_left = [self.Idle_01_left,self.Idle_02_left]
        self.attack_animationcycle_left = [self.attack_01_left,self.attack_02_left,self.attack_03_left,self.attack_04_left,self.attack_05_left]
        self.walking_animationcycle_left = [self.walking_01_left,self.walking_02_left]

        self.IDLE = itertools.cycle(self.idle_animationcycle)
        self.WALKING = itertools.cycle(self.walking_animationcycle)
        self.ATTACK = itertools.cycle(self.attack_animationcycle)
        
        self.IDLE_left = itertools.cycle(self.idle_animationcycle_left)
        self.WALKING_left = itertools.cycle(self.walking_animationcycle_left)
        self.ATTACK_left = itertools.cycle(self.attack_animationcycle_left)
        
        self.cycle = self.IDLE
        self.actual_image = next(self.cycle)
        self.animation = "idle"
        self.direction = "right"

    def animate_player(self,W,A,S,D,Q):
        self.timer = self.timer + 1
        if W == True or A == True or S == True or D == True:
            self.animation = "move"

        if W == True or D == True:
            self.direction = "right"

        if S == True or A == True:
            self.direction = "left"

        if Q == True:
            self.animation = "attack"

        if W == False and A == False and S == False and D == False and Q == False:
            self.animation = "idle"
        
        if self.animation == "move" and self.direction == "right":
            self.cycle = self.WALKING

        elif self.animation == "attack" and self.direction == "right" :
            self.cycle = self.ATTACK

        elif self.animation == "move" and self.direction == "left":
            self.cycle = self.WALKING_left

        elif self.animation == "attack" and self.direction == "left" :
            self.cycle = self.ATTACK_left

        else: 
            if self.direction == "right":
                self.cycle = self.IDLE

            if self.direction == "left":
                self.cycle = self.IDLE_left

        if self.timer % 3 == 0:
            self.actual_image = next(self.cycle)

        return(self.actual_image)