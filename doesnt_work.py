# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:34:08 2020

@author: svtir
"""
#Import libraries
import pygame as py
import numpy as np



import numpy as np
from enum import Enum


    
# Elements Enum class

class Element(Enum):
    FIRE = 0
    WATER = 1
    EARTH = 2
    AIR = 3

# Monsters

class Monster():
    def __init__(self,name, dex, stren, hp, ac, luck, element):
        self.dexterity = dex
        self.strength = stren
        self.hp = hp
        self.armour = ac
        self.luck = luck
        self.element = element
        self.name = name
        
    def crit_multiplier(self):
        critChance = np.random.rand()
        if critChance < self.luck:
            print("Critical Hit!")
            return 2
        else:
            return 1
        
    def element_compare(self, defender):
        if self.element == Element.AIR:
            return 1
        if defender.element == Element.AIR:
            return 1
        if self.element == defender.element:
            return 1
        if self.element == Element.FIRE:
            if defender.element == Element.WATER:
                print('Its not very effective')
                return 0.75
            if defender.element == Element.EARTH:
                print('Its super effective!')
                return 1.5
        if self.element == Element.WATER:
            if defender.element == Element.FIRE:
                print('Its super effective!')
                return 1.5
            if defender.element == Element.EARTH:
                print('Its not very effective')
                return 0.75
        if self.element == Element.EARTH:
            if defender.element == Element.FIRE:
                print('Its not very effective')
                return 0.75
            if defender.element == Element.WATER:
                print('Its super effective!')
                return 1.5
        
    def attack(self, defender):
        defender.hp = defender.hp - self.strength
        
    def scratch(self, defender):
        print(self.name, 'used scratch.')
        baseDmg = self.strength * self.element_compare(defender)
        damage = baseDmg * self.crit_multiplier()
        defender.hp -= damage
        



class Eagle(Monster):
    
    def __init__(self,name, dex, stren, hp, ac, luck, element):
        super().__init__('Eagle',7, 5, 15, 5, 0.2,Element.AIR)

        
    def dive_attack(self,defender):
        
        defender.armour -=5
        
        
monster1 = Eagle()
monster2 = Monster(7, 5, 15, 5, 0.1,Element.EARTH)
     

print(monster2.armour)
monster1.dive_attack(monster2)
        
    
print(monster2.armour)
    


print(monster1.name)






















