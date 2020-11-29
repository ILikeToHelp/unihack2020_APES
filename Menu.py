import pygame,sys
import GUI as our_game
import Player as p
import Monsters
width = 1280
height = 720
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([width,height])
base_font = pygame.font.Font(None,32)
start_button_font = pygame.font.Font(None,42)
background_image = pygame.image.load("pics/menunew.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))
Player_1_text = ['Player 1', 'Insert P1 name']
Player_2_text = ['Player 2', 'Insert P2  name']

monster_options = ['Eagle','Treebeard','Devil','Naga']







input_rect_player_1 = pygame.Rect(125,200,180,32)
input_rect_player_2 = pygame.Rect(800,200,180,32)

input_rect_player1_monster_1 = pygame.Rect(125,350,180,32)
input_rect_player1_monster_2 = pygame.Rect(125,400,180,32)
input_rect_player1_monster_3 = pygame.Rect(125,450,180,32)
input_rect_player1_monster_4 = pygame.Rect(125,500,180,32)

input_rect_player2_monster_1 = pygame.Rect(800,350,180,32)
input_rect_player2_monster_2 = pygame.Rect(800,400,180,32)
input_rect_player2_monster_3 = pygame.Rect(800,450,180,32)
input_rect_player2_monster_4 = pygame.Rect(800,500,180,32)


rect_start_button = pygame.Rect(width/2-150,600,180,50)

color = pygame.Color('lightskyblue3')
color_light = (170,170,170)
color_selected = 'navyblue'


color_p1_m1 = color
color_p1_m2 = color
color_p1_m3 = color
color_p1_m4 = color
color_p2_m1 = color
color_p2_m2 = color
color_p2_m3 = color
color_p2_m4 = color

user_one_input =True
mouse_pos = [0,0]
start_typing_p1 = False
start_typing_p2 = False


player_1_mon_choice = 0
player_2_mon_choice = 0

player_1_has_made_name_choice = False
player_2_has_made_name_choice = False

player_1_has_made_mon_choice = False
player_2_has_made_mon_choice = False



GAMESTART = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_typing_p1 ==False:

         if event.type == pygame.MOUSEBUTTONDOWN:




            if (input_rect_player_1.x <= mouse_pos[0]<= input_rect_player_1.x+input_rect_player_1.width) and (input_rect_player_1.y <= mouse_pos[1]<= input_rect_player_1.y+input_rect_player_1.height):
                start_typing_p1 = True



            elif (input_rect_player1_monster_1.x <= mouse_pos[0]<= input_rect_player1_monster_1.x+input_rect_player1_monster_1.width) and (input_rect_player1_monster_1.y <= mouse_pos[1]<= input_rect_player1_monster_1.y+input_rect_player1_monster_1.height):

                    player_1_mon_choice = monster_options[0]
                    print('P1 chose '+player_1_mon_choice)
                    player_1_has_made_mon_choice = True
                    color_p1_m1 = color_selected
                    color_p1_m2 = color
                    color_p1_m3 = color
                    color_p1_m4 = color



            elif (input_rect_player1_monster_2.x <= mouse_pos[0]<= input_rect_player1_monster_2.x+input_rect_player1_monster_2.width) and (input_rect_player1_monster_2.y <= mouse_pos[1]<= input_rect_player1_monster_2.y+input_rect_player1_monster_2.height):
                    player_1_mon_choice = monster_options[1]
                    print('P1 chose '+player_1_mon_choice)
                    player_1_has_made_mon_choice = True
                    color_p1_m2 = color_selected
                    color_p1_m1 = color
                    color_p1_m3 = color
                    color_p1_m4 = color

            elif (input_rect_player1_monster_3.x <= mouse_pos[0]<= input_rect_player1_monster_3.x+input_rect_player1_monster_3.width) and (input_rect_player1_monster_3.y <= mouse_pos[1]<= input_rect_player1_monster_3.y+input_rect_player1_monster_3.height):
                    player_1_mon_choice = monster_options[2]
                    print('P1 chose '+player_1_mon_choice)
                    player_1_has_made_mon_choice = True
                    color_p1_m3 = color_selected
                    color_p1_m1 = color
                    color_p1_m2 = color
                    color_p1_m4 = color

            elif (input_rect_player1_monster_4.x <= mouse_pos[0]<= input_rect_player1_monster_4.x+input_rect_player1_monster_4.width) and (input_rect_player1_monster_4.y <= mouse_pos[1]<= input_rect_player1_monster_4.y+input_rect_player1_monster_4.height):
                    player_1_mon_choice = monster_options[3]
                    print('P1 chose '+player_1_mon_choice)
                    player_1_has_made_mon_choice = True
                    color_p1_m4 = color_selected
                    color_p1_m1 = color
                    color_p1_m2 = color
                    color_p1_m3 = color


            elif (input_rect_player2_monster_1.x <= mouse_pos[0]<= input_rect_player2_monster_1.x+input_rect_player2_monster_1.width) and (input_rect_player2_monster_1.y <= mouse_pos[1]<= input_rect_player2_monster_1.y+input_rect_player2_monster_1.height):
                    player_2_mon_choice = monster_options[0]
                    print('P2 chose '+player_2_mon_choice)
                    player_2_has_made_mon_choice = True
                    color_p2_m1 = color_selected
                    color_p2_m2 = color
                    color_p2_m3 = color
                    color_p2_m4 = color

            elif (input_rect_player2_monster_2.x <= mouse_pos[0]<= input_rect_player2_monster_2.x+input_rect_player2_monster_2.width) and (input_rect_player2_monster_2.y <= mouse_pos[1]<= input_rect_player2_monster_2.y+input_rect_player2_monster_2.height):
                    player_2_mon_choice = monster_options[1]
                    print('P2 chose '+player_2_mon_choice)
                    player_2_has_made_mon_choice = True
                    color_p2_m2 = color_selected
                    color_p2_m1 = color
                    color_p2_m3 = color
                    color_p2_m4 = color

            elif (input_rect_player1_monster_3.x <= mouse_pos[0]<= input_rect_player2_monster_3.x+input_rect_player2_monster_3.width) and (input_rect_player2_monster_3.y <= mouse_pos[1]<= input_rect_player2_monster_3.y+input_rect_player2_monster_3.height):
                    player_2_mon_choice = monster_options[2]
                    print('P2 chose '+player_2_mon_choice)
                    player_2_has_made_mon_choice = True
                    color_p2_m3 = color_selected
                    color_p2_m1 = color
                    color_p2_m2 = color
                    color_p2_m4 = color

            elif (input_rect_player2_monster_4.x <= mouse_pos[0]<= input_rect_player2_monster_4.x+input_rect_player2_monster_4.width) and (input_rect_player2_monster_4.y <= mouse_pos[1]<= input_rect_player2_monster_4.y+input_rect_player2_monster_4.height):
                    player_2_mon_choice = monster_options[3]
                    print('P2 chose '+player_2_mon_choice)
                    player_2_has_made_mon_choice = True
                    color_p2_m4 = color_selected
                    color_p2_m1 = color
                    color_p2_m2 = color
                    color_p2_m3 = color


            elif (rect_start_button.x <= mouse_pos[0]<= rect_start_button.x+rect_start_button.width) and (rect_start_button.y <= mouse_pos[1]<= rect_start_button.y+rect_start_button.height):
                    if player_1_has_made_mon_choice and player_1_has_made_name_choice  and player_2_has_made_mon_choice  and player_2_has_made_name_choice:
                        GAMESTART = True
                        player1 = None
                        player2 = None
                        print('GAME START')
                        if(player_1_mon_choice == "Naga"):
                            monster = Monsters.Naga()
                            player1 = p.Player(1, monster, Player_1_text[1])
                        elif(player_1_mon_choice == "Devil"):
                            monster = Monsters.Devil()
                            player1 = p.Player(1, monster, Player_1_text[1])
                        elif(player_1_mon_choice == "Treebeard"):
                            monster = Monsters.Treebeard()
                            player1 = p.Player(1, monster, Player_1_text[1])
                        elif(player_1_mon_choice == "Eagle"):
                            monster = Monsters.Eagle()
                            player1 = p.Player(1, monster, Player_1_text[1])

                        if(player_2_mon_choice == "Naga"):
                            monster = Monsters.Naga()
                            player2 = p.Player(2, monster, Player_2_text[1])
                        elif(player_2_mon_choice == "Devil"):
                            monster = Monsters.Devil()
                            player2 = p.Player(2, monster, Player_2_text[1])
                        elif(player_2_mon_choice == "Treebeard"):
                            monster = Monsters.Treebeard()
                            player2 = p.Player(2, monster, Player_2_text[1])
                        elif(player_2_mon_choice == "Eagle"):
                            monster = Monsters.Eagle()
                            player2 = p.Player(2, monster, Player_2_text[1])

                        our_game.main(player1, player2)



        elif start_typing_p1 ==True:



                if event.type ==  pygame.KEYDOWN:




                    if event.key == pygame.K_BACKSPACE:
                            Player_1_text[1] = Player_1_text[1][0:-1]



                    if event.key == pygame.K_RETURN:

                        start_typing_p1 = False
                        player_1_has_made_name_choice = True


                    else:

                        Player_1_text[1] += event.unicode






        if start_typing_p2 ==False:
             if event.type == pygame.MOUSEBUTTONDOWN:


                if (input_rect_player_2.x <= mouse_pos[0]<= input_rect_player_2.x+input_rect_player_2.width) and (input_rect_player_2.y <= mouse_pos[1]<= input_rect_player_2.y+input_rect_player_2.height):
                    start_typing_p2 = True



        elif start_typing_p2 ==True:


                if event.type ==  pygame.KEYDOWN:




                    if event.key == pygame.K_BACKSPACE:
                            Player_2_text[1] = Player_2_text[1][0:-1]



                    if event.key == pygame.K_RETURN:

                        start_typing_p2 = False
                        player_2_has_made_name_choice = True


                    else:

                        Player_2_text[1] += event.unicode






    screen.fill((0,0,0))
    screen.blit(background_image, [0, 0])

    #Draw rectangles
    pygame.draw.rect(screen,color,input_rect_player_1,2)
    pygame.draw.rect(screen,color,input_rect_player_2,2)

    pygame.draw.rect(screen,color_p1_m1,input_rect_player1_monster_1,0)
    pygame.draw.rect(screen,color_p1_m2,input_rect_player1_monster_2,0)
    pygame.draw.rect(screen,color_p1_m3,input_rect_player1_monster_3,0)
    pygame.draw.rect(screen,color_p1_m4,input_rect_player1_monster_4,0)

    pygame.draw.rect(screen,color_p2_m1,input_rect_player2_monster_1,0)
    pygame.draw.rect(screen,color_p2_m2,input_rect_player2_monster_2,0)
    pygame.draw.rect(screen,color_p2_m3,input_rect_player2_monster_3,0)
    pygame.draw.rect(screen,color_p2_m4,input_rect_player2_monster_4,0)


    pygame.draw.rect(screen,color,rect_start_button,2)


    #Monster options for p1
    text_surface_p1_monster_1 = base_font.render(monster_options[0],False,(255,255,255))
    text_surface_p1_1_monster_2 = base_font.render(monster_options[1],True,(255,255,255))
    text_surface_p1_1_monster_3 = base_font.render(monster_options[2],True,(255,255,255))
    text_surface_p1_1_monster_4 = base_font.render(monster_options[3],True,(255,255,255))



    #Monster options for p2
    text_surface_p2_monster_1 = base_font.render(monster_options[0],False,(255,255,255))
    text_surface_p2_1_monster_2 = base_font.render(monster_options[1],True,(255,255,255))
    text_surface_p2_1_monster_3 = base_font.render(monster_options[2],True,(255,255,255))
    text_surface_p2_1_monster_4 = base_font.render(monster_options[3],True,(255,255,255))

    text_surface_start_button = start_button_font.render('START',True,(255,255,255))

    screen.blit(text_surface_p2_monster_1,[input_rect_player1_monster_1.x+5,input_rect_player1_monster_1.y+5])
    screen.blit(text_surface_p2_1_monster_2,[input_rect_player1_monster_2.x+5,input_rect_player1_monster_2.y+5])
    screen.blit(text_surface_p2_1_monster_3,[input_rect_player1_monster_3.x+5,input_rect_player1_monster_3.y+5])
    screen.blit(text_surface_p2_1_monster_4,[input_rect_player1_monster_4.x+5,input_rect_player1_monster_4.y+5])



    screen.blit(text_surface_p2_monster_1,[input_rect_player2_monster_1.x+5,input_rect_player2_monster_1.y+5])
    screen.blit(text_surface_p2_1_monster_2,[input_rect_player2_monster_2.x+5,input_rect_player2_monster_2.y+5])
    screen.blit(text_surface_p2_1_monster_3,[input_rect_player2_monster_3.x+5,input_rect_player2_monster_3.y+5])
    screen.blit(text_surface_p2_1_monster_4,[input_rect_player2_monster_4.x+5,input_rect_player2_monster_4.y+5])

    screen.blit(text_surface_start_button,[rect_start_button.x+40,rect_start_button.y+10])



    text_surface_p1 = base_font.render(Player_1_text[0],False,(255,255,255))
    text_surface_p1_1 = base_font.render(Player_1_text[1],True,(255,255,255))


    text_surface_p2 = base_font.render(Player_2_text[0],False,(255,255,255))
    text_surface_p2_1 = base_font.render(Player_2_text[1],False,(255,255,255))

    #rectangle 1
    screen.blit(text_surface_p1_1,(input_rect_player_1.x+5,input_rect_player_1.y+5))
    #Rectangle 2

    screen.blit(text_surface_p2_1,(input_rect_player_2.x+5,input_rect_player_2.y+5))

    screen.blit(text_surface_p1,(125,150))


    screen.blit(text_surface_p2,(800,150))
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)



    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
