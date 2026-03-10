###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Tuple

import pygame

from bscp.Map.tile import Tile
from bscp.Map.tilemap import TileMap
from bscp.Utils.vector import Vector


class Map:
    ENTITY_COLOR = (255, 255, 0)

    def __init__(self, tilemap: TileMap, tile_size: int = 32):
        self.tilemap: TileMap = tilemap
        self.tile_size: int = tile_size

    @property
    def width_px(self) -> int:
        return self.tilemap.width * self.tile_size

    @property
    def height_px(self) -> int:
        return self.tilemap.height * self.tile_size

    def draw(self, surface: pygame.Surface) -> None:
        for row in self.tilemap.tiles:
            for tile in row:
                self.draw_tile(surface, tile)

    def draw_tile(self, surface: pygame.Surface, tile: Tile) -> None:
        color = getattr(tile, "color", (200, 200, 200))
        rect = pygame.Rect(
            tile.x * self.tile_size,
            tile.y * self.tile_size,
            self.tile_size,
            self.tile_size
        )
        pygame.draw.rect(surface, color, rect)
        if tile.is_occupied():
            for entity in tile.occupants:
                entity_rect = pygame.Rect(
                    tile.x * self.tile_size + self.tile_size // 4,
                    tile.y * self.tile_size + self.tile_size // 4,
                    self.tile_size // 2,
                    self.tile_size // 2
                )
                pygame.draw.rect(surface, self.ENTITY_COLOR, entity_rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)

    def world_to_tile(self, position: Vector) -> Tuple[int, int]:
        tx = int(position.x)
        ty = int(position.y)
        return tx, ty

    def tile_to_world(self, x: int, y: int) -> Vector:
        return Vector(x + 0.5, y + 0.5)

    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.tilemap.width and 0 <= y < self.tilemap.height

    @staticmethod
    def move_entity(entity, new_pos: Vector, tilemap: TileMap):
        old_tile_x, old_tile_y = int(entity.position.x), int(entity.position.y)
        new_tile_x, new_tile_y = int(new_pos.x), int(new_pos.y)
        if 0 <= old_tile_y < tilemap.height and 0 <= old_tile_x < tilemap.width:
            old_tile = tilemap.tiles[old_tile_y][old_tile_x]
            if entity in old_tile.occupants:
                old_tile.occupants.remove(entity)
        entity.position = new_pos
        if 0 <= new_tile_y < tilemap.height and 0 <= new_tile_x < tilemap.width:
            new_tile = tilemap.tiles[new_tile_y][new_tile_x]
            if entity not in new_tile.occupants:
                new_tile.occupants.append(entity)

    def __repr__(self) -> str:
        return f"<Map {self.tilemap.width}x{self.tilemap.height} tilesize={self.tile_size}>"
