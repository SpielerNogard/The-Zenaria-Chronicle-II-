
class Collisionen(object):
    def __init__(self):
        self.name = "Hallo"
        self.Collision1 = ["Wasser_Ozean","Wasser_Fluss","Baum1","Baum2","Durchsichtig","Berg","House_1","House_2","House_3","House_4","Palast_Außen_Wand","Palast_Außen_Wand_Top","Temple","Palast_Außen","Zaun","Stein","Schwarzes_Rechteck"]
        self.Collision2 = ["Tempel_Wand_Front_Rest","Tempel_Wand_Front_Verbindung_Zum_Boden","Tempel_Wand_Links","Tempel_Wand_Rechts","Tempel_Wand_Oben","Tempel_Wand_Unten","Altar","Fackel","Fountain"]
        self.Collision3 = ["Haus_innen_Wand_links_Final","Haus_innen_Wand_oben_FInal","Haus_innen_Wand_rechts_Final","Haus_innen_Wand_unten_Final","Haus_Wand_Visible__Front__Final"]
        self.has_Colisions = self.Collision1 + self.Collision2 + self.Collision3
        self.playerx_change = 0
        self.playery_change = 0
    def check_Collisions(self,playerx,playery,playerx_change,playery_change,actualchunk):
        self.playerx_change = playerx_change
        self.playery_change = playery_change
        #print("PlayerX_Change: "+str(playerx_change))
        #print("PlayerY_Change: "+str(playery_change))
        if playerx_change < 0 :
            self.Norden(playerx,playery,actualchunk)
        if playery_change>0:
            self.Osten(playerx,playery,actualchunk)
        if playerx_change >0:
            self.Süden(playerx,playery,actualchunk)
        if playery_change<0:
            self.Westen(playerx,playery,actualchunk)
        Start_X = playerx - 32
        Ende_X = playerx + 96
        Start_Y = playery - 32
        Ende_Y = playery + 96
        
        return(self.playerx_change,self.playery_change)

    def Norden(self,playerx,playery,actualchunk):
        Start_X = playerx - 32
        Ende_X = playerx + 96
        Start_Y = playery - 32
        Ende_Y = playery + 96
        for a in actualchunk:
            Gegenstand = str(a[0])
            Gegenstand_x = int(a[1])
            Gegenstand_y = int(a[2])

            if Gegenstand_x >= playerx and Gegenstand_x <= (playerx+64):
                if Gegenstand_y >= Start_Y and Gegenstand_y <playery:
                    print(Gegenstand)
                    if Gegenstand in self.has_Colisions:
                        self.playerx_change = 0

    def Osten(self,playerx,playery,actualchunk):
        Start_X = playerx - 32
        Ende_X = playerx + 96
        Start_Y = playery - 32
        Ende_Y = playery + 96
        for a in actualchunk:
            Gegenstand = str(a[0])
            Gegenstand_x = int(a[1])
            Gegenstand_y = int(a[2])

            if Gegenstand_x >= (playerx+64) and Gegenstand_x <= Ende_X:
                if Gegenstand_y >= playery and Gegenstand_y <playery+64:
                    print(Gegenstand)
                    if Gegenstand in self.has_Colisions:
                        self.playery_change = 0

    def Süden(self,playerx,playery,actualchunk):
        for a in actualchunk:
            Gegenstand = str(a[0])
            Gegenstand_x = int(a[1])
            Gegenstand_y = int(a[2])

            if Gegenstand_x >= playerx and Gegenstand_x <= playerx+64:
                if Gegenstand_y >= playery + 64 and Gegenstand_y <= playery + 96:
                    print (Gegenstand)
                    if Gegenstand in self.has_Colisions:
                        self.playerx_change = 0

    def Westen(self,playerx,playery,actualchunk):
        for a in actualchunk:
            Gegenstand = str(a[0])
            Gegenstand_x = int(a[1])
            Gegenstand_y = int(a[2])

            if Gegenstand_x <= playerx and Gegenstand_x >= playerx-32:
                if Gegenstand_y >= playery and Gegenstand_y <playery+64:
                    print (Gegenstand)
                    if Gegenstand in self.has_Colisions:
                        self.playery_change = 0