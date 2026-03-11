###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional, List

import pygame

from bscp.Core.window import Window
from bscp.Entities.entity import Entity
from bscp.Map.tilemap import TileMap


class Game:

    def __init__(
            self,
            size: tuple[int, int],
            title: str = "BSCP : Foundation Architect",
            vsync: bool = True
    ):
        pygame.init()
        self._window = Window(size, title, vsync)
        self.map = TileMap()
        self.entities: List[Entity] = []

    @property
    def window(self) -> Window:
        return self._window

    def display(self):
        self.window.display()

    def destroy(self) -> None:
        self.window.destroy()

    def check_entities(self) -> None:
        for entity in self.entities:
            self.map.tiles[int(entity.position.x)][int(entity.position.y)].set_entity(entity)
        for row in self.map.tiles:
            for tile in row:
                new_entity = tile.spawn_new_entity()
                if new_entity is not None:
                    self.entities.append(new_entity)
