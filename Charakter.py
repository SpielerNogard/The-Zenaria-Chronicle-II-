class charakter(object):

    def __init__(self, name, health, mana, gold, lvl,klasse, posx, posy, max_health, max_mana, all_exp,current_exp,strenght ):

        self.name = name

        self.pos_x = posx
        self.pos_y = posy

        self.current_health = health
        self.max_health = max_health

        self.current_mana = mana
        self.max_mana = max_mana

        self.gold = gold

        self.start_attack_damage = 10
        self.attack_speed = 1

        self.exp = current_exp
        self.all_exp = all_exp

        self.strenght = strenght

        self.lvl = lvl 

        self.health_per_lvl = 10
        self.mana_per_lvl = 10
        self.strenght_per_lvl = 1
        self.exp_multi = 2

        self.abilitie1_cost=25
        self.abilitie2_cost=50
        self.abilitie3_cost=75
        self.abilitie4_cost=100

        self.charakterclass = klasse
        self.attack_range = 20
        self.need_teleport = False
        if self.charakterclass == "Krieger":
            self.ability1 = "Schwertwurf"
            self.ability2 = "Schwertwirbel"
            self.ability3 = "Macht der Phalanx"
            self.ability4 = "Wille des Blutes"

    def move(self, delta_x, delta_y):
        self.pos_x = self.pos_x + delta_x
        self.pos_y = self.pos_y + delta_y
        return(self.pos_x,self.pos_y)
    def get_exp(self, exp_gain):

        self.exp = self.exp + exp_gain
        self.all_exp = self.exp + exp_gain
        if self.exp >= self.lvl* self.exp_multi:
            self.lvl_up()

    def get_gold(self,gold_gain):
        self.gold = self.gold+gold_gain

    def lvl_up(self):

        self.lvl = self.lvl + 1
        self.exp = 0
        #print("LVL UP")

        
        self.strenght = self.strenght + self.strenght_per_lvl
        self.max_mana = self.max_mana + self.mana_per_lvl
        self.max_health = self.max_health + self.health_per_lvl

        #heal
        self.current_mana = self.max_mana
        self.current_health = self.max_health

        
    def heal(self,amount):
        self.current_health = self.current_health + amount
    def die(self):
        self.exp = self.exp - int(0.05*self.exp)
        self.current_health = self.max_health / 2
        self.current_mana = self.max_mana / 2
        self.need_teleport = True
        

        #print("You died")
    def revived(self):
        self.need_teleport = False
    def attack(self):
        self.calculate_attack_damage()
        return self.attack_damage
    
    def calculate_attack_damage(self):
        attack_multi = self.start_attack_damage * self.strenght
        self.attack_damage = self.start_attack_damage + attack_multi

        #life multiplier
        life_multiplier = 1
        if self.current_health < self.max_health * 0.25:
            life_multiplier = 3.0
            
        elif self.current_health < self.max_health*0.5:
            life_multiplier = 2.0
        
        elif self.current_health > self.max_health*0.5:
            life_multiplier = 1.5

        #print("Life multiplier Ist: "+str(life_multiplier))
        self.attack_damage = self.attack_damage*life_multiplier

    def damaged(self, damage):
        self.current_health = self.current_health - damage

        if self.current_health <= 0:
            self.die()

        #print("Ouch")
    def pay(self,payed):

        successfully_payed = False
        if self.gold >= payed:
            self.gold = self.gold - payed
            successfully_payed = True
        
        return(successfully_payed)

    def teleport_player(self,posx,posy):
        self.pos_x = posx
        self.pos_y = posy

    def use_abilitie_1(self):
        if self.abilitie1_cost<= self.current_mana:
            self.current_mana = self.current_mana - self.abilitie1_cost
            if self.ability1 == "Schwertwurf":
                print("werfe Schwert")
    
    def use_abilitie_2(self):
        if self.abilitie2_cost<= self.current_mana:
            self.current_mana = self.current_mana - self.abilitie2_cost
            if self.ability3 == "Schwertwirbel":
                print("wirble Schwert")
    
    def use_abilitie_3(self):
        if self.abilitie3_cost<= self.current_mana:
            self.current_mana = self.current_mana - self.abilitie3_cost
            if self.ability3 == "Macht der Phalanx":
                print("Phanlanxiere")
    
    def use_abilitie_4(self):
        if self.abilitie4_cost<= self.current_mana:
            self.current_mana = self.current_mana - self.abilitie4_cost
            if self.ability4 == "Wille des Blutes":
                print("Blut")

