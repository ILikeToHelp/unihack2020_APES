# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:36:21 2020

@author: Marc
"""

import pygame
from PIL import image

SIZE = WIDTH, HEIGHT = 1280, 720 #the width and height of our screen
BACKGROUND_PICTURE = pygame.image.load('bg.png') #https://www.deviantart.com/drboxhead/art/Avatar-The-Last-Airbender-Wallpaper-750669085
BACKGROUND_PICTURE = pygame.transform.scale(BACKGROUND_PICTURE, SIZE)

FPS = 10 #Frames per second



class MySprite(pygame.sprite.Sprite):
    def __init__(self, left):
        super(MySprite, self).__init__()

        self.images = []
        self.rect = None

        self.imagesL = []
        self.imagesL.append(pygame.image.load(ImageL1))
        self.imagesL.append(pygame.image.load(ImageL2))
        self.imagesL.append(pygame.image.load(ImageL3))

        self.imagesR = []
        self.imagesR.append(pygame.image.load(ImageR1))
        self.imagesR.append(pygame.image.load(ImageR2))
        self.imagesR.append(pygame.image.load(ImageR3))

        if left is False:
            self.images = self.imagesL
            self.rect = positionL

        else:
            self.images = self.imagesR
            self.rect = positionR


        self.index = 0

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite_looking_right = MySprite(False)
    my_sprite_looking_left = MySprite(True)
    my_group = pygame.sprite.Group(my_sprite_looking_right, my_sprite_looking_left)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.blit(BACKGROUND_PICTURE, [0,0])
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)






# Define for now (httpswww.kindpng.comimgvhmmwJxR_eagle-sprite-sheet-png-transparent-png)

# ImageL1 = 'EagleL1.png'
# ImageL2 = 'EagleL2.png'
# ImageL3 = 'EagleL3.png'

# ImageR1 = 'EagleR1.png'
# ImageR2 = 'EagleR2.png'
# ImageR3 = 'EagleR3.png'



# Define for now (https://broseoseike.wordpress.com/tag/sprite-sheet/#jp-carousel-(406)

# ImageL1 = 'EntL1.png'
# ImageL2 = 'EntL2.png'
# ImageL3 = 'EntL3.png'

# ImageR1 = 'EntR1.png'
# ImageR2 = 'EntR2.png'
# ImageR3 = 'EntR3.png'



# Define for now (https://www.coroflot.com/geekbrush/Wicked-Little-Devil)

# ImageL1 = 'DevilL1.png'
# ImageL2 = 'DevilL2.png'
# ImageL3 = 'DevilL3.png'

# ImageR1 = 'DevilR1.png'
# ImageR2 = 'DevilR2.png'
# ImageR3 = 'DevilR3.png'


#Define for now (https://broseoseike.files.wordpress.com/2009/04/naga.png)

# ImageL1 = 'NagaL1.png'
# ImageL2 = 'NagaL2.png'
# ImageL3 = 'NagaL3.png'
#
# ImageR1 = 'NagaR1.png'
# ImageR2 = 'NagaR2.png'
# ImageR3 = 'NagaR3.png'



def resize_monsters():

    resize_image("Jumped.png", int(width/10), int(height/7))
    resize_image("ReadyToJump.png", int(width/12), int(height/7))
    resize_image("ReadyToJumpL.png", int(width/12), int(height/7))
    resize_image("Crouch.png", int(width/10), int(height/10))
    resize_image("CrouchL.png", int(width/10), int(height/10))

    resize_image("PlayerStatic.png", int(width/10), int(height/5))
    resize_image("PlayerStep1.png", int(width/10), int(height/5))

    resize_image("PlayerStep2.png", int(width/10), int(height/5))
    resize_image("PlayerStep3.png", int(width/10), int(height/5))

    resize_image("PlayerStaticL.png", int(width/10), int(height/5))
    resize_image("PlayerStep1L.png", int(width/10), int(height/5))
    resize_image("PlayerStep2L.png", int(width/10), int(height/5))
    resize_image("PlayerStep3L.png", int(width/10), int(height/5))

    resize_image("Kick.png", int(width/7), int(height/6))
    resize_image("KickL.png", int(width/7), int(height/6))

    resize_image("RPunch.png", int(width/14), int(height/7))
    resize_image("RPunchL.png", int(width/14), int(height/7))

    resize_image("Punch.png", int(width/10), int(height/7))
    resize_image("PunchL.png", int(width/10), int(height/7))


def resize_image(name, desiredWidth, desiredHeigh):
    # source: https://gph.is/1cmXeXT
    img = Image.open("Pics/" + name)
    img = img.resize((desiredWidth, desiredHeigh), Image.ANTIALIAS)
    img.save("Pics/resized" + name)


# Define Position of bird

positionL = pygame.Rect(5, 5, 150, 198)

positionR = pygame.Rect(410, 5, 150, 198)


# Main Code

main()





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
