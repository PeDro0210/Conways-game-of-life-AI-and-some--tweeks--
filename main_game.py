import pygame
from pygame.locals import *
from dot_classes import reddot, bluedot, dot
from game_classes import MiniGrid, button, game_of_life  
from itertools import zip_longest

grid= MiniGrid(10, 1920/16, 1080/8)
window=pygame.display.set_mode((1920,1080))
background=pygame.draw.rect(window,(255,255,255),(0,0,1920,1080),0)
button1=button(350,825,50,0,0,0)


#I have to fix the zip function

blue_dot=[] 
blue_coords=[]
red_dot=[]
red_coords=[]

fill_value_dot=dot(0,0,150,150,150,0,True,[],[],[])
fill_value_coord=[0,0]

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

            
                new_gen_blue=[]
                new_gen_coords_blue=[]
                new_gen_red=[]
                new_gen_coords_red=[]
                
                erase_blue=[]
                erase_coords_blue=[]
                erase_red=[]
                erase_coords_red=[]
                

                for b_dot, r_dot in zip_longest(game.blue_dots, game.red_dots, fillvalue=fill_value_dot):
                    
                    print(b_dot.x, b_dot.y)
                    for wtf_dot in b_dot.same_neigbor:
                       wtf_dot.draw(window)
                    
                    
                    
                    intersection=game.inteserction_betwean_dots_blue(b_dot)     
                    intersection_r=game.inteserction_betwean_dots_red(r_dot)
                    
                    if None != intersection: 
                        for j in intersection:
                            new_dot_b=bluedot(j[0],j[1],0,0,255,4,True,[],[],[])
                            new_gen_blue.append(new_dot_b)
                            new_gen_coords_blue.append([new_dot_b.x,new_dot_b.y])
                            draw=new_dot_b.draw(window)
                            print(new_dot_b.same_neigbor)
                            
                    
                    if None != intersection_r:
                        for i in intersection_r:
                            new_dot_r=reddot(i[0],i[1],255,0,0,4,True,[],[],[])
                            new_gen_red.append(new_dot_r)
                            new_gen_coords_red.append([new_dot_r.x,new_dot_r.y])
                            draw_2=new_dot_r.draw(window)
                            print(new_dot_b.same_neigbor)
                            

                    b_dot.point_state()
                    r_dot.point_state()
            

                    if b_dot.state:
                        pass
                    else:
                        erase_blue.append(b_dot)
                        erase_coords_blue.append([b_dot.x,b_dot.y])
                        b_dot.remove(window)
                    
                    if r_dot.state:
                        pass
                    else:
                        erase_red.append(r_dot)
                        erase_coords_red.append([r_dot.x,r_dot.y])
                        r_dot.remove(window)
                
                

                for new_blue in new_gen_blue:
                    game.blue_dots.append(new_blue)

                for new_b_coords in new_gen_coords_blue:
                    game.blue_coords.append(new_b_coords)

                for new_red in new_gen_red:
                    game.red_dots.append(new_red)

                for new_r_coords in new_gen_coords_red:
                    game.red_coords.append(new_r_coords)

                for erase_b in erase_blue:
                    if erase_b in game.blue_dots:
                        game.blue_dots.remove(erase_b)

                for erase_b_coords in erase_coords_blue:
                    if erase_b_coords in game.blue_coords:
                        game.blue_coords.remove(erase_b_coords)

                for erase_r in erase_red:
                    if erase_r in game.red_dots:
                        game.red_dots.remove(erase_r)

                for erase_r_coords in erase_coords_red:
                    if erase_r_coords in game.red_coords:
                        game.red_coords.remove(erase_r_coords)


                
                print('dots erase')
                
                    
                    




                        

                    
    MiniGrid.draw(grid, window) 
    pygame.display.update()