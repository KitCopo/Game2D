import pygame
from Config.constats import *

class Camera: 
    def __init__(self) -> None:
        self.offsetX : int = 0
        self.offsetY : int = 0

        # self.SizeBoxColision: tuple[int,int] = (100,100)
        # self.BoxColision : pygame.Rect = pygame.Rect()
    
    def move(self,direction : str) -> None:
        if direction == "up": 
            self.offsetY += Velocity
        elif direction == "down":
            self.offsetY -= Velocity
        elif direction == "left":
            self.offsetX += Velocity
        elif direction == "right":
            self.offsetX -= Velocity 