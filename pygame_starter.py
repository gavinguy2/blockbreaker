import pygame
import math
import game_mouse
import ball
import paddle
import score
import brick



class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):

        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)
        pygame.font.init()
        self.font = pygame.font.SysFont('arial', 30, True)

        
        
        self.ball =  ball.Ball(10, 10, (255,255,255), width, height) 
      
                    
            
            
        self.paddle = paddle.Paddle(60, 20, (255,255,255), width, height )
        self.brick = [brick.Brick(60, 30, 575,0, (255,255,255), width, height),brick.Brick(60, 30, 575,62, (255,255,255), width, height ),brick.Brick(60, 30, 575,124, (255,255,255), width, height ),brick.Brick(60, 30, 575,186, (255,255,255), width, height),brick.Brick(60, 30, 575,248, (255,255,255), width, height),brick.Brick(60, 30, 575,310, (255,255,255), width, height ),brick.Brick(60, 30, 575,372, (255,255,255), width, height ),brick.Brick(60, 30, 575,434, (255,255,255), width, height )]
        self.score = score.Score()
        

        
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if self.score.computer == 0:
            return
        if len(self.brick) == 0:
            return
        
        
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in keys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")
            
        self.paddle.movepaddle(keys)
        
        
        self.ball.game_logic(self.score)
        if self.paddle.contains(self.ball):
            self.ball.x = self.paddle.x + self.paddle.w
            self.ball.dx *= -1
                
        for brick in self.brick:

            self.ball.game_logic(self.score)
            if brick.contains(self.ball):
                #ball.x = brick.y + brick.w
                self.ball.dx *= -1
                #score a point for player
            
                self.brick.remove(brick)
            
        return
    
    def paint(self, surface):
  
        surface.fill((0,0,0))
        
        self.ball.paint(surface)
            
        self.paddle.paint(surface)
        for brick in self.brick:
            brick.paint(surface)



        text = "Player Lives: "+str(self.score.computer)
        if self.score.computer == 0:
            text = "YOU DIED"
        if len(self.brick) == 0:
            text = "VICTORY ACHIEVED"
            
        
        textsurface = self.font.render(text, True, (255,255,255))
        surface.blit(textsurface, (10,10))

        return

def main():
    screen_width = 600
    screen_height = 496
    frames_per_second = 30
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

