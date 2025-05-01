import pygame
import random
import pygame.freetype
#Let's import the Car Class
from snake import Car
pygame.init()
pygame.font.init()





GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
black = (0, 0, 0)
        
width = 800
height = 800


cols = 20
rows = 20
col_width = width // cols
row_height = height // rows 
cell_border_width = 2

text_offset = 5 
text_size = 14        

size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200 
playerCar.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(playerCar)
font = pygame.freetype.Font("C:\\Windows\\fonts\\MOD20.ttf", text_size)

#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
cells = [[]]


def drawBoard():
    for i in range(cols):
        x = i * col_width
        pygame.draw.line(screen, WHITE, [x, 0], [x, height], cell_border_width)
    for j in range(rows):
        y = j * row_height
        pygame.draw.line(screen, WHITE, [0, y], [width, y], cell_border_width)
            
            
            
 
   
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

        drawBoard()
        for i in range(cols):
            x = i * col_width  + text_offset
            for j in range(rows):
                y = j * row_height  + text_offset
                text_surface, rect = font.render(f"{i}, {j}", WHITE)
                screen.blit(text_surface, (x, y))
        # or just `render_to` the target surface.
            # font.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))
        pygame.display.flip()

                 
                
         
         
         
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            playerCar.moveUp(5)  
        if keys[pygame.K_DOWN]:
            playerCar.moveDown(5)  
        
        # Game Logic
        all_sprites_list.update()

        # Drawing on Screen
        # screen.fill(GREEN)
        # Draw The Road
        # pygame.draw.rect(screen, GREY, [40,0, 200,300])
        # Draw Line painting on the road
        # pygame.draw.line(screen, WHITE, [140,0],[140,300],5)
        
        # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        # all_sprites_list.draw(screen)

        # Refresh Screen
        # pygame.display.flip()

        # Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit() 
