###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame

from bscp.Map.map import Map
from bscp.Map.tilemap import TileMap


class MapEditor:
    DEFAULT_TILE_TYPES = ["floor", "wall", "containment", "spawn"]

    TILE_COLORS = {
        "floor": (50, 50, 50),
        "wall": (100, 100, 100),
        "containment": (150, 0, 150),
        "spawn": (0, 150, 0),
    }

    def __init__(self, game_map: Map):
        self.map: Map = game_map
        self.tilemap: TileMap = game_map.tilemap
        self.selected_tile_type: str = "wall"
        self.running: bool = True

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.draw()
            pygame.time.delay(16)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.selected_tile_type = self.DEFAULT_TILE_TYPES[0]
                elif event.key == pygame.K_2:
                    self.selected_tile_type = self.DEFAULT_TILE_TYPES[1]
                elif event.key == pygame.K_3:
                    self.selected_tile_type = self.DEFAULT_TILE_TYPES[2]
                elif event.key == pygame.K_4:
                    self.selected_tile_type = self.DEFAULT_TILE_TYPES[3]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                tile_x = x // self.map.tile_size
                tile_y = y // self.map.tile_size
                if self.map.is_in_bounds(tile_x, tile_y):
                    tile = self.tilemap.tiles[tile_y][tile_x]
                    if event.button == 1:
                        tile.type = self.selected_tile_type
                        tile.color = self.TILE_COLORS.get(self.selected_tile_type, (200, 200, 200))
                        tile.walkable = self.selected_tile_type != "wall"
                    elif event.button == 3:
                        tile.type = "floor"
                        tile.color = self.TILE_COLORS["floor"]
                        tile.walkable = True

    def draw(self) -> None:
        surface = pygame.display.get_surface()
        if surface is None:
            return
        self.map.draw(surface)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Selected tile: {self.selected_tile_type}", True, (255, 255, 255))
        surface.blit(text, (10, 10))
        pygame.display.flip()

    def save_map(self, file_name: str) -> None:
        from bscp.Map.map_loader import MapLoader
        MapLoader.save(self.tilemap, file_name)

    def load_map(self, file_name: str) -> None:
        from bscp.Map.map_loader import MapLoader
        MapLoader.load(self.tilemap, file_name)
        for row in self.tilemap.tiles:
            for tile in row:
                tile.color = self.TILE_COLORS.get(tile.type, (200, 200, 200))
