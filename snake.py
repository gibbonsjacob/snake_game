import pygame
import config






def is_valid_move(curr_direction, new_direction):
    ## a valid move means you can only turn 90 degrees
    ## meaning you can't go from right to left, up to down, etc
    
    ## because of this, if either values from the current direction don't change in the new direction
    ## we know that a 90 degree turn could not have happened (if we have [1,0] and then [-1,0] that would be moving from right to left which is not allowed) 


    if curr_direction != [0, 0]: 
        return not ((curr_direction[0] == new_direction[0]) or (curr_direction[1] == new_direction[1]))
    else: #base case where we haven't started moving yet (when direction is [0,0])
        return True






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
        self.next_body_location = None

         
    
    def show(self, screen):
        for k in range(len(self.body)):
            if k == 0:
                self.head = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
                pygame.draw.rect(screen, config.RED, self.head)
            if k > 0:
                x = self.body[k][0] * self.w + 1
                y = self.body[k][1] * self.w + 1           
                body_part = pygame.Rect(x, y, self.w - 1, self.w -1)
                pygame.draw.rect(screen, config.WHITE, body_part)


    def change_direction(self, vector):
        
        if is_valid_move(self.direction, vector):
            self.direction = vector

        
             
    def move(self):
        


        if self.i + self.direction[0] < config.cols and self.i + self.direction[0] > -1: 
            self.i += self.direction[0]
        if self.j + self.direction[1] < config.rows and self.j + self.direction[1] > -1:    
            self.j += self.direction[1]  
        self.x = self.i * self.w + 1
        self.y = self.j * self.w + 1
        
        ## we just updated the new i and j values for the head, so now let's move every body part to where the part before it just was
        new_body = [[self.i, self.j]]
        for k in range(len(self.body)):
            if k > 0:
                new_body.append(self.body[k-1])
                
                
        ## finally, let's add in the newly eaten food as a body part if there is one
        ## we do it this way so that the new body part spawns where the food was rather than 
        ## at the end of the tail because there may not be a place available for it (the very last game)
        
        if self.next_body_location is not None:
               
            new_body.append(self.next_body_location)
            self.next_body_location = None                  
        
        self.body = new_body


        
    def eats(self, food):
        
        if self.i == food.i and self.j == food.j:
            self.next_body_location = [food.i, food.j]
            return True
        return False
    
    
    def grow(self):
        if self.next_body_location not in self.body:
            self.body.append(self.next_body_location)
        # print(self.body)
            
        
    
    
        

           
    
    
