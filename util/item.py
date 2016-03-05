from util.randomize import randname

class Item():
    """Documentation for Item

    """
    def __init__(self, eqpble):
        self.equipped = False
        self.equippable = eqpble

    def equip(self):
        if self.equippable:
            self.equipped = not self.equipped


class Armor(Item):
    """Documentation for Armor

    """
    def __init__(self, def):
        super(Armor, self).__init__(True)
        self.def = def
        self.name = randname(Armor)
        
class Weapon(Item):
    """Documentation for Weapon

    """
    def __init__(self, str):
        super(Weapon, self).__init__(True)
        self.str = str
        self.name = randname(Weapon)
