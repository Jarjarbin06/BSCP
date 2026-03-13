###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from random import randint
from typing import Optional, List
from uuid import uuid4

import pygame

from bscp.Core.sprite import Sprite
from bscp.Map.tilemap import TileMap
from bscp.Systems.logger_instance import open_log
from bscp.Systems.pathfinder import Pathfinder
from bscp.Utils.vector import Vector


class NPC:

    def __init__(self, x: float, y: float, sprite: Optional["Sprite"], enemy: Optional[List[str]], faction_name: str = "FP", max_speed: float = 0.5) -> None:
        if not isinstance(x, float):
            open_log().log(
                "WARN",
                "NPC",
                f"__init__: x must be a float (currently {repr(type(x))})"
            )
        if not isinstance(y, float):
            open_log().log(
                "WARN",
                "NPC",
                f"__init__: y must be a float (currently {repr(type(y))})"
            )
        if not isinstance(sprite, (Sprite, None)):
            open_log().log(
                "ERROR",
                "NPC",
                f"__init__: sprite must be a Sprite or None (currently {repr(type(sprite))})"
            )
            return
        if not isinstance(enemy, (List, None)):
            open_log().log(
                "ERROR",
                "NPC",
                f"__init__: enemy must be a List or None (currently {repr(type(enemy))})"
            )
            return
        if enemy is not None:
            for e in enemy:
                if not isinstance(e, str):
                    open_log().log(
                        "WARN",
                        "NPC",
                        f"__init__: enemy must contain only str (currently {repr(type(e))})"
                    )
        self.id = uuid4()
        self.sprite: Optional["Sprite"] = sprite
        self.faction_name: str = faction_name
        self.enemy: Optional[List[str]] = enemy
        self.position: Vector = Vector(x, y)
        self.speed = Vector(0, 0)
        self.max_speed: float = max_speed
        self.target_loc: Optional[Vector] = None
        self.path: List[Vector] = []
        self.follow_entity: Optional["Entity"] = None
        open_log().log("VALID", "NPC", f"created: {repr(self)}")

    def update(self, dt: float, map: TileMap) -> None:
        if not isinstance(dt, float):
            open_log().log(
                "WARN",
                "NPC",
                f"update: dt must be a float (currently {repr(type(dt))})"
            )
        if not isinstance(map, TileMap):
            open_log().log(
                "ERROR",
                "NPC",
                f"update: map must be a TileMap (currently {repr(type(map))})"
            )
            return
        if self.follow_entity is None:
            if self.target_loc is None:
                self.target_loc = Vector(
                    randint(0, len(map.tiles[0]) - 1),
                    randint(0, len(map.tiles) - 1)
                )
                self.path = Pathfinder.find_path(
                    Vector(int(self.position.x), int(self.position.y)),
                    self.target_loc,
                    map
                ) or [self.position]
            if not self.path:
                self.target_loc = None
                return
        else:
            if self.target_loc != self.follow_entity.position:
                self.target_loc = self.follow_entity.position
                self.path = Pathfinder.find_path(
                    Vector(int(self.position.x), int(self.position.y)),
                    self.target_loc,
                    map
                ) or [self.position]
        next_node = self.path[0]
        direction = self.position.direction_to(next_node)
        distance = self.position.distance_to(next_node)
        move_distance = min(self.max_speed * dt, distance)
        self.position += direction * move_distance
        if move_distance == distance:
            self.path.pop(0)
        if not self.path:
            self.target_loc = None
        if self.sprite is not None:
            self.sprite.position = self.position

    def draw(self, surface, zoom: float, position: Vector) -> None:
        if not isinstance(surface, pygame.Surface):
            open_log().log(
                "ERROR",
                "NPC",
                f"draw: surface must be a pygame.Surface (currently {repr(type(surface))})"
            )
            return
        if not isinstance(zoom, float):
            open_log().log(
                "WARN",
                "NPC",
                f"draw: zoom must be a float (currently {repr(type(zoom))})"
            )
        if not isinstance(position, Vector):
            open_log().log(
                "ERROR",
                "NPC",
                f"draw: position must be a Vector (currently {repr(type(position))})"
            )
            return
        if self.sprite:
            self.sprite.draw(surface, zoom, position)

    def set_target_loc(self, target_loc: Vector) -> None:
        if not isinstance(target_loc, Vector):
            open_log().log(
                "ERROR",
                "NPC",
                f"draw: set_target_loc must be a Vector (currently {repr(type(target_loc))})"
            )
            return
        self.target_loc = target_loc
        open_log().log("INFO", "NPC", f"new target : {repr(target_loc)}")

    def __repr__(self) -> str:
        return (
            f"<NPC "
            f"id={str(self.id)} "
            f"faction='{self.faction_name}' "
            f"pos={self.position} "
            f"speed={self.speed} "
            f"max_speed={self.max_speed} "
            f"target={self.target_loc} "
            f"path_len={len(self.path)} "
            f"follow={str(self.follow_entity.id)[:8] if self.follow_entity else None}"
            f">"
        )
