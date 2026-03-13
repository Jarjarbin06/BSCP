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

from bscp.Systems.config_instance import open_config
from bscp.Systems.logger_instance import open_log


class Tile:

    def __init__(self, x: int, y: int, tile_size: tuple[int, int] = (open_config().tile_size, open_config().tile_size)):
        self.x: int = int(x)
        self.y: int = int(y)
        self.entity: Optional["NPC" | "SCP"] = None
        self.color = (50, 50, 50)
        self.tile_size = tile_size
        self.selected: bool = False
        self.spawn: Optional["NPC" | "SCP"] = None
        self.wall: bool = False

    def select(self) -> None:
        self.selected = True

    def unselect(self) -> None:
        self.selected = False

    def make_wall(self) -> None:
        self.wall = True

    def unmake_wall(self) -> None:
        self.wall = False

    def remove_entity(self):
        if self.entity is not None:
            self.entity = None

    def set_entity(self, entity: "Entity"):
        if self.entity is None:
            self.entity = entity

    def set_spawn(self, spawn: "Entity"):
        self.spawn = spawn

    def get_spawn(self):
        if self.entity is None and self.spawn is not None:
            return self.spawn
        return None

    def draw(self, surface, zoom: float, camera_pos: "Vector"):
        tile_w, tile_h = self.tile_size[0] * zoom, self.tile_size[1] * zoom
        screen_x = (self.x - camera_pos.x) * tile_w
        screen_y = (self.y - camera_pos.y) * tile_h
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(screen_x, screen_y, tile_w, tile_h))
        color = self.color
        if self.selected:
            color = (
                max(color[0] - 50, 0),
                max(color[1] - 50, 0),
                max(color[2] - 50, 0)
            )
        if self.spawn:
            color = (50, 150, 50)
        margin_w, margin_h = tile_w * 0.05, tile_h * 0.05
        pygame.draw.rect(
            surface,
            color,
            pygame.Rect(
                screen_x + margin_w,
                screen_y + margin_h,
                tile_w - 2 * margin_w,
                tile_h - 2 * margin_h
            )
        )

    def __repr__(self) -> str:
        return (
            f"<Tile "
            f"pos=({self.x}, {self.y}) "
            f"entity={'None' if self.entity is None else type(self.entity).__name__} "
            f"spawn={'None' if self.spawn is None else type(self.spawn).__name__} "
            f"wall={self.wall} "
            f"selected={self.selected}>"
        )
