import pygame
from Config.constats import *

class World: 
    def __init__(self,Camera) -> None:
        self.camera = Camera
        self.world : list = self.LoadGamePath("./Game/Config/world.txt")

        # 🔹 Carregar a imagem da grama APENAS UMA VEZ
        self.grass : pygame.Surface = pygame.image.load("./Assents/World/gram.png").convert()
        self.grass = pygame.transform.scale(self.grass, (BlocksSize[0] + 2,BlocksSize[1] + 2))

        self.water : pygame.Surface = pygame.image.load("./Assents/World/water.png").convert()
        self.water = pygame.transform.scale(self.water, (BlocksSize[0] + 2,BlocksSize[1] + 2))

        self.water2 : pygame.Surface = pygame.image.load("./Assents/World/water2.png").convert()
        self.water2 = pygame.transform.scale(self.water2, (BlocksSize[0] + 2,BlocksSize[1] + 2))

        self.water3 : pygame.Surface = pygame.image.load("./Assents/World/water3.png").convert()
        self.water3 = pygame.transform.scale(self.water3, (BlocksSize[0] + 2,BlocksSize[1] + 2))

        self.grass2 : pygame.Surface = pygame.image.load("./Assents/World/gram2.png").convert()
        self.grass2 = pygame.transform.scale(self.grass2, (BlocksSize[0] + 2,BlocksSize[1] + 2))

        self.grass3 : pygame.Surface = pygame.image.load("./Assents/World/gram3.png").convert()
        self.grass3 = pygame.transform.scale(self.grass3, (BlocksSize[0] + 2,BlocksSize[1] + 2))
        
        self.arreia : pygame.Surface = pygame.image.load("./Assents/World/arreia.png").convert()
        self.arreia = pygame.transform.scale(self.arreia, (BlocksSize[0] + 2,BlocksSize[1] + 2))

        # 🔹 Criar um buffer para armazenar o mapa
        # self.map_surface : pygame.Surface = pygame.Surface((len(self.world[0]) * BlocksSize[0] + 2, len(self.world) * BlocksSize[1] + 2))
        # self.render_map()  # Renderiza o mapa apenas uma vez

    def LoadGamePath(self,path: str) -> list: 
        with open(path, 'r') as f:
            world : list = [list(map(int, linha.split())) for linha in f.readlines()] # ler o arquivo de configuraçao do mundo
        return world
    
    def render(self, display: pygame.Surface) -> None: 
        display.fill((0, 0, 0))  # Evita resíduos na tela

        for y, linha in enumerate(self.world):
            for x, tile in enumerate(linha):
                pos_x = x * BlocksSize[0] + 2 + self.camera.offsetX
                pos_y = y * BlocksSize[1] + 2 + self.camera.offsetY

                match tile: 
                    case 0:
                       display.blit(self.grass, (pos_x, pos_y))
                    case 1: 
                       display.blit(self.water, (pos_x, pos_y))
                    case 2: 
                       display.blit(self.grass2, (pos_x, pos_y))
                    case 3: 
                       display.blit(self.grass3, (pos_x, pos_y))
                    case 4:
                       display.blit(self.arreia, (pos_x, pos_y))
                    case 5: 
                       display.blit(self.water2, (pos_x, pos_y))
                    case 6: 
                       display.blit(self.water3, (pos_x, pos_y))
                    case _: 
                       print('Error block not exist')