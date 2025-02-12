import pygame
from Math.vector import *
from Config.constats import *

class player: 
    def __init__(self) -> None:
        self.state: str = "stop"
        self.Sprites: list = []

        for i in range(23): 
            sprite: pygame.Surface = pygame.image.load(f"./Assents/World/player{i+1}.png").convert_alpha()
            sprite = pygame.transform.scale(sprite, (BlocksSize))  # Escala a imagem e guarda de volta
            self.Sprites.append(sprite)

        self.position: Vector2 = Vector2(DisplaySize[0] / 2, DisplaySize[1] / 2) 
        
        self.currents_sprite: float = 0  # Float para suavizar animação
        self.image: pygame.Surface = self.Sprites[int(self.currents_sprite)]
    
    def ChangeState(self, NewState: str) -> None:
        if self.state != NewState: 
            # Garante que a animação comece imediatamente do primeiro frame correto
            if NewState == "up":
                self.currents_sprite = 6  # Primeira sprite do movimento para cima
            elif NewState == "down": 
                self.currents_sprite = 12
            elif NewState == "left": 
                self.currents_sprite = 17
            elif NewState == "right":
                self.currents_sprite = 17
            elif NewState == "stop":
                self.currents_sprite = 0  # Primeira sprite do estado parado
        
        self.state = NewState  # Atualiza o estado
    
    def animation(self) -> None:
        if self.state == "stop":
            self.currents_sprite += AnimationVelocity
            if self.currents_sprite > 5:  # Sprites de idle (0 a 5)
                self.currents_sprite = 0
        
        elif self.state == "up":
            self.currents_sprite += AnimationVelocity
            if self.currents_sprite > 10:  # Sprites de movimento (6 a 10)
                self.currents_sprite = 6  # Volta para 6 para repetir o ciclo
        
        elif self.state == 'down': 
            self.currents_sprite += AnimationVelocity
            if self.currents_sprite > 16:
                self.currents_sprite = 12 
        
        elif self.state == "right": 
            self.currents_sprite += AnimationVelocity 
            if self.currents_sprite > 22: 
                self.currents_sprite = 17
        
        elif self.state == "left":
            self.currents_sprite += AnimationVelocity
            if self.currents_sprite > 22:
                self.currents_sprite = 17
        
        self.image = self.Sprites[int(self.currents_sprite)]
    
    def attack(self) -> None: 
        pass
    
    def render(self, display: pygame.Surface) -> None:
        self.animation()  # Chama a animação antes de desenhar
        display.blit(self.image, (self.position.__tuple__()))
