import pygame
from Config.constats import *

class Chunk: 
    def __init__(self) -> None: 
        self.VisibleChuncks : list = []
    
    def render(self) -> list:
        pass

class World: 
    def __init__(self, Camera) -> None:
        self.camera = Camera
        self.world: list = self.LoadGamePath("./Game/Config/world.txt")

        # 🔹 Carregar texturas APENAS UMA VEZ
        self.textures = {
            0: pygame.transform.scale(pygame.image.load("./Assents/World/gram.png").convert(), (BlocksSize[0] + 2, BlocksSize[1] + 2)),
            1: pygame.transform.scale(pygame.image.load("./Assents/World/water.png").convert(), (BlocksSize[0] + 2, BlocksSize[1] + 2)),
            2: pygame.transform.scale(pygame.image.load("./Assents/World/arreia.png").convert(), (BlocksSize[0] + 2, BlocksSize[1] + 2)),
            3: pygame.transform.scale(pygame.image.load("./Assents/World/water2.png").convert(), (BlocksSize[0] + 2, BlocksSize[1] + 2)),
            4: pygame.transform.scale(pygame.image.load("./Assents/World/water3.png").convert(), (BlocksSize[0] + 2, BlocksSize[1] + 2)),
        }

        # 🔹 Criar um buffer para o mapa
        self.map_surface = pygame.Surface((len(self.world[0]) * BlocksSize[0] + 2, len(self.world) * BlocksSize[1] + 2))
        self.render_map()  # Renderiza o mapa apenas uma vez

    def LoadGamePath(self, path: str) -> list: 
        with open(path, 'r') as f:
            return [list(map(int, linha.split())) for linha in f.readlines()]  # Ler arquivo do mundo

    def render_map(self) -> None:
        """Renderiza o mapa uma única vez no buffer `map_surface`."""
        for y, linha in enumerate(self.world):
            for x, tile in enumerate(linha):
                if tile in self.textures:
                    pos_x = x * BlocksSize[0] + 2
                    pos_y = y * BlocksSize[1] + 2
                    self.map_surface.blit(self.textures[tile], (pos_x, pos_y))
                else:
                    print(f'Erro: bloco {tile} não existe')

    def render(self, display: pygame.Surface) -> None:
        """Desenha o mapa na tela com deslocamento da câmera."""
        display.fill((0, 0, 0))  # Evita resíduos na tela
        display.blit(self.map_surface, (self.camera.offset.x, self.camera.offset.y))  # Aplica o offset
