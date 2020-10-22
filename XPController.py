
class XPController(object):
    def __init__(self):
        self.WolfXP = 10
        self.SlimeXP = 5
        self.DämonXP = 15
        self.GolemXP = 20

        self.WolfGold = 100
        self.SlimeGold = 50
        self.DämonGold = 150
        self.GolemGold = 200

    def Calculate_XP(self, gestorbene_Gegner):
        given_xp = 0
        givengold = 0
        for a in gestorbene_Gegner:
            if a == "Wolf":
                given_xp = given_xp + self.WolfXP
                givengold = givengold + self.WolfGold
            if a == "Slime":
                given_xp = given_xp + self.SlimeXP
                givengold = givengold + self.SlimeGold

            if a == "Golem":
                given_xp = given_xp + self.GolemXP
                givengold = givengold + self.GolemGold

            if a == "Dämon":
                given_xp = given_xp + self.DämonXP
                givengold = givengold + self.DämonGold



        return(given_xp,givengold)