import pygame
import config
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Snake(pygame.sprite.Sprite):
    
    def __init__(self, i, j, w, body = []):
        pygame.sprite.Sprite.__init__(self)
        
        self.i = i
        self.j = j 
        self.w = w
        self.body = body
        self.x = self.i * self.w + 1
        self.y = self.j * self.w + 1
        self.direction = [0, 0]
        self.length = len(body)
    



    def showHead(self, screen):
        self.head = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
        pygame.draw.rect(screen, RED, self.head)
    
    
    def showBody(self, screen):
        for b in self.body:
            pygame.draw.rect(screen, WHITE, b)


    def change_direction(self, vector):
        self.direction = vector

        
             
    def move(self):
        if self.i + self.direction[0] < config.cols and self.i + self.direction[0] > -1: 
            self.i += self.direction[0]
        if self.j + self.direction[1] < config.rows and self.j + self.direction[1] > -1:    
            self.j += self.direction[1]  
        self.x = self.i * self.w + 1
        self.y = self.j * self.w + 1
    
        

           
    
    
