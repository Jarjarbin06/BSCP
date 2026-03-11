###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional

from bscp.Entities.entity import Entity
from bscp.Utils.vector import Vector


class NPC(Entity):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
        self.sprite = None
        self.position = Vector(x, y)
        self.speed = Vector(0, 0)
        self.max_speed: float = 1.0

    def update(self, dt: float) -> None:
        self.position.x += self.speed.x * dt
        self.position.y += self.speed.y * dt
