# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:36:21 2020

@author: Marc
"""

import pygame
from PIL import Image
import Monsters as m
import Player as p

SIZE = WIDTH, HEIGHT = 900, 600#the width and height of our screen
BACKGROUND_PICTURE = pygame.image.load('pics/bg.png') #https://www.deviantart.com/drboxhead/art/Avatar-The-Last-Airbender-Wallpaper-750669085
BACKGROUND_PICTURE = pygame.transform.scale(BACKGROUND_PICTURE, SIZE)

FPS = 6  #Frames per second

# ImageR1 = 'pics/resizedEagleR1.png'
# ImageR2 = 'pics/resizedEagleR2.png'
# ImageR3 = 'pics/resizedEagleR3.png'

# Define for now (httpswww.kindpng.comimgvhmmwJxR_eagle-sprite-sheet-png-transparent-png)




# Define for now (https://broseoseike.wordpress.com/tag/sprite-sheet/#jp-carousel-(406)


# TODO FIX THOSE SPRITES -> VERY BAD

# ImageR1 = 'pics/resizedEntR1.png'
# ImageR2 = 'pics/resizedEntR2.png'
# ImageR3 = 'pics/resizedEntR3.png'



# Define for now (https://www.coroflot.com/geekbrush/Wicked-Little-Devil)


# ImageR1 = 'pics/resizedDevilR1.png'
# ImageR2 = 'pics/resizedDevilR2.png'
# ImageR3 = 'pics/resizedDevilR3.png'


#Define for now (https://broseoseike.files.wordpress.com/2009/04/naga.png)

# ImageR1 = 'pics/resizedNagaR1.png'
# ImageR2 = 'pics/resizedNagaR2.png'
# ImageR3 = 'pics/resizedNagaR3.png'


class MySprite(pygame.sprite.Sprite):
    def __init__(self, player):
        super(MySprite, self).__init__()

        self.images = []
        self.rect = None

        self.index = 0


        if(player.number == 1):
            self.rect = positionL
            # it's player one so on the left
            if(player.monster.name == "Eagle"):
                # it's an eagle, so load eagle left images
                self.images.append(pygame.image.load('pics/resizedEagleL1.png'))
                self.images.append(pygame.image.load('pics/resizedEagleL2.png'))
                self.images.append(pygame.image.load('pics/resizedEagleL3.png'))
            elif(player.monster.name == "Naga"):
                # it's an eagle, so load eagle left images
                self.images.append(pygame.image.load('pics/resizedNagaL1.png'))
                self.images.append(pygame.image.load('pics/resizedNagaL2.png'))
                self.images.append(pygame.image.load('pics/resizedNagaL3.png'))
            elif(player.monster.name == "Devil"):
                self.images.append(pygame.image.load('pics/resizedDevilL1.png'))
                self.images.append(pygame.image.load('pics/resizedDevilL2.png'))
                self.images.append(pygame.image.load('pics/resizedDevilL3.png'))
            elif(player.monster.name == "Ent"):
                self.images.append(pygame.image.load('pics/resizedEntL1.png'))
                self.images.append(pygame.image.load('pics/resizedEntL2.png'))
                self.images.append(pygame.image.load('pics/resizedEntL3.png'))
        else:
            #only two players, duh
            self.rect = positionR
            if(player.monster.name == "Eagle"):
                # it's an eagle, so load eagle left images
                self.images.append(pygame.image.load('pics/resizedEagleR1.png'))
                self.images.append(pygame.image.load('pics/resizedEagleR2.png'))
                self.images.append(pygame.image.load('pics/resizedEagleR3.png'))
            elif(player.monster.name == "Naga"):
                # it's an eagle, so load eagle left images
                self.images.append(pygame.image.load('pics/resizedNagaR1.png'))
                self.images.append(pygame.image.load('pics/resizedNagaR2.png'))
                self.images.append(pygame.image.load('pics/resizedNagaR3.png'))
            elif(player.monster.name == "Devil"):
                self.images.append(pygame.image.load('pics/resizedDevilR1.png'))
                self.images.append(pygame.image.load('pics/resizedDevilR2.png'))
                self.images.append(pygame.image.load('pics/resizedDevilR3.png'))
            elif(player.monster.name == "Ent"):
                self.images.append(pygame.image.load('pics/resizedEntR1.png'))
                self.images.append(pygame.image.load('pics/resizedEntR2.png'))
                self.images.append(pygame.image.load('pics/resizedEntR3.png'))



    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]







def resize_monsters():
    # NAGA
    resize_image("NagaL1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("NagaL2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("NagaL3.png", int(WIDTH/6), int(HEIGHT/3))

    resize_image("NagaR1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("NagaR2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("NagaR3.png", int(WIDTH/6), int(HEIGHT/3))

    # DEVIL# #
# ImageR1 = 'pics/resizedNagaR1.png'
# ImageR2 = 'pics/resizedNagaR2.png'
# ImageR3 = 'pics/resizedNagaR3.png'
    resize_image("DevilL1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("DevilL2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("DevilL3.png", int(WIDTH/6), int(HEIGHT/3))

    resize_image("DevilR1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("DevilR2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("DevilR3.png", int(WIDTH/6), int(HEIGHT/3))


    #ENT
    resize_image("EagleL1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleL2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleL3.png", int(WIDTH/6), int(HEIGHT/3))

    resize_image("EagleR1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleR2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleR3.png", int(WIDTH/6), int(HEIGHT/3))


    #EAGLE
    resize_image("EntL1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EntL2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EntL3.png", int(WIDTH/6), int(HEIGHT/3))

    resize_image("EntR1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EntR2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EntR3.png", int(WIDTH/6), int(HEIGHT/3))

def resize_image(name, desiredWidth, desiredHeigh):
    # source: https://gph.is/1cmXeXT
    img = Image.open("pics/" + name)
    img = img.resize((desiredWidth, desiredHeigh), Image.ANTIALIAS)
    img.save("pics/resized" + name)


# Define Position of bird

positionL = pygame.Rect(WIDTH/7, HEIGHT/3, 150, 198)

positionR = pygame.Rect(WIDTH-2*WIDTH/7, HEIGHT/3, 150, 198)


# Main Code

resize_monsters()




def main(player1, player2):
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    # light shade of the button
    color_light = (170,170,170)

    # dark shade of the button
    color_dark = (100,100,100)

    # white color
    color = (255,255,255)

    smallfont = pygame.font.SysFont('Corbel',35)

    button_fonts_m1 = []
    for i in player1.monster.moves:
        button_fonts_m1.append(smallfont.render(i , True , color))
    button_fonts_m1.append(smallfont.render("Surrender" , True , color))


    button_fonts_m2 = []
    for j in player2.monster.moves:
        button_fonts_m2.append(smallfont.render(j , True , color))
    button_fonts_m2.append(smallfont.render("Surrender" , True , color))


    my_sprite_looking_right = MySprite(player1)
    my_sprite_looking_left = MySprite(player2)
    my_group = pygame.sprite.Group(my_sprite_looking_right, my_sprite_looking_left)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()

        screen.blit(BACKGROUND_PICTURE, [0,0])

        button_1_loc = [WIDTH/7,4*HEIGHT/5,WIDTH/4,HEIGHT/18]
        button_2_loc = [WIDTH/7,7*HEIGHT/8,WIDTH/4,HEIGHT/18]
        button_3_loc = [WIDTH/7 + 3*WIDTH/7,4*HEIGHT/5,WIDTH/4,HEIGHT/18]
        button_4_loc = [WIDTH/7 + 3*WIDTH/7,7*HEIGHT/8,WIDTH/4,HEIGHT/18]
        line_loc = [0,3*HEIGHT/4,160,70]

        #surface, color, start_pos, end_pos, width
        pygame.draw.line(screen, color_dark,[0,3*HEIGHT/4], [WIDTH,3*HEIGHT/4], 8)
        pygame.draw.rect(screen,color_dark,button_1_loc)
        pygame.draw.rect(screen,color_dark,button_2_loc)
        pygame.draw.rect(screen,color_dark,button_3_loc)
        pygame.draw.rect(screen,color_dark,button_4_loc)

        text_locations = []
        text_locations.append([3*button_1_loc[0]/2,button_1_loc[1]])
        text_locations.append([3*button_2_loc[0]/2,button_2_loc[1]])
        text_locations.append([9*WIDTH/14,button_3_loc[1]])
        text_locations.append([9*WIDTH/14,button_4_loc[1]])


        # if players 1 turn

        for i in range(len(button_fonts_m1)):
            screen.blit(button_fonts_m1[i], text_locations[i])

        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)






my_eagle = m.Eagle()

my_ent = m.Ent()

my_devil = m.Devil()

my_naga = m.Naga()



p1 = p.Player(1, my_naga, "Patryk")
p2 = p.Player(2, my_devil, "Sotiris")


main(p1,p2)


# #def monster_turn(monster):
#
# Eagle_turn =True
# Ent_turn = False
#
# while True:
#   if Eagle_turn ==True:
#     for ev in py.event.get():
#
#         if ev.type == py.QUIT:
#             py.quit()
#
#         #checks if a mouse is clicked
#         if ev.type == py.MOUSEBUTTONDOWN:
#
#             #if the mouse is clicked on the
#             # button the game is terminated
#             if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]:
#                 monster1.quick_attack(monster2)
#                 print(monster2.hp)
#                 Ent_turn = True
#                 Eagle_turn =False
#
#
#
#             if button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]:
#                 print(monster2.hp)
#                 monster1.dive_attack(monster2)
#                 print(monster2.hp)
#                 Ent_turn = True
#                 Eagle_turn =False
#
#
#
#             if button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]:
#                 print(monster2.hp)
#                 monster1.wing_slash(monster2)
#                 print(monster2.hp)
#                 Ent_turn = True
#                 Eagle_turn =False
#
#
#     # fills the screen with a color
#     screen.fill((60,25,60))
#
#     # stores the (x,y) coordinates into
#     # the variable as a tuple
#     mouse = py.mouse.get_pos()
#
#
#     # if mouse is hovered on a button it
#     # changes to lighter shade
#     if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]:
#         py.draw.rect(screen,color_light,button_1_loc)
#
#     elif button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]:
#         py.draw.rect(screen,color_light,button_2_loc)
#
#     elif button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]:
#         py.draw.rect(screen,color_light,button_3_loc)
#
#     else:
#         py.draw.rect(screen,color_dark,button_1_loc )
#         py.draw.rect(screen,color_dark,button_2_loc )
#         py.draw.rect(screen,color_dark,button_3_loc )
#
#
#     # superimposing the text onto our button
#     screen.blit(attack_1_mon_1 ,(button_1_loc[0],button_1_loc[1]))
#     screen.blit(attack_2_mon_1 ,(button_2_loc[0],button_2_loc[1]))
#     screen.blit(attack_3_mon_1 ,(button_3_loc[0],button_3_loc[1]))
#
#
#     # updates the frames of the game
#     py.display.update()
#
#   elif Ent_turn  ==True:
#     for ev in py.event.get():
#
#         if ev.type == py.QUIT:
#             py.quit()
#
#         #checks if a mouse is clicked
#         if ev.type == py.MOUSEBUTTONDOWN:
#
#             #if the mouse is clicked on the
#             # button the game is terminated
#             if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]:
#                 monster2.stomp(monster1)
#                 print(monster1.hp)
#                 Ent_turn = False
#                 Eagle_turn =True
#
#
#
#             if button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]:
#                 monster2.stomp(monster1)
#                 print(monster1.hp)
#                 Ent_turn = False
#                 Eagle_turn =True
#
#
#
#             if button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]:
#                 monster2.vine_whip(monster1)
#                 print(monster1.hp)
#                 Ent_turn = False
#                 Eagle_turn = True
#
#
#     # fills the screen with a color
#     screen.fill((60,25,60))
#
#     # stores the (x,y) coordinates into
#     # the variable as a tuple
#     mouse = py.mouse.get_pos()
#
#
#     # if mouse is hovered on a button it
#     # changes to lighter shade
#     if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]:
#         py.draw.rect(screen,color_light,button_1_loc)
#
#     elif button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]:
#         py.draw.rect(screen,color_light,button_2_loc)
#
#     elif button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]:
#         py.draw.rect(screen,color_light,button_3_loc)
#
#     else:
#         py.draw.rect(screen,color_dark,button_1_loc )
#         py.draw.rect(screen,color_dark,button_2_loc )
#         py.draw.rect(screen,color_dark,button_3_loc )
#
#
#     # superimposing the text onto our button
#     screen.blit(attack_1_mon_2 ,(button_1_loc[0],button_1_loc[1]))
#     screen.blit(attack_2_mon_2 ,(button_2_loc[0],button_2_loc[1]))
#     screen.blit(attack_3_mon_2 ,(button_3_loc[0],button_3_loc[1]))
#
#
#     # updates the frames of the game
#     py.display.update()
