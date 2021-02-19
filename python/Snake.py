import pygame
pygame.init()

dis_width = 800 #sets border of game
dis_height = 600


dis=pygame.display.set_mode((dis_width,dis_height)) #Sets screen size in pixels
pygame.display.update()
pygame.display.set_caption('Snake') #Displays name at the window browser
game_over=False

blue=(0,0,255) #have colors
red=(255,0,0)
black=(0,0,0)

x1=300
y1=300

x1_change=0 #give starting point change in motion
y1_change=0

clock = pygame.time.Clock()


while not game_over:
    for event in pygame.event.get(): #prints movement from the mouse
        print(event)
        if event.type==pygame.QUIT: #allows you to quit the game
            game_over=True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #if presses left key
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT: #if presses right key
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP: #If presses up key
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN: #If presses down key
                x1_change = 0
                y1_change = 10

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis,blue,[x1,y1,10,10]) #sets the starting point with a blue color/snake
        pygame.display.update()

        clock.tick(30)
pygame.quit()
quit()