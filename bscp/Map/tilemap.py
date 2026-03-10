###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import List, Optional

from bscp.Map.tile import Tile
from bscp.Utils.vector import Vector


class TileMap:

    def __init__(self, width: int, height: int, default_type: str = "floor"):
        self.width: int = width
        self.height: int = height
        self.tiles: List[List[Tile]] = [
            [Tile(x, y, type=default_type) for x in range(width)]
            for y in range(height)
        ]

    def get_tile(self, x: int, y: int) -> Optional[Tile]:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None

    def set_tile_type(self, x: int, y: int, tile_type: str, walkable: Optional[bool] = None) -> bool:
        tile = self.get_tile(x, y)
        if tile:
            tile.type = tile_type
            if walkable is not None:
                tile.set_walkable(walkable)
            else:
                tile.set_walkable(tile.walkable)
            return True
        return False

    def place_entity(self, entity: object, x: int, y: int) -> bool:
        tile = self.get_tile(x, y)
        if tile and tile.walkable and not tile.is_occupied():
            tile.set_entity(entity)
            entity.position = Vector(x, y)
            return True
        return False

    def remove_entity(self, x: int, y: int) -> bool:
        tile = self.get_tile(x, y)
        if tile:
            tile.set_entity(None)
            return True
        return False

    def is_walkable(self, x: int, y: int) -> bool:
        tile = self.get_tile(x, y)
        return bool(tile and tile.walkable and not tile.is_occupied())

    def get_neighbors(self, x: int, y: int, diagonals: bool = False) -> List[Tile]:
        neighbors = []
        directions = [
            (0, -1),  # up
            (0, 1),  # down
            (-1, 0),  # left
            (1, 0)  # right
        ]
        if diagonals:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            tile = self.get_tile(x + dx, y + dy)
            if tile:
                neighbors.append(tile)
        return neighbors

    def __repr__(self) -> str:
        return f"<TileMap {self.width}x{self.height}>"

    def debug_print(self) -> None:
        for row in self.tiles:
            line = ""
            for tile in row:
                if tile.is_occupied():
                    line += "E"
                elif tile.type == "floor":
                    line += "."
                elif tile.type == "wall":
                    line += "#"
                elif tile.type == "containment":
                    line += "C"
                else:
                    line += "?"
            print(line)
