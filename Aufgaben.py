

class Aufgaben(object):
    def __init__ (self,name,beschreibung,gegenstand1,gegenstand2,gegenstand3,gegenstand1_max,gegenstand2_max,gegenstand3_max,chunkx,chunky,spawnposx,spawnposy,gold,xp,zielchunkx,zielchunky):
        self.name = name
        self.beschreibung = beschreibung

        self.gegenstand1 = gegenstand1
        self.gegenstand1_max = gegenstand1_max
        self.gegenstand1_current = 0

        self.gegenstand2 = gegenstand2
        self.gegenstand2_max = gegenstand2_max
        self.gegenstand2_current = 0

        self.gegenstand3 = gegenstand3
        self.gegenstand3_max = gegenstand3_max
        self.gegenstand3_current = 0

        self.chunkx = chunkx
        self.chunky = chunky

        self.spawnposx = spawnposx
        self.spawnposy = spawnposy

        self.posxspeicher = 9000
        self.posyspeicher = 9000

        self.currentposx = 9000
        self.currentposy = 9000

        self.zielchunkx = zielchunkx
        self.zielchunky = zielchunky
        
        self.is_active = False
        self.is_finished = False

        self.gold = gold
        self.xp = xp
        self.near_enough = False
        self.already_claimed = False

    def spawn(self):
        self.currentposx = self.spawnposx
        self.currentposy = self.spawnposy
    
    def despawn(self):
        self.currentposx = self.posxspeicher
        self.currentposy = self.posyspeicher

    def check_position(self,playerposx,playerposy):
        Abstand_x = abs(self.currentposx - playerposx)
        Abstand_y = abs(self.currentposy - playerposy)
        if Abstand_x <= 100 and Abstand_y <=100:
            self.near_enough = True           
        else:
            self.near_enough = False

    def activate_Quest(self):
        self.isactive = True

    def claim(self):
        self.already_claimed = True

    def check_finished(self):
        if self.gegenstand1_current >= self.gegenstand1_max and self.gegenstand2_current >= self.gegenstand2_max and self.gegenstand3_current >= self.gegenstand3_max:
            self.is_finished = True

        return(self.is_finished)

    def check_Drops(self,Drops):
        for a in Drops:
            if a == self.gegenstand1:
                self.gegenstand1_current = self.gegenstand1_current + 1
            if a == self.gegenstand2:
                self.gegenstand2_current = self.gegenstand2_current + 1
            if a == self.gegenstand3:
                self.gegenstand3_current = self.gegenstand3_current + 1

    



        