import pygame
from Config.constats import *
from Camera.camera import *
from World.world import *
from World.Player.player import *
from World.tree.tree import *

class Game: 
    def __init__(self) -> None: 
        pygame.init()
        self.display : pygame.Surface = pygame.display.set_mode(DisplaySize) #janela do game
        
        pygame.display.set_caption("Game 2D")
        
        self.Camera : Camera = Camera()
        self.world : World = World(self.Camera)
        self.player : player = player()
        self.tree  : tree = tree(self.Camera)

        self.clock = pygame.time.Clock()

    def Render(self) -> None:
        self.display.fill((0,0,0))

        self.world.render(self.display)
        self.player.render(self.display)
        self.tree.render(self.display)

        pygame.display.flip()

    def update(self) -> None:
        run : bool = True
        while run: 
            deltaTime = self.clock.get_time() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.ChangeState("up")
                self.Camera.move("up",deltaTime)
            if keys[pygame.K_s]:
                self.player.ChangeState("down")
                self.Camera.move("down",deltaTime)
            if keys[pygame.K_a]:
               self.player.ChangeState("left")
               self.Camera.move("left",deltaTime)
            if keys[pygame.K_d]:
               self.player.ChangeState("right")
               self.Camera.move("right",deltaTime)
            
            if not (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
                self.player.ChangeState("stop")

            self.Render()

            self.clock.tick(120)
            print(int(self.clock.get_fps()))

if __name__ == "__main__": 
    game : Game = Game()
    game.update()

    pygame.quit()