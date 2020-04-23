import pygame
import game_mouse
import random
import paddle
import ball

class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height, color, screenw, screenh):
        pygame.sprite.Sprite.__init__(self)
        WHITE = (255, 255, 255)
        self.image = pygame.Surface([10, 60])
        self.image.fill(WHITE)
        self.width = 10
        self.height = 10
        self.x = random.randint(70,100)
        self.y = random.randint(50,500)
        
        self.color = (255,255,255)
        self.screenw = screenw
        self.screenh = screenh
        self.dx = 1
        self.dy = 1
        
        self.rect = self.image.get_rect()

    def game_logic(self, score):
        
        x,y = self.x, self.y
        
        x += self.dx
        y += self.dy
        if x + self.width >= self.screenw:
            self.dx = -self.dx
            
        
        if x <= 0:
            x = random.randint(70,100)
            y = random.randint(50,500)
            self.dx = -self.dx
            
            score.computer -= 1
            
            
        if y + self.height >= self.screenh:
            self.dy = -self.dy
        if y <= 0:
            self.dy = -self.dy
        self.x, self.y = x, y


        

        return
    def paint(self, surface):
        pygame.draw.rect( surface, self.color, pygame.Rect((self.x, self.y), (self.width, self.height) ), 0)

