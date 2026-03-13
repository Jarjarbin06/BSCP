###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import List

from bscp.Map.tile import Tile
from bscp.Systems.config_instance import open_config
from bscp.Utils.vector import Vector


class TileMap:

    def __init__(self, size: tuple[int, int] = open_config().map_size):
        self.tile_size: tuple[int, int] = (open_config().tile_size, open_config().tile_size)
        self.tiles: List[List[Tile]] = [[Tile(x, y, tile_size=self.tile_size) for x in range(size[0])] for y in range(size[1])]

    def draw(self, surface, zoom: float, position: Vector):
        for row in self.tiles:
            for tile in row:
                tile.draw(surface, zoom, position)

    def set_entity(self, position: Vector, entity: "Entity"):
        self.tiles[int(position.y)][int(position.x)].set_entity(entity)

    def debug(self):
        for row in self.tiles:
            for tile in row:
                if tile.spawn:
                    print("\033[42m", end="")
                if tile.selected:
                    print("\033[4m", end="")
                if tile.entity:
                    print("E", end="")
                elif tile.wall:
                    print("#", end="")
                else:
                    print(".", end="")
                print("\033[0m", end="")
            print()
