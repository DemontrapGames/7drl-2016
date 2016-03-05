from random import randint

class Creature():
    def __init__(self, x, y,
                 hp, str, def
                 spd, mgk=0, lck=0):
        self.x = x
        self.y = y

        self.hp = hp
        self.str = str
        self.def = def
        self.spd = spd
        self.inv = None

        if mgk > 0:
            self.mgk = mgk

        if lck > 0:
            self.lck = lck

    def move(self, dx, dy):
        # TODO: implement wall checking here
        self.x += (dx * self.spd)
        self.y += (dy * self.spd)

    def attack(self, enemy):
        if self.hp > 0:
            enemy.hp -= (enemy.getDef() - self.getStr())

    def getStr(self):
        if self.inv is not None:
            for i in self.inv:
                if i.equipped and \
                   i.str > 0:
                    return i.str + self.str

    def getDef(self):
        if self.inv is not None:
            for i in self.inv:
                if i.equipped and \
                   i.def > 0:
                    return i.def + self.def


class Player(Creature):
    def __init__(self):
        super(Player, self).__init__()
        self.inv = []
        self.equipped = []

    def equip(self, i):
        for o in self.inv:
            if o.name == i.name and \
               not o.equipped:
                self.equipped(o)
                self.inv.remove(o)

                for e in self.equipped:
                    if type(e) == type(o):
                        self.inv.append(e)
                        self.equipped.remove(e)
            
