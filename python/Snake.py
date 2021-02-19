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

snake_block=10 #size of block
snake_speed=30

clock = pygame.time.Clock()

font_style=pygame.font.SysFont(None, 20)

def message(msg,color):
    mesg= font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameLoop(): #creating a function
    game_over = False
    game_close = False
    
    x1=dis_width/2
    y1=dis_height/2

    x1_change=0 #give starting point change in motion
    y1_change=0 #makes snake go fasttt

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0 ) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0 ) * 10.0

    while not game_over:
        
        while game_close == True:
            dis.fill(black)
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
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            game_close=True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block]) #Sets the red dot/rectangle
        pygame.draw.rect(dis,blue,[x1,y1,snake_block,snake_block]) #sets the starting point with a blue color/snake
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yeet.") # has code acknowledge food


        clock.tick(snake_speed)

#message("You lost", red)
#pygame.display.update()
#time.sleep(2)

    pygame.quit()
    quit()

gameLoop()