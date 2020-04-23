import pygame
import game_mouse
import ball

class Paddle:
    def __init__(self, height, width,color,screenw,screenh):
        WHITE = (255, 255, 255)
        self.h = height
        self.w = width
        self.c = color
        self.x = 8
        self.y = 250
        self.speed = 10
        self.screenw = screenw
        self.screenh = screenh

    def getP(self):
        return (self.x,self.y)

    def setP(self, x, y):
        self.x, self.y = x, y
    

    def movepaddle(self, keys):
        x1,y1 = self.getP()

        if pygame.K_UP in keys:
            y1 -= self.speed


        if y1 <= 0:
            y1 = 0
            
        if pygame.K_DOWN in keys:
            y1 += self.speed

        if y1 >= self.screenh - self.h:
            y1 = self.screenh - self.h
            
        self.setP(x1,y1)


    def contains(self, ball):
        ballrect = pygame.Rect(ball.x, ball.y, ball.width, ball.height)
        paddlerect = pygame.Rect(self.x, self.y, self.w, self.h)
        
        return paddlerect.colliderect(ballrect)


 
    def paint(self, surface):
        pygame.draw.rect(surface, self.c, pygame.Rect(self.getP(), (self.w, self.h) ), 0)
