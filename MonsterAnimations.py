# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:36:21 2020

@author: Marc
"""

import pygame
 

SIZE = WIDTH, HEIGHT = 700, 550 #the width and height of our screen
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

ImageL1 = 'NagaL1.png'
ImageL2 = 'NagaL2.png'
ImageL3 = 'NagaL3.png'

ImageR1 = 'NagaR1.png'
ImageR2 = 'NagaR2.png'
ImageR3 = 'NagaR3.png'





# Define Position of bird

positionL = pygame.Rect(5, 5, 150, 198)

positionR = pygame.Rect(410, 5, 150, 198)


# Main Code

main()









