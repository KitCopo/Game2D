import pygame
from Config.constats import *

class World: 
    def __init__(self) -> None:
        self.world : list = self.LoadGamePath("./Game/Config/world.txt")

        # 🔹 Carregar a imagem da grama APENAS UMA VEZ
        self.grass = pygame.image.load("./Assents/World/gram.png").convert()
        self.grass = pygame.transform.scale(self.grass, (BlocksSize[0] + 2,BlocksSize[1] + 2))
        
        # 🔹 Criar um buffer para armazenar o mapa
        self.map_surface : pygame.Surface = pygame.Surface((len(self.world[0]) * BlocksSize[0] + 2, len(self.world) * BlocksSize[1] + 2))
        self.render_map()  # Renderiza o mapa apenas uma vez

    def LoadGamePath(self,path: str) -> list: 
        with open(path, 'r') as f:
            world : list = [list(map(int, linha.split())) for linha in f.readlines()] # ler o arquivo de configuraçao do mundo
        return world
    
    def render_map(self) -> None:
        for y, linha in enumerate(self.world):
            for x, tile in enumerate(linha):
                if tile == 0:  # Se for grama (ou qualquer outro ID que queira)
                    self.map_surface.blit(self.grass, (x * BlocksSize[0] +2, y * BlocksSize[1] +2))

    def render(self, display: pygame.Surface) -> None: 
        display.blit(self.map_surface, (0,0))