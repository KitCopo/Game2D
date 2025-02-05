import pygame
import World
from Config.constats import *
from World.world import *

class Game: 
    def __init__(self) -> None: 
        pygame.init()
        self.display : pygame.Surface = pygame.display.set_mode(DisplaySize) #janela do game
        
        pygame.display.set_caption("Game 2D")

        self.world = World()

    def Render(self) -> None:
        self.display.fill((0,0,0))

        self.world.render(self.display)

        pygame.display.flip()

    def update(self) -> None:
        run : bool = True 
        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.Render()

if __name__ == "__main__": 
    game : Game = Game()
    game.update()

    pygame.quit()