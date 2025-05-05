


### Game Setup 
    
board_width = 800
board_height = 800
scoreboard_height = 50
window_height = board_height + scoreboard_height



cols = 20
rows = 20

cell_border_width = 1

board = []

game_score = 0

frame_rate = 60
update_interval = 200



### Colors: 

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GREEN = (66, 255, 88)
GREEN = (20, 255, 140)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)




### Gameplay

move_vectors = {
                'left': [-1, 0],
                'right': [1, 0], 
                'down': [0, 1],
                'up': [0, -1]
                }