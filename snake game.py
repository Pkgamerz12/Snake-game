import time
import pygame
import random

pygame.init()
clock= pygame.time.Clock()

white = (255,255,255)
black =(0,0,0)
red =(255,0,0)
green =(0,255,0)
block_size = 20

font = pygame.font.SysFont(None,100)

def snake(block_size,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay,black,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()
    

def messege_on_screen(msg,color,y_display = 0):
    #screen_text= font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[450,500])
    textSurf,textRect= text_objects(msg,color)
    textRect.center= 550,500 - y_display
    gameDisplay.blit(textSurf,textRect)


gameDisplay= pygame.display.set_mode((900,1000))



def gameloop():
    food_x= random.randrange(0,1050,30)
    food_y= random.randrange(0,840,30)
    running =True
    gameover = False
    lead_x = 300
    lead_y= 300
    button_left=0
    button_right=0
    xspeed =0
    yspeed =0
    snakelist = []
    snakelenght = 1
    
    while running:
        while gameover == True:
            gameDisplay.fill(white)
            messege_on_screen("game over",red)
            messege_on_screen("Touch the screen to play again",black,-100)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    press_check = pygame.mouse.get_pos()
                    toch_x,toch_y = press_check
                    if toch_x > 0 and toch_y > 0:
                        running = True
                        gameover = False
                        gameloop()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running =False
            if event.type== pygame.MOUSEBUTTONDOWN:
                touch_pos = pygame.mouse.get_pos()
                button_left,button_right= touch_pos
                if button_left<350 and button_right<1600 and button_right >1250:
                    xspeed = -10
                    yspeed = 0
                elif button_left>700 and button_right<1600 and button_right>1250:
                    xspeed = 10
                    yspeed= 0
                elif button_left>350 and button_left<700 and button_right>900 and button_right<1250:
                    yspeed = -10
                    xspeed =0
                elif button_left>350 and button_left<700 and button_right>1600 and button_right<1950:
                    yspeed = 10
                    xspeed =0
        if lead_x >= 1025 or lead_x <= 0 or lead_y >= 840 or lead_y <= 0:
            gameover = True
            
                
            
               
                
            
        lead_x += xspeed
        lead_y += yspeed
                
                
                
        applethickness = 30       
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,red,(food_x,food_y,applethickness,applethickness))
        
        
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        
        if len(snakelist) > snakelenght:
            del snakelist[0]
        for snakesegment in snakelist[: -1]:
            if snakesegment == snakehead:
                gameover = True
        
        snake(block_size,snakelist)
        
        pygame.draw.line(gameDisplay,black,(350,900),(350,1950))
        pygame.draw.line(gameDisplay,black,(700,900),(700,1950))
        pygame.draw.line(gameDisplay,black,(50,1250),(1050,1250))
        pygame.draw.line(gameDisplay,black,(50,1600),(1050,1600))
        pygame.display.update()
        if lead_x  > food_x  and lead_x < food_x  + applethickness or lead_x + block_size > food_x and lead_x+ block_size < food_x + applethickness:
            if lead_y > food_y and lead_y < food_y + applethickness or lead_y + block_size > food_y and lead_y + block_size < food_y + applethickness:
        
    
                food_x= random.randrange(20,1000,10)
                food_y= random.randrange(20,800,10)
                snakelenght += 1
            
        
        
        
        
        
      
        clock.tick(30)
                
                
                
    messege_on_screen("you suck",black)    
    pygame.display.update()  
    pygame.quit()
    quit()
gameloop()