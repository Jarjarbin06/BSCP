###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component
from utils.vector import Vector


class MovementComponent(Component):

    def __init__(self, max_speed: float) -> None:
        super().__init__()
        if not isinstance(max_speed, float): raise TypeError()
        self.max_speed: float = max_speed

    def update(self, dt: float) -> None:
        super().update(dt)
        if not isinstance(dt, float): raise TypeError()
        entity = self.require_entity()
        if entity.velocity.length() > self.max_speed:
            entity.velocity = entity.velocity.normalize() * self.max_speed