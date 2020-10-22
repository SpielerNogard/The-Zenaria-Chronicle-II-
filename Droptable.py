import random

class Droptable(object):
    def __init__(self):
        self.slimedrops = ["Holzscheite","klebriger Schleim"]
        self.wolfdrops = ["Wolfspelz"]

        self.Drops = []

    def give_drops(self,tote_mobs):
        self.Drops = []
        for a in tote_mobs:
            self.Drops.append(a)
            if a == "Slime":
                Drop = random.choice(self.slimedrops)
                self.Drops.append(Drop)
            elif a == "Wolf":
                Drop = random.choice(self.wolfdrops)
                self.Drops.append(Drop)
        return(self.Drops)
