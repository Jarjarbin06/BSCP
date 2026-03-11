###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional

import pygame

from bscp.Entities.entity import Entity


class Tile:

    def __init__(self, x: int, y: int, tile_size: tuple[int, int] = (10, 10)):
        self.x: int = int(x)
        self.y: int = int(y)
        self.entity: Optional[Entity] = None
        self.color = (50, 50, 50)
        self.tile_size = (10, 10)
        self.selected: bool = False
        self.spawn: Optional[Entity] = None

    def select(self) -> None:
        self.selected = True

    def unselect(self) -> None:
        self.selected = False

    def remove_entity(self):
        if self.entity is not None:
            self.entity = None

    def set_entity(self, entity: Entity):
        if self.entity is None:
            self.entity = entity

    def set_spawn(self, spawn: Entity):
        self.spawn = spawn.copy()

    def spawn_new_entity(self) -> Optional[Entity]:
        if self.entity is None and self.spawn is not None:
            self.entity = self.spawn.copy()
            return self.entity
        return None

    def draw(self, surface):
        color = self.color
        if self.selected:
            color = (self.color[0] - 50, self.color[1] - 50, self.color[2] - 50)
        if self.spawn is not None:
            color = (50, 150, 50)
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(self.x * self.tile_size[0], self.y * self.tile_size[1], self.tile_size[0], self.tile_size[1]))
        pygame.draw.rect(surface, color, pygame.Rect((self.x + 0.25) * self.tile_size[0], (self.y + 0.25) * self.tile_size[1], self.tile_size[0] - 0.5, self.tile_size[1] - 0.5))
