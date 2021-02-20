#For scripting class. bintzhm, referenced edureka

import pygame
import time
import random
pygame.init()


dis_width = 800 #sets border of game
dis_height = 600


dis=pygame.display.set_mode((dis_width,dis_width)) #Sets screen size in pixels
pygame.display.set_caption('Snake by Madison Bintz') #Displays name at the window browser

blue=(0,0,255) #have colors
red=(255,0,0)
black=(0,0,0)
lightPurple=(200,191,231)
Purple=(63,72,204)
darkBlue=(0,162,232)

snake_block=10 #size of block
snake_speed=20

clock = pygame.time.Clock()

font_style= pygame.font.SysFont(None, 20)
score_font = pygame.font.SysFont(None, 20)

def score(score):
    value = score_font.render("Score: " + str(score), True, darkBlue) #displays score
    dis.blit(value, [0, 0])

def snakeline(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, Purple, [x[0], x[1], snake_block, snake_block]) #Grow the SNAKE

def message(msg,color):
    mesg= font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop(): #creating a function
    game_over = False
    game_close = False
    
    x1=dis_width/2
    y1=dis_height/2

    x1_change=0 #give starting point change in motion
    y1_change=0 #makes snake go fasttt

    snake_list = []
    Length_of_snake = 1 #sets starting size of snake
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0 ) * 10.0 #make the fooooooood
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0 ) * 10.0

    while not game_over:
        
        while game_close == True:
            dis.fill(lightPurple)
            message("You lost. Press 'q' to Quit and press 'p' to Play again.", red) # give users option to play again or not
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #has q quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p: # has p play again
                        gameLoop()


        for event in pygame.event.get():
            if event.type==pygame.QUIT: #allows you to quit the game
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #if presses left key
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #if presses right key
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: #If presses up key
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN: #If presses down key
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0: #no hitting the borderrr
            game_close=True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(lightPurple)
        pygame.draw.rect(dis,darkBlue,[foodx,foody,snake_block,snake_block]) #Sets the red dot/rectangle
        
        snake_head = []
        snake_head.append(x1) #make bigger
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]
            
        for x in snake_list[:-1]: #this is where the snake will have you lose if you hit the snake
                if x == snake_head:
                    game_close = True
            
        snakeline(snake_block, snake_list)
        score(Length_of_snake - 1)
        
        #pygame.draw.rect(dis,blue,[x1,y1,snake_block,snake_block]) #sets the starting point with a blue color/snake
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0 ) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0 ) * 10.0
            Length_of_snake += 1
            print("Yeet.") # has code acknowledge food


        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()