import pygame 
import snake
import config 
import random 
GREEN = (66, 255, 88)



def choose_food_location(snake: snake.Snake):
    
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
        
        
    
    
    def show(self, screen):
        self.head = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
        pygame.draw.rect(screen, GREEN, self.head)   
        
        
    
    # def move(self):
             