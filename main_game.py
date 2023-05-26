import pygame
from pygame.locals import *
from dot_classes import reddot, bluedot
from game_classes import MiniGrid, button, game_of_life  
import os

grid= MiniGrid(10, 1920/16, 1080/8)
window=pygame.display.set_mode((1920,1080))
background=pygame.draw.rect(window,(255,255,255),(0,0,1920,1080),0)
button1=button(350,825,50,0,0,0)

blue_dot=[]
blue_coords=[]
red_dot=[]
red_coords=[]



#main loop  
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        mouse_pos = pygame.mouse.get_pos()
        button1.draw(window)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if grid.clicked_death_point(mouse_pos,window):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    
                    punto_blue = bluedot(mouse_pos, mouse_pos, 0, 0, 255, 4, True , [],[],[])
                    point_blue=punto_blue.center_snap(grid.clicked_death_point(mouse_pos,window)[1:])

                    
                    if point_blue not in blue_coords:
                        blue_coords.append(point_blue)# I'm really thinking if is really necessary to have an specif array for the coords, this was made in a pretty early stage
                        blue_dot.append(punto_blue)
                        punto_blue.draw(window)
                    else:
                        print('not valid')
                 
                #same shit        
                if keys[pygame.K_k]:
                    
                    punto_red = reddot(mouse_pos, mouse_pos, 255, 0, 0, 4,True ,[],[],[])
                    point_red=punto_red.center_snap(grid.clicked_death_point(mouse_pos,window)[1:])
                          
                    if point_red not in red_coords:
                        red_coords.append(point_red)
                        red_dot.append(punto_red)
                        punto_red.draw(window)
                    else:
                        print('not valid')



            if button1.clicked(mouse_pos):
                print('clicked' )
                game=game_of_life(blue_dot,red_dot,blue_coords,red_coords)
                game.neighboar_checking() #dude, leave this here, it would start with the main loop    
                #I was just trying how did the state atributes worked, it worked pretty well



                for b_dot, r_dot in zip(game.blue_dots, game.red_dots):
                    
                
                    
                       
                    
                    intersection=game.inteserction_betwean_dots_blue(b_dot)     
                    intersection_r=game.inteserction_betwean_dots_red(r_dot)
                    
                    
                    if None != intersection: 
                        print(intersection) 
                        new_dot_b=bluedot(intersection[0],intersection[1],0,0,255,4,True,[],[],[])
                        print(new_dot_b.x,new_dot_b.y)
                        game.blue_dots.append(new_dot_b)
                        game.blue_coords.append([new_dot_b.x,new_dot_b.y])
                        draw=new_dot_b.draw(window)
                        print(draw)
                            
                    
                    if None != intersection_r:
                        print(intersection_r)
                        new_dot_r=reddot(intersection_r[0],intersection_r[1],255,0,0,4,True,[],[],[])
                        print(new_dot_r.x,new_dot_r.y)
                        game.red_dots.append(new_dot_r)
                        game.red_coords.append([new_dot_r.x,new_dot_r.y])
                        draw_2=new_dot_r.draw(window)
                        print(draw_2)
                    
                    
                    # b_dot.point_state()#this is conflicting with the new generations
                    # r_dot.point_state()#this is conflicting with the new generations
             

                    if b_dot.state:
                        pass
                    else:
                        game.blue_coords.remove([b_dot.x,b_dot.y])
                        b_dot.remove(window)
                        
                    
                    if r_dot.state:
                        pass
                    else:
                        game.red_coords.remove([r_dot.x,r_dot.y])
                        r_dot.remove(window)

                        

                    
    MiniGrid.draw(grid, window) 
    pygame.display.update()