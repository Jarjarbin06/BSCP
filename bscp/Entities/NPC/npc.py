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

from bscp.Map.tilemap import TileMap
from bscp.Systems.logger_instance import open_log
from bscp.Systems.pathfinder import Pathfinder
from bscp.Utils.vector import Vector


class NPC:

    def __init__(self, x: float, y: float, sprite: Optional["Sprite"], enemy: Optional[List[str]], faction_name: str = "FP", max_speed: float = 0.5) -> None:
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
        if self.sprite:
            self.sprite.draw(surface, zoom, position)

    def set_target_loc(self, target_loc: Vector) -> None:
        open_log().log("INFO", "NPC", f"new target : {repr(target_loc)}")
        self.target_loc = target_loc

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
