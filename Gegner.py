import random 

class MOB(object):

    def __init__(self,name,klasse,positionx,positiony,spawnpositonx,spawnpositiony,chunkx,chunky,bevorzugte_Richtung):

        self.name = name
        self.klasse = klasse
        self.positionx = positionx
        self.positiony = positiony
        self.spawnpositionx = spawnpositonx
        self.spawnpositony = spawnpositiony
        self.chunkx = chunkx
        self.chunky = chunky

        self.posx = positionx
        self.posy = positiony

        self.spawned = False
        self.agro = False
        
        self.bevorzugte_Richtung = bevorzugte_Richtung
        self.movement_Speed = 1
        self.moves = ["Nord","NordOst","SüdOst","Süden","Osten","SüdWest","Westen","NordWest",self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung,self.bevorzugte_Richtung]
        self.animation = "move"
        

        self.actualframe = ""

        self.animationstimer = 1

        self.animation = "move"
        self.move_frames = 2
        self.attack_frames = 5
        self.death_frames = 5

        

        self.realanimationtimer = 1
        self.dauerderFrames = 10

        self.pixel = 1
        self.damaged = False
        if self.klasse == "Slime":
            self.agro_range = 50
            self.attack_range = 15
            self.attack_damage = 10
            self.attack_speed = 105
            self.life = 50

        if self.klasse == "Wolf":
            self.agro_range = 50
            self.attack_range = 20
            self.attack_damage = 25
            self.attack_speed = 105
            self.life = 75

        if self.klasse == "Dämon":
            self.agro_range = 50
            self.attack_range = 25
            self.attack_damage = 30
            self.attack_speed = 105
            self.life = 100 

        if self.klasse == "Golem":
            self.agro_range = 50
            self.attack_range = 25
            self.attack_damage = 80
            self.attack_speed = 120
            self.life = 250    
            
        self.attack_timer = 0
        self.has_attacked = False
        self.is_alive = True 
        
    def revive(self):
        if self.klasse == "Golem":
            self.life = 250
        if self.klasse == "Dämon":
            self.life = 100
        if self.klasse == "Wolf":
            self.life = 75
        if self.klasse == "Slime":
            self.life = 50
        self.is_alive = True 

    def random_spawner(self,chunkx,chunky,posx,posy):
        self.spawnpositionx = posx
        self.spawnpositony = posy
        self.chunkx = chunkx
        self.chunky = chunky
        self.spawned = False

    def check_spawn(self,x,y):
        if self.chunkx == x and self.chunky == y:
            if self.spawned == False:
                self.spawned = True
                self.posx = self.spawnpositionx
                self.posy = self.spawnpositony
                print("gegner gespawnt")
        else:
            self.spawned = False
            self.posx = self.positionx
            self.posy = self.positiony

        if self.is_alive == False and self.realanimationtimer > 48:
            self.posx = 9000
            self.posy = 9000

    def die(self):
        self.is_alive = False

    def recieve_damage(self,damage):
        Drops = ""
        self.life = self.life - damage
        if self.life <= 0 and self.is_alive == True:
            self.die()
            self.animation = "die"
            Drops = self.klasse

        return ( Drops)
    def checke_entfernung(self,player_posx,player_posy):
        Abstand_x = abs(self.posx - player_posx)
        Abstand_y = abs(self.posy - player_posy)
        return(Abstand_x,Abstand_y)

    def move(self,player_posx, player_posy,playerchunkx,playerchunky,chunkwidth,chunkheight):
        #print("Ich habe gerade "+str(self.life)+" Leben")
        self.check_spawn(playerchunkx,playerchunky)
        self.check_agro(player_posx,player_posy)

        if self.spawned == True and self.agro == False and self.is_alive == True:
            self.animation = "move"
            Richtung = random.choice(self.moves)
            if Richtung == "Nord":
                self.posx	= self.posx
                self.posy = self.posy - self.movement_Speed
        
            elif Richtung == "NordOst":
                self.posx = self.posx + (self.movement_Speed/2)
                self.posy = self.posy - (self.movement_Speed/2)
        
            elif Richtung == "Osten":
                self.posx = self.posx + self.movement_Speed
                self.posy = self.posy
        
            elif Richtung == "SüdOst":
                self.posx = self.posx + (self.movement_Speed/2)
                self.posy = self.posy + (self.movement_Speed/2)

            elif Richtung == "Süden":
                self.posx = self.posx
                self.posy = self.posy + self.movement_Speed

            elif Richtung == "SüdWest":
                self.posx = self.posx - (self.movement_Speed/2)
                self.posy = self.posy + (self.movement_Speed/2)

            elif Richtung == "Westen":
                self.posx = self.posx - self.movement_Speed
                self.posy = self.posy

            elif Richtung == "NordWest":
                self.posx = self.posx - (self.movement_Speed/2)
                self.posy = self.posy - (self.movement_Speed/2)
            #print("MEineX: "+str(self.posx)+" MeineY: "+str(self.posy))
            if self.posx <= 0:
                print("Ich bin oben angestoßen")
                self.posx = chunkwidth - 1
            elif self.posx > chunkwidth:
                print("Ich bin unten angestoßen")
                self.posx = 1

            if self.posy <= 0:
                self.posy = chunkheight - 1
                print("Ich bin rechts angestoßen")
            elif self.posy > chunkheight:
                print("Ich bin links angestoßen")
                self.posy = 1

        if self.agro == True and self.is_alive == True:
            self.animation = "attack"
            
            if player_posx < self.posx:
                self.posx = self.posx - self.movement_Speed
                #print("1")
            elif player_posx > self.posx:
                self.posx = self.posx + self.movement_Speed
                #print("2")
            if player_posy < self.posy:
                self.posy = self.posy - self.movement_Speed
                #print("3")
            elif player_posy > self.posy:
                self.posy = self.posy + self.movement_Speed
                #print("4")
            
        return(self.posx,self.posy)




    def how_attack_damage(self,player_posx,player_posy):
        Damage = 0
        Abstand_x = abs(self.posx - player_posx)
        Abstand_y = abs(self.posy - player_posy)
        if self.has_attacked == False:
            if Abstand_x <= self.attack_range and Abstand_y <= self.attack_range:
                Damage = self.attack_damage
                self.has_attacked = True
        elif self.has_attacked == True:
            self.attack_timer = self.attack_timer + 1
            Damage = 0
            if self.attack_timer > self.attack_speed:
                self.attack_timer = 0
                self.has_attacked = False
        #print("Self.attacktimer = "+str(self.attack_timer))
        self.attack_timer = self.attack_timer+1
        return(Damage)

    def check_agro(self,player_posx,player_posy):
        Abstand_x = abs(self.posx - player_posx)
        Abstand_y = abs(self.posy - player_posy)

        #print("X Abstand zum player: "+str(Abstand_x))
        #print("Y Abstand zum Player: "+str(Abstand_y))

        if Abstand_x <= self.agro_range and Abstand_y <= self.agro_range:
            self.agro = True

        else:
            self.agro = False   

    def animate(self):
        self.realanimationtimer = self.realanimationtimer+1
        #print("Realanimationtimer: "+str(self.realanimationtimer))
        if self.animation == "move":
            if self.realanimationtimer <= 10:
                self.actualframe = "move_01"
            elif self.realanimationtimer <=20:
                self.actualframe = "move_02"
            elif self.realanimationtimer > 20:
                self.realanimationtimer = 1 

        if self.animation == "attack":
            if self.realanimationtimer <= 10:
                self.actualframe = "attack_01"
            elif self.realanimationtimer <= 20:
                self.actualframe = "attack_02"
            elif self.realanimationtimer <= 30:
                self.actualframe = "attack_03"
            elif self.realanimationtimer <= 40:
                self.actualframe = "attack_04"
            elif self.realanimationtimer <= 50:
                self.actualframe = "attack_05"
            elif self.realanimationtimer >50:
                self.realanimationtimer = 1

        if self.animation == "die":
            if self.realanimationtimer <= 10:
                self.actualframe = "die_01"
            elif self.realanimationtimer <= 20:
                self.actualframe = "die_02"
            elif self.realanimationtimer <= 30:
                self.actualframe = "die_03"
            elif self.realanimationtimer <= 40:
                self.actualframe = "die_04"
            elif self.realanimationtimer <= 50:
                self.actualframe = "die_05"
            elif self.realanimationtimer >50:
                self.realanimationtimer = 1
                self.die()

        if self.actualframe == "move_01":
            self.pixel = 0
            self.damaged = False
        if self.actualframe == "move_02":
            self.pixel = 1
            self.damaged = False

        if self.actualframe == "attack_01":
            self.pixel = 2
            self.damaged = False
        if self.actualframe == "attack_02":
            self.pixel = 3
            self.damaged = False
        if self.actualframe == "attack_03":
            self.pixel = 4
            self.damaged = False
        if self.actualframe == "attack_04":
            self.pixel = 5
            self.damaged = False
        if self.actualframe == "attack_05":
            self.pixel = 6
            self.damaged = False

        if self.actualframe == "die_01":
            self.pixel = 7
            self.damaged = False
        if self.actualframe == "die_02":
            self.pixel = 8
            self.damaged = False
        if self.actualframe == "die_03":
            self.pixel = 9
            self.damaged = False
        if self.actualframe == "die_04":
            self.pixel = 10
            self.damaged = False
        if self.actualframe == "die_05":
            self.pixel = 11
            self.damaged = False
            self.die()

        #print(self.actualframe)
        #print("Frame: "+str(self.pixel))
        return(self.pixel,self.damaged)

        
