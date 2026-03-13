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
from bscp.Systems.logger_instance import open_log


class TileMap:

    def __init__(self, size: tuple[int, int] = open_config().map_size):
        self.tile_size: tuple[int, int] = (open_config().tile_size, open_config().tile_size)
        self.tiles: List[List[Tile]] = [[Tile(x, y, tile_size=self.tile_size) for x in range(size[0])] for y in range(size[1])]
        open_log().log("VALID", "TileMap", f"created: {repr(self)}")
        self.log_debug()

    def draw(self, surface, zoom: float, position: Vector):
        for row in self.tiles:
            for tile in row:
                tile.draw(surface, zoom, position)

    def set_entity(self, position: Vector, entity: "Entity"):
        self.tiles[int(position.y)][int(position.x)].set_entity(entity)

    def show_debug(self):
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

    def log_debug(self):
        for row in self.tiles:
            string = ""
            for tile in row:
                if tile.spawn:
                    string += "S"
                elif tile.entity:
                    string += "E"
                elif tile.wall:
                    string += "#"
                else:
                    string += "."
            open_log().comment(string)

    def __repr__(self) -> str:
        width = len(self.tiles[0]) if self.tiles else 0
        height = len(self.tiles)
        spawn_count = 0
        entity_count = 0
        wall_count = 0
        for row in self.tiles:
            for tile in row:
                if tile.spawn:
                    spawn_count += 1
                if tile.entity:
                    entity_count += 1
                if tile.wall:
                    wall_count += 1
        return (
            f"<TileMap "
            f"size={width}x{height} "
            f"tile_size={self.tile_size} "
            f"spawns={spawn_count} "
            f"entities={entity_count} "
            f"walls={wall_count}>"
        )
