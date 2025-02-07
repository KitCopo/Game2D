import pygame
from Config.constats import *

class player: 
    def __init__(self) -> None:
        self.player : pygame.Surface = pygame.image.load("./Assents/World/player.png").convert()
        self.player = pygame.transform.scale(self.player, (32,32))
        self.position : tuple[int,int] = (DisplaySize[0] / 2,DisplaySize[1] / 2)
    
    def animation(self) -> None:
        pass
    
    def attack(self) -> None: 
        pass

    def render(self,display : pygame.Surface) -> None: 
        display.blit(self.player,(self.position))