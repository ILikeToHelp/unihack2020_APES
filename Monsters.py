import numpy as np
from enum import Enum
import pygame as py
import sys

# Elements Enum class

class Element(Enum):
    FIRE = 0
    WATER = 1
    EARTH = 2
    AIR = 3

# General Monsters class

class Monster():
    def __init__(self, name, dex, stren, hp, ac, luck, element):
        self.name = name
        self.dexterity = dex
        self.strength = stren
        self.hp = hp
        self.armour = ac
        self.luck = luck
        self.element = element

    # Uses the luck to see if the hit is critical
    def crit_multiplier(self):
        critChance = np.random.rand()
        if critChance < self.luck:
            print("Critical Hit!")
            return 2
        else:
            return 1
    def dodge(defender):
        dodgeChance = np.random.rand()
        if dodgeChance < (defender.dexterity) * 0.05:
            print("Dodged!")
            return 0
        else:
            return 1

    def armour_multiplier(defender):
        return 10/(10+defender.armour)

    # Compares the Elements to find multipliers
    def element_compare(self, defender):
        if self.element == Element.AIR:
            return 1
        elif defender.element == Element.AIR:
            return 1
        elif self.element == defender.element:
            return 1
        elif self.element == Element.FIRE:
            if defender.element == Element.WATER:
                print('Its not very effective')
                return 0.75
            elif defender.element == Element.EARTH:
                print('Its super effective!')
                return 1.5
        elif self.element == Element.WATER:
            if defender.element == Element.FIRE:
                print('Its super effective!')
                return 1.5
            elif defender.element == Element.EARTH:
                print('Its not very effective')
                return 0.75
        elif self.element == Element.EARTH:
            if defender.element == Element.FIRE:
                print('Its not very effective')
                return 0.75
            elif defender.element == Element.WATER:
                print('Its super effective!')
                return 1.5

    # ATTACKS

    def quick_attack(self, defender):
        print(self.name, 'used quick attack.')
        baseDmg = self.strength * self.element_compare(defender)
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

class Eagle(Monster):

    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Eagle', 7, 5, 15, 10, 0.2, Element.AIR)
        self.moves = ['Quick Attack', 'Dive Attack', 'Wing Slash']
    def dive_attack(self,defender):
        print(self.name, 'used dive attack.')
        defender.armour -=5

    def wing_slash(self, defender):
        print(self.name, 'used wing slash.')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

class Treebeard(Monster):

    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Treebeard', 4, 7, 20, 10, 0.1, Element.EARTH)
        self.moves = ['Attack', 'Stomp', 'Vine Whip']
    def stomp(self, defender):
        print(self.name, 'used stomp')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

    def vine_whip(self, defender):
        print(self.name, 'used vine whip')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

class Devil(Monster):
    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Devil', 9, 5, 17, 4, 0.3, Element.FIRE)
        self.moves = ['Quick Attack', 'Hellflame', 'Ash Cloud']
    def hellflame(self, defender):
        print(self.name, 'used hellflame')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

    def ash_cloud (self, defender):
        print(self.name, 'used ash cloud')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

class Naga(Monster):
    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Naga', 9, 5, 17, 4, 0.3, Element.WATER)
        self.moves = ['Quick Attack', 'Aqua Pulse', 'Rainstorm']
    def aqua_pulse(self, defender):
        print(self.name, 'used aqua pulse')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True

    def rainstorm (self, defender):
        print(self.name, 'used rainstorm')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
        if defender.hp <= 0:
            return True



monster1 = Eagle()
monster2 = Treebeard()
monster3 = Devil()
monster4 = Naga()

move_list_eagle = ['Quick Attack', 'Dive Attack', 'Wing Slash']
move_list_treebeard = ['Attack', 'Stomp', 'Vine Whip']
move_list_eagle = ['Quick Attack', 'Dive Attack', 'Wing Slash']
move_list_treebeard = ['Quick Attack', 'Stomp', 'Vine Whip']
move_list_devil = ['Quick Attack', 'Hellflame', 'Ash Cloud']
