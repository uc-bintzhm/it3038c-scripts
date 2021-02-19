import pygame
import time
import random
pygame.init()


dis_width = 800 #sets border of game
dis_height = 600


dis=pygame.display.set_mode((dis_width,dis_width)) #Sets screen size in pixels
pygame.display.update()
pygame.display.set_caption('Snake by Madison Bintz') #Displays name at the window browser

game_over=False

blue=(0,0,255) #have colors
red=(255,0,0)
black=(0,0,0)

snake_block=10 #size of block

clock = pygame.time.Clock()
snake_speed=30

font_style=pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg= font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

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
            game_over=True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block]) #Sets the red dot/rectangle
        pygame.draw.rect(dis,blue,[x1,y1,snake_block,snake_block]) #sets the starting point with a blue color/snake
        
        pygame.display.update()

        clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()