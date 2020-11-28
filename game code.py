import numpy as np
from enum import Enum


    
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
        if dodgeChance < defender.luck:
            print("Dodged!")
            return 0
        else:
            return 1
       
    # Compares the Elements to find multipliers    
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
        
    # ATTACKS  
        
    def scratch(self, defender):
        print(self.name, 'used scratch.')
        if defender.dodge() == 0:
            damage = 0
        else:
            baseDmg = self.strength * self.element_compare(defender)
            damage = baseDmg * self.crit_multiplier()
            defender.armour -= damage
            if defender.armour < 0:
                # deals damage to the armour, and takes any overflow damage away from hp
                defender.hp += defender.armour
                defender.armour = 0
        
monster1 = Monster('marc', 7, 5, 15, 5, 0.2, Element.FIRE)
monster2 = Monster('pat', 7, 5, 15, 5, 0.1, Element.EARTH)



print (monster2.hp)
monster1.scratch(monster2)
print (monster2.hp)
