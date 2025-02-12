import pygame
from Config.constats import *

class tree: 
    def __init__(self, camera):
        self.camera = camera
        
        # Carregar a sprite da árvore
        self.sprite: pygame.Surface = pygame.image.load("./Assents/World/tree.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (152, 152))

        # Lista para armazenar as posições das árvores
        self.position: list = []
        
        # Variáveis de deslocamento
        self.offsetX = 0
        self.offsetY = 0

        # Gerar posições das árvores
        for i in range(10):
            self.position.append((0 + self.offsetX, 0 + self.offsetY))
            self.offsetX += 155 
            if (i + 1) % 5 == 0: 
                self.offsetY = 420  
                self.offsetX = 0  

        # Criar o buffer (superfície offscreen)
        self.buffer = pygame.Surface((DisplaySize[0], DisplaySize[1]), pygame.SRCALPHA)

        # Desenhar todas as árvores no buffer
        self.draw_trees_to_buffer()

    def draw_trees_to_buffer(self):
        # Limpar o buffer
        self.buffer.fill((0, 0, 0, 0))  # Transparente, caso já tenha algo no buffer
        for pos in self.position:
            self.buffer.blit(self.sprite, (pos[0], pos[1]))

    def animation(self): 
        pass

    def render(self, display: pygame.Surface):
        # Desenhar o buffer na tela principal com o deslocamento da câmera
        display.blit(self.buffer, (self.camera.offset.x, self.camera.offset.y))
