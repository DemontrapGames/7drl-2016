from random import randint
import util.config as config
import libtcodpy as libtcod
import util.floor as floor

class Creature():
    def __init__(self, x, y, char,
                 hp, strength, defense,
                 spd, mgk=0, lck=0):
        self.x = x
        self.y = y

        self.hp = hp
        self.strength = strength
        self.defense = defense
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
                   i.strength > 0:
                    return i.strength + self.strength

    def getDef(self):
        if self.inv is not None:
            for i in self.inv:
                if i.equipped and \
                   i.defense > 0:
                    return i.defense + self.defense

    def setPos(self, x, y):
        self.x = x
        self.y = y


class Player(Creature):
    def __init__(self, class_type):
        self.class_type = class_type
#        stats = randomize.makeStats(class_type)
        super(Player, self).__init__(0, 0, "@", 12, 5, 5, 2)
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
