import pygame
import config


class Snake(pygame.sprite.Sprite):
    
    def __init__(self, i, j, w):
        pygame.sprite.Sprite.__init__(self)
        
        self.i = i
        self.j = j 
        self.w = w
        self.x = self.i * self.w + 1
        self.y = self.j * self.w + 1
        self.body = [[self.i, self.j]]
        self.direction = [0, 0]
        self.length = len(self.body)

         
    
    def show(self, screen):
        for k in range(self.length):
            if k == 0:
                self.head = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
                pygame.draw.rect(screen, config.RED, self.head)
            if k > 0:
                x = self.body[k][0] * self.w + 1
                y = self.body[k][1] * self.w + 1           
                body_part = pygame.Rect(x, y, self.w - 1, self.w -1)
                pygame.draw.rect(screen, config.WHITE, body_part)


    def change_direction(self, vector):
        self.direction = vector

        
             
    def move(self):
        if self.i + self.direction[0] < config.cols and self.i + self.direction[0] > -1: 
            self.i += self.direction[0]
        if self.j + self.direction[1] < config.rows and self.j + self.direction[1] > -1:    
            self.j += self.direction[1]  
        self.x = self.i * self.w + 1
        self.y = self.j * self.w + 1
    
    
        
    def eats(self, food):
        
        if self.i == food.i and self.j == food.j:
            self.next_body_location = [food.i, food.j]
            
            ## add logic to add a new body part here
            
            
            return True
        return False
            
        
    
    
        

           
    
    
