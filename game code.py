import numpy as np
from enum import Enum
import pygame

    
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
                
class Eagle(Monster):
    
    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Eagle', 7, 5, 15, 10, 0.2, Element.AIR)
        
    def dive_attack(self,defender):
        print(self.name, 'used dive attack.')
        defender.armour -=5
    
    def wing_slash(self, defender):
        print(self.name, 'used wing slash.')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage

class Ent(Monster):
    
    def __int__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Ent', 4, 7, 20, 10, 0.1, Element.Earth)
    
    
        
        
monster1 = Monster('marc', 7, 5, 15, 5, 0.2, Element.FIRE)
monster2 = Monster('pat', 7, 5, 15, 5, 0.1, Element.EARTH)
monster3 = Eagle()

move_list_eagle = ['Quick Attack', 'Dive Attack', 'Wing Slash']
move_list_ent = 
# main code

print ('hp: ', monster3.hp)
monster1.scratch(monster3)
print ('hp: ', monster3.hp)


turns = 1

p1_monster = monster1
p2_monster = monster3

while p1_monster.hp > 0 and p2_monster.hp > 0:
    
    

ATTACK
    if monster1.dodge() == 0:
        damage = 0
    else:
        monster3.dive_attack(monster1)
        
    