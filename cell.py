import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (66, 255, 88)

class Cell():
    def __init__(self, i, j, w):
        self.i = i
        self.j = j 
        self.w = w
        self.x = self.i * self.w
        self.y = self.j * self.w 
        self.has_snake = False
        self.has_food = False

    def show_food(self, screen):
        if self.has_food:
            self.food = pygame.Rect(self.x, self.y, self.w - 1, self.w -1 )
            pygame.draw.rect(screen, GREEN, self.food)



    def show(self, screen):
        # self.body = pygame.Surface([self.i * self.w, self.j * self.w])
        if self.has_snake:
            fill_color = RED
        else:
            fill_color = BLACK
        # self.body.fill(fill_color)
        pygame.draw.rect(screen, fill_color, self.body)
        # pygame.draw.rect(screen, self.body, WHITE, [self.x, self.y, self.w, self.w])
        # self.rect = self.body.get_rect()
