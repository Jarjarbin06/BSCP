###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import List

from bscp.Entities.entity import Entity
from bscp.Map.tile import Tile
from bscp.Utils.vector import Vector


class TileMap:

    def __init__(self, size: tuple[int, int] = (100, 100)):
        self.tile_size: tuple[int, int] = (10, 10)
        self.tiles: List[List[Tile]] = [[Tile(x, y, tile_size=self.tile_size) for x in range(size[0])] for y in range(size[1])]

    def draw(self, surface):
        for row in self.tiles:
            for tile in row:
                tile.draw(surface)

    def set_entity(self, position: Vector, entity: Entity):
        self.tiles[int(position.y)][int(position.x)].set_entity(entity)
