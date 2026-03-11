###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import uuid
from typing import Optional, List

from bscp.Utils.vector import Vector


class Entity:

    def __init__(self, x: float, y: float) -> None:
        self.id = uuid.uuid4()
        self.sprite: Optional["Sprite"] = None
        self.faction_name: Optional[str] = None
        self.enemy: Optional[List[str]] = None
        self.position: Vector = Vector(0, 0)

    def copy(self) -> "Entity":
        new_entity = type(self)(self.position.x, self.position.y)
        if self.sprite is not None:
            new_entity.sprite = self.sprite
        if self.sprite is not None:
            new_entity.faction_name = self.faction_name
        if self.sprite is not None:
            new_entity.enemy = self.enemy
        new_entity.position = self.position
        return new_entity

    def draw(self, surface, tile_size: tuple[int, int] = (10, 10)) -> None:
        pass
