import pygame
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
        self.head = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
        self.length = len(body)
    



    def showHead(self, screen):
        pygame.draw.rect(screen, RED, self.head)
    
    
    def showBody(self, screen):
        for b in self.body:
            pygame.draw.rect(screen, WHITE, b)


         


    # def moveRight(self):
    #     self.direction = [1, 0]
    #     # self.head.x += pixels

    # def moveLeft(self):
    #     self.direction = [-1, 0]
    #     # self.head.x -= pixels
    
    # def moveDown(self):
    #     self.direction = [0, 1]
    #     # self.head.y += pixels

    # def moveUp(self):
    #     self.direction = [0, -1]
    #     # self.head.y -= pixels
           
    
    
    def change_direction(self, vector):
        self.i += vector[0]
        self.j += vector[1]   
        
             

    def move(self):
        self.i += self.direction[0]
        self.j += self.direction[1]  