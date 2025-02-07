import pygame
from Config.constats import *
from World.world import *
from Camera.camera import *
from World.Player.player import *

class Game: 
    def __init__(self) -> None: 
        pygame.init()
        self.display : pygame.Surface = pygame.display.set_mode(DisplaySize) #janela do game
        
        pygame.display.set_caption("Game 2D")
        
        self.Camera : Camera = Camera()
        self.world : World = World(self.Camera)
        self.player : player = player()

    def Render(self) -> None:
        self.display.fill((0,0,0))

        self.world.render(self.display)
        self.player.render(self.display)

        pygame.display.flip()

    def update(self) -> None:
        run : bool = True 
        while run:   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.Camera.move("up")
            if keys[pygame.K_s]:
                self.Camera.move("down")
            if keys[pygame.K_a]:
               self.Camera.move("left")
            if keys[pygame.K_d]:
               self.Camera.move("right")

            self.Render()

if __name__ == "__main__": 
    game : Game = Game()
    game.update()

    pygame.quit()