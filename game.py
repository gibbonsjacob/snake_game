import pygame
import random
import pygame.freetype
from snake import Snake
from cell import Cell

pygame.init()
pygame.font.init()




#########################################################
##      SETUP

frame_rate = 60
update_interval = 200
update_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(update_event_id, update_interval)


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
w = width // cols ## screen will be a square so we can just do this once
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
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            snake.change_direction(move_vectors['left'])
        if keys[pygame.K_RIGHT]:
            snake.change_direction(move_vectors['right'])
        if keys[pygame.K_UP]:
            snake.change_direction(move_vectors['up'])
        if keys[pygame.K_DOWN]:
            snake.change_direction(move_vectors['down'])
        
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                draw=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     draw=False
                if event.key == pygame.K_LEFT:
                    snake.change_direction(move_vectors['left'])
                if event.key == pygame.K_RIGHT:
                    snake.change_direction(move_vectors['right'])
                if event.key == pygame.K_UP:
                    snake.change_direction(move_vectors['up'])
                if event.key == pygame.K_DOWN:
                    snake.change_direction(move_vectors['down'])                        
            if event.type == update_event_id:
                snake.move()
                                     

        all_sprites_list.update()
        screen.fill((0, 0, 0))

        makeBoard()
        drawBoard()

        for i in range(cols):
            x = i * w  + text_offset
            for j in range(rows):
                y = j * w  + text_offset
                ## how to show the coords if we need 
                text_surface, rect = font.render(f"{i}, {j}", WHITE)
                screen.blit(text_surface, (x, y))
        
        
        # snake.move()
        snake.showHead(screen)
        snake.showBody(screen)
                 
                
         
         
         
                
        # keys = pygame.key.get_pressed()
        
        # if keys[pygame.K_LEFT]:
        #     snake.change_direction(move_vectors['left'])
        # if keys[pygame.K_RIGHT]:
        #     snake.change_direction(move_vectors['right'])
        # if keys[pygame.K_UP]:
        #     snake.change_direction(move_vectors['up'])
        # if keys[pygame.K_DOWN]:
        #     snake.change_direction(move_vectors['down'])
        # all_sprites_list.update()

        pygame.display.flip()

        clock.tick(frame_rate)

pygame.quit() 
