import pygame
import random
import pygame.freetype
from snake import Snake
from cell import Cell

pygame.init()
pygame.font.init()




#########################################################
##      SETUP


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
w = width // cols
# col_width = width // cols
# row_height = height // rows 
cell_border_width = 1

text_offset = 5 
text_size = 12        

size = (width, height)

move_vectors = {
                'left': [-1, 0],
                'right': [1, 0], 
                'down': [0, 1],
                'up': [0, -1]
                }

##############################################################





screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
all_sprites_list = pygame.sprite.Group()



start_i = random.randint(0, cols)
start_j = random.randint(0, rows)

snake = Snake(start_i, start_j, w)
all_sprites_list.add(snake)




font = pygame.freetype.Font("C:\\Windows\\fonts\\Arial.ttf", text_size)

draw = True
clock=pygame.time.Clock()

board = []

def makeBoard():
    global board
    board = [[0] * cols] * rows
    for i in range(cols):
        board[i] = []        
        for j in range(rows):
            board[i].append(Cell(i, j, w))


def drawBoard():
    for i in range(cols):
        x = i * w
        pygame.draw.line(screen, WHITE, [x, 0], [x, height], cell_border_width)
    for j in range(rows):
        y = j * w
        pygame.draw.line(screen, WHITE, [0, y], [width, y], cell_border_width)
            
           
            
 
  
while draw:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                draw=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     draw=False
        all_sprites_list.update()
        makeBoard()
        drawBoard()
        snake.showHead(screen)
        snake.showBody(screen)
        for i in range(cols):
            x = i * w  + text_offset
            for j in range(rows):
                y = j * w  + text_offset
                ## how to show the coords if we need 
                text_surface, rect = font.render(f"{i}, {j}", WHITE)
                screen.blit(text_surface, (x, y))

        pygame.display.flip()

                 
                
         
         
         
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            print(move_vectors['left'])
            Snake.change_direction(move_vectors['left'])
        if keys[pygame.K_RIGHT]:
            Snake.change_direction(move_vectors['right'])
        if keys[pygame.K_UP]:
            Snake.change_direction(move_vectors['up'])
        if keys[pygame.K_DOWN]:
            Snake.change_direction(move_vectors['down'])
        
        
        clock.tick(5)

pygame.quit() 
