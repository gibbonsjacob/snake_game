import pygame 
from snake import Snake
import config 
import random 



def choose_food_location(snake: Snake):
    
    options = []
    
    for i in range(config.cols):
        for j in range(config.rows):
            options.append([i, j])
    
    
    for coords in options:
        if coords in snake.body:
            options.remove(coords)
    
    
    return random.choice(options)


class Food(pygame.sprite.Sprite):
    
    def __init__(self, i, j, w):
        pygame.sprite.Sprite.__init__(self)
        
        self.i = i
        self.j = j
        self.w = w 
        self.x = self.i * self.w + 1
        self.y = self.j * self.w + 1
        
        
    
    def update_location(self, new_coords):
        new_i = new_coords[0]
        new_j = new_coords[1]
        setattr(self, 'i', new_i)
        setattr(self, 'j', new_j)
        setattr(self, 'x', self.i * self.w + 1)
        setattr(self, 'y', self.j * self.w + 1)
    
    
    def show(self, screen):
        self.head = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
        pygame.draw.rect(screen, config.LIGHT_GREEN, self.head)   
        
        
    
    # def move(self):
             