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
    
    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Ent', 4, 7, 20, 10, 0.1, Element.EARTH)
    
    def stomp(self, defender):
        print(self.name, 'used stomp')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage
    
    def vine_whip(self, defender):
        print(self.name, 'used vine whip')
        baseDmg = self.strength * self.element_compare(defender) * 1.2
        damage = baseDmg * self.crit_multiplier() * defender.armour_multiplier()
        defender.hp -= damage

class devil(Monster):
    def __init__(self):
        # name, dex, stren, hp, ac, luck, element
        super().__init__('Devil', 9, 5, 17, 4, 0.3, Element.FIRE)
        
        

monster1 = Eagle()
monster2 = Ent()

move_list_eagle = ['Quick Attack', 'Dive Attack', 'Wing Slash']
move_list_ent = ['Attack', 'Stomp', 'Vine Whip']

# main code



    



import pygame as py


# initializing the constructor 
py.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = py.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = py.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
attack_1_mon_1 = smallfont.render(move_list_eagle[0] , True , color) 
attack_2_mon_1 = smallfont.render(move_list_eagle[1] , True , color) 
attack_3_mon_1 = smallfont.render(move_list_eagle[2] , True , color) 

attack_1_mon_2 = smallfont.render(move_list_ent[0] , True , color) 
attack_2_mon_2 = smallfont.render(move_list_ent[1] , True , color) 
attack_3_mon_2 = smallfont.render(move_list_ent[2] , True , color) 



button_1_loc = [width/2,height/2,160,40]
button_2_loc = [150,height/2,160,40]
button_3_loc = [width/2,150,160,40]


#def monster_turn(monster):
    
Eagle_turn =True
Ent_turn = False

while True: 
  if Eagle_turn ==True:
    for ev in py.event.get(): 
          
        if ev.type == py.QUIT: 
            py.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == py.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]: 
                monster1.quick_attack(monster2)
                print(monster2.hp)
                Ent_turn = True
                Eagle_turn =False
                
                
                
            if button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]: 
                print(monster2.hp)
                monster1.dive_attack(monster2)
                print(monster2.hp)
                Ent_turn = True
                Eagle_turn =False
            
            
                
            if button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]: 
                print(monster2.hp)
                monster1.wing_slash(monster2)
                print(monster2.hp)
                Ent_turn = True
                Eagle_turn =False
                
                  
    # fills the screen with a color 
    screen.fill((60,25,60))
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = py.mouse.get_pos() 


    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]: 
        py.draw.rect(screen,color_light,button_1_loc) 
          
    elif button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]: 
        py.draw.rect(screen,color_light,button_2_loc) 
        
    elif button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]: 
        py.draw.rect(screen,color_light,button_3_loc) 
   
    else: 
        py.draw.rect(screen,color_dark,button_1_loc ) 
        py.draw.rect(screen,color_dark,button_2_loc )
        py.draw.rect(screen,color_dark,button_3_loc ) 
        
      
    # superimposing the text onto our button 
    screen.blit(attack_1_mon_1 ,(button_1_loc[0],button_1_loc[1]))
    screen.blit(attack_2_mon_1 ,(button_2_loc[0],button_2_loc[1]))
    screen.blit(attack_3_mon_1 ,(button_3_loc[0],button_3_loc[1]))
    
      
    # updates the frames of the game 
    py.display.update() 
            
  elif Ent_turn  ==True:   
    for ev in py.event.get(): 
          
        if ev.type == py.QUIT: 
            py.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == py.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]: 
                monster2.stomp(monster1)
                print(monster1.hp)
                Ent_turn = False
                Eagle_turn =True
                
                
                
            if button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]: 
                monster2.stomp(monster1)
                print(monster1.hp)
                Ent_turn = False
                Eagle_turn =True
            
            
                
            if button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]: 
                monster2.vine_whip(monster1)
                print(monster1.hp)
                Ent_turn = False
                Eagle_turn = True
                
                  
    # fills the screen with a color 
    screen.fill((60,25,60))
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = py.mouse.get_pos() 


    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]: 
        py.draw.rect(screen,color_light,button_1_loc) 
          
    elif button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]: 
        py.draw.rect(screen,color_light,button_2_loc) 
        
    elif button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]: 
        py.draw.rect(screen,color_light,button_3_loc) 
   
    else: 
        py.draw.rect(screen,color_dark,button_1_loc ) 
        py.draw.rect(screen,color_dark,button_2_loc )
        py.draw.rect(screen,color_dark,button_3_loc ) 
        
      
    # superimposing the text onto our button 
    screen.blit(attack_1_mon_2 ,(button_1_loc[0],button_1_loc[1]))
    screen.blit(attack_2_mon_2 ,(button_2_loc[0],button_2_loc[1]))
    screen.blit(attack_3_mon_2 ,(button_3_loc[0],button_3_loc[1]))
    
      
    # updates the frames of the game 
    py.display.update()         

    
    
            







        
    























