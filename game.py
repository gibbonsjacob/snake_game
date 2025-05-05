import pygame
import random
import pygame.freetype
from snake import Snake
from cell import Cell
from food import choose_food_location
from food import Food 
import config 




pygame.init()
pygame.font.init()




#########################################################
##      SETUP

frame_rate = config.frame_rate
update_interval = config.update_interval
update_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(update_event_id, update_interval)


GREEN = config.GREEN
WHITE = config.WHITE
RED = config.RED
PURPLE = config.PURPLE
BLACK = config.BLACK
        
        
        
        
board_width = config.board_width
board_height = config.board_height
scoreboard_height = config.scoreboard_height
window_height = config.window_height
cols = config.cols
rows = config.rows
w = board_width // cols ## screen will be a square so we can just do this once
cell_border_width = config.cell_border_width

text_offset = 5 
text_size = 12        

size = (board_width, board_height)

move_vectors = config.move_vectors

##############################################################





screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
all_sprites_list = pygame.sprite.Group()



start_i = random.randint(0, cols - 1)
start_j = random.randint(0, rows - 1)




snake = Snake(start_i, start_j, w)
food_coords = choose_food_location(snake)
food = Food(food_coords[0], food_coords[1], w)
all_sprites_list.add(snake, food)




font = pygame.freetype.Font("C:\\Windows\\fonts\\Arial.ttf", text_size)

draw = True
clock=pygame.time.Clock()



def makeBoard():
    config.board = [[0] * cols] * rows
    for i in range(cols):
        config.board[i] = []        
        for j in range(rows):
            config.board[i].append(Cell(i, j, w))


def drawBoard():
    for i in range(cols):
        x = i * w
        pygame.draw.line(screen, WHITE, [x, 0], [x, board_height], cell_border_width)
    for j in range(rows):
        y = j * w
        pygame.draw.line(screen, WHITE, [0, y], [board_width, y], cell_border_width)
            
           
            
 
  
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


            if event.type == update_event_id:
                snake.move()
                
                if snake.collide():
                    snake.direction = [0, 0] 
                    # screen.fill(BLACK)
                    # font = pygame.freetype.Font("C:\\Windows\\fonts\\Arial.ttf", 36)
                    # text_surface, rect = font.render('Game Over!', RED)
                    # screen.blit(text_surface, (width // 2, height // 2))
                    draw = False
                
                if snake.eats(food):
                    config.game_score += 1
                    print(config.game_score) 
                    new_food_location = choose_food_location(snake)
                    food.update_location(new_food_location)
                    snake.grow()

                                     

        all_sprites_list.update()
        screen.fill(BLACK)

        makeBoard()
        drawBoard()

        for i in range(cols):
            x = i * w  + text_offset
            for j in range(rows):
                y = j * w  + text_offset
                
                if i == food.i and j == food.j: 
                    config.board[i][j].has_food = True
                if i == snake.i and j == snake.j:
                    config.board[i][j].has_snake = True
                
                     
                    
                ## how to show the coords if we need 
                # text_surface, rect = font.render(f"{i}, {j}", WHITE)
                # screen.blit(text_surface, (x, y))
        

        snake.show(screen)
        food.show(screen)

        pygame.display.flip()

        clock.tick(frame_rate)


screen.fill(BLACK)
font = pygame.freetype.Font("C:\\Windows\\fonts\\Arial.ttf", 36)
text_surface, rect = font.render('Game Over!', RED)
screen.blit(text_surface, (board_width // 2, board_height // 2))
pygame.quit() 
