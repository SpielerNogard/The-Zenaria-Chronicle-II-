

class UI(object):
    def __init__(self):
        self.name = "UI "

    def calculate_Health(self,max_health,current_health):

        healthpercent = current_health/max_health
        if healthpercent > 1:
            healthpercent = 1
        return(healthpercent)

    def calculate_Mana(self,max_mana,current_mana):

        manapercent = current_mana/max_mana
        return(manapercent)

    def calculate_XP(self, current_lvl, xpmulti, current_xp):
        xppercent = current_xp/(current_lvl*xpmulti)
        return xppercent