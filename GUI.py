# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:36:21 2020

@author: Marc
"""

import pygame
from PIL import Image
import Monsters as m
import Player as p
import sys

SIZE = WIDTH, HEIGHT = 1920, 1080#the width and height of our screen
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
            elif(player.monster.name == "Treebeard"):
                self.images.append(pygame.image.load('pics/resizedTreebeardL1.png'))
                self.images.append(pygame.image.load('pics/resizedTreebeardL2.png'))
                self.images.append(pygame.image.load('pics/resizedTreebeardL3.png'))
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
            elif(player.monster.name == "Treebeard"):
                self.images.append(pygame.image.load('pics/resizedTreebeardR1.png'))
                self.images.append(pygame.image.load('pics/resizedTreebeardR2.png'))
                self.images.append(pygame.image.load('pics/resizedTreebeardR3.png'))



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


    #EAGLE
    resize_image("EagleL1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleL2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleL3.png", int(WIDTH/6), int(HEIGHT/3))

    resize_image("EagleR1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleR2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("EagleR3.png", int(WIDTH/6), int(HEIGHT/3))


    #TREEBEARD
    resize_image("TreebeardL1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("TreebeardL2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("TreebeardL3.png", int(WIDTH/6), int(HEIGHT/3))

    resize_image("TreebeardR1.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("TreebeardR2.png", int(WIDTH/6), int(HEIGHT/3))
    resize_image("TreebeardR3.png", int(WIDTH/6), int(HEIGHT/3))

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


def playerOneFlees():
    print("PLAYER ONE IS A PUSSSY-A CAT I MEAN> SMALL CAT")
    sys.exit()

def playerTwoFlees():
    print("PLAYER TWO IS A PUSSSY-A CAT I MEAN> SMALL CAT")
    sys.exit()

def main(player1, player2):

    PlayerOneTurn = True

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
        mouse = pygame.mouse.get_pos()
        button_1_loc = [WIDTH/7,4*HEIGHT/5,WIDTH/4,HEIGHT/18]
        button_2_loc = [WIDTH/7,7*HEIGHT/8,WIDTH/4,HEIGHT/18]
        button_3_loc = [WIDTH/7 + 3*WIDTH/7,4*HEIGHT/5,WIDTH/4,HEIGHT/18]
        button_4_loc = [WIDTH/7 + 3*WIDTH/7,7*HEIGHT/8,WIDTH/4,HEIGHT/18]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the first button is clicked, perform quick attack
                if button_1_loc[0] <= mouse[0] <= button_1_loc[0]+ button_1_loc[2] and button_1_loc[1] <= mouse[1] <= button_1_loc[1]+button_1_loc[3]:
                    pygame.draw.rect(screen,color_light,button_1_loc)

                    if(PlayerOneTurn):
                        # if it's players one turn, print the values
                        print("Monsters " + player2.monster.name + " old hp was: " + str(player2.monster.hp))
                        # and call the corresponding functions
                        player1.monster.quick_attack(player2.monster)
                        print("Monsters " + player2.monster.name + " new hp is: " + str(player2.monster.hp))
                        PlayerOneTurn = False
                    else:
                        #reverse is true
                        print("Monsters " + player1.monster.name + " old hp was: " + str(player1.monster.hp))
                        player2.monster.quick_attack(player1.monster)
                        print("Monsters " + player1.monster.name + " new hp is: " + str(player1.monster.hp))
                        PlayerOneTurn = True
                if button_2_loc[0] <= mouse[0] <= button_2_loc[0]+ button_2_loc[2] and button_2_loc[1] <= mouse[1] <= button_2_loc[1]+button_2_loc[3]:
                    pygame.draw.rect(screen,color_light,button_2_loc)
                    if(PlayerOneTurn):
                        # if it's players one turn, print the values
                        print("Monsters " + player2.monster.name + " old hp was: " + str(player2.monster.hp))
                        if(player1.monster.name == "Naga"):
                            player1.monster.aqua_pulse(player2.monster)
                        elif(player1.monster.name == "Treebeard"):
                            player1.monster.stomp(player2.monster)
                        elif(player1.monster.name == "Eagle"):
                            player1.monster.dive_attack(player2.monster)
                        elif(player1.monster.name == "Devil"):
                            player1.monster.hellflame(player2.monster)
                        print("Monsters " + player2.monster.name + " new hp is: " + str(player2.monster.hp))
                        PlayerOneTurn = False
                    else:
                        # if it's players one turn, print the values
                        print("Monsters " + player1.monster.name + " old hp was: " + str(player1.monster.hp))
                        if(player2.monster.name == "Naga"):
                            player2.monster.aqua_pulse(player1.monster)
                        elif(player2.monster.name == "Treebeard"):
                            player2.monster.stomp(player1.monster)
                        elif(player2.monster.name == "Eagle"):
                            player2.monster.dive_attack(player1.monster)
                        elif(player2.monster.name == "Devil"):
                            player2.monster.hellflame(player1.monster)
                        print("Monsters " + player1.monster.name + " new hp is: " + str(player1.monster.hp))
                        PlayerOneTurn = True
                if button_3_loc[0] <= mouse[0] <= button_3_loc[0]+ button_3_loc[2] and button_3_loc[1] <= mouse[1] <= button_3_loc[1]+button_3_loc[3]:
                    pygame.draw.rect(screen,color_light,button_3_loc)
                    if(PlayerOneTurn):
                        # if it's players one turn, print the values
                        print("Monsters " + player2.monster.name + " old hp was: " + str(player2.monster.hp))
                        if(player1.monster.name == "Naga"):
                            player1.monster.rainstorm(player2.monster)
                        elif(player1.monster.name == "Treebeard"):
                            player1.monster.vine_whip(player2.monster)
                        elif(player1.monster.name == "Eagle"):
                            player1.monster.wing_slash(player2.monster)
                        elif(player1.monster.name == "Devil"):
                            player1.monster.ash_cloud(player2.monster)
                        print("Monsters " + player2.monster.name + " new hp is: " + str(player2.monster.hp))
                        PlayerOneTurn = False
                    else:
                        # if it's players one turn, print the values
                        print("Monsters " + player1.monster.name + " old hp was: " + str(player1.monster.hp))
                        if(player2.monster.name == "Naga"):
                            player2.monster.rainstorm(player1.monster)
                        elif(player2.monster.name == "Treebeard"):
                            player2.monster.vine_whip(player1.monster)
                        elif(player2.monster.name == "Eagle"):
                            player2.monster.wing_slash(player1.monster)
                        elif(player2.monster.name == "Devil"):
                            player2.monster.ash_cloud(player1.monster)
                        print("Monsters " + player1.monster.name + " new hp is: " + str(player1.monster.hp))
                        PlayerOneTurn = True
                if button_4_loc[0] <= mouse[0] <= button_4_loc[0]+ button_4_loc[2] and button_4_loc[1] <= mouse[1] <= button_4_loc[1]+button_4_loc[3]:
                    pygame.draw.rect(screen,color_light,button_1_loc)

                    if(PlayerOneTurn):
                        playerOneFlees()
                    else:
                        playerTwoFlees()

            pygame.display.update()
        my_group.update()

        screen.blit(BACKGROUND_PICTURE, [0,0])


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
        if(PlayerOneTurn):
            for i in range(len(button_fonts_m1)):
                screen.blit(button_fonts_m1[i], text_locations[i])
        else:
            for i in range(len(button_fonts_m2)):
                screen.blit(button_fonts_m2[i], text_locations[i])

        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)






my_eagle = m.Eagle()

my_treebeard = m.Treebeard()

my_devil = m.Devil()

my_naga = m.Naga()



p1 = p.Player(1, my_eagle, "Patryk")
p2 = p.Player(2, my_treebeard, "Sotiris")


main(p1,p2)
