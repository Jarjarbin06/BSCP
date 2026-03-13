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
        self.spawn = type(spawn)(self.x, self.y)

    def spawn_new_entity(self) -> Optional["Entity"]:
        if self.entity is None and self.spawn is not None:
            self.entity = type(self.spawn)(self.x, self.y)
            return self.entity
        return None

    def draw(self, surface, zoom: float, camera_pos: "Vector"):
        color = self.color
        if self.selected:
            color = (
                max(color[0] - 50, 0),
                max(color[1] - 50, 0),
                max(color[2] - 50, 0)
            )
        if self.spawn is not None:
            color = (50, 150, 50)
        tile_w, tile_h = self.tile_size[0] * zoom, self.tile_size[1] * zoom
        screen_x = (self.x - camera_pos.x) * tile_w
        screen_y = (self.y - camera_pos.y) * tile_h
        pygame.draw.rect(
            surface,
            (0, 0, 0),
            pygame.Rect(screen_x, screen_y, tile_w, tile_h)
        )
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
