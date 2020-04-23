import pygame
import game_mouse
import ball

class Brick:
    def __init__(self, height, width, x, y, color,screenw,screenh):
        WHITE = (255, 255, 255)
        self.h = height
        self.w = width
        self.c = color
        self.x = x
        self.y = y
        self.speed = 10
        self.screenw = screenw
        self.screenh = screenh

    def getP(self):
        return (self.x,self.y)

    def setP(self, x, y):
        self.x, self.y = x, y
    



    def contains(self, ball):
        ballrect = pygame.Rect(ball.x, ball.y, ball.width, ball.height)
        brickrect = pygame.Rect(self.x, self.y, self.w, self.h)
        
        return brickrect.colliderect(ballrect)


 
    def paint(self, surface):
        pygame.draw.rect(surface, self.c, pygame.Rect(self.getP(), (self.w, self.h) ), 0)
