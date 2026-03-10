###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional, List

from bscp.Entities.Components.component import Component
from bscp.Utils.vector import Vector


class MovementComponent(Component):

    def __init__(self, max_speed: float) -> None:
        super().__init__()
        if not isinstance(max_speed, float): raise TypeError()
        self.max_speed: float = max_speed
        self.path: Optional[List[Vector]] = None
        self.path_index: int = 0

    def update(self, dt: float) -> None:
        super().update(dt)
        if not isinstance(dt, float): raise TypeError()
        entity = self.require_entity()
        if entity.velocity.length() > self.max_speed:
            entity.velocity = entity.velocity.normalize() * self.max_speed

    def set_velocity(self, direction: "Vector") -> None:
        entity = self.require_entity()
        entity.velocity = direction.normalize() * self.max_speed
