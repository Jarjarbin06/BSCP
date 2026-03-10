###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional

from bscp.Entities.Components.ai import AIComponent
from bscp.Entities.Components.component import Component
from bscp.Entities.Components.containement import ContainmentComponent
from bscp.Entities.Components.health import HealthComponent
from bscp.Entities.Components.movement import MovementComponent
from bscp.Entities.entity import Entity
from bscp.Utils.vector import Vector


class SCP(Entity):

    def __init__(
            self,
            name: str = "SCP",
            position: Optional[Vector] = None,
            anomaly_id: str = "SCP-000",
            max_health: int = 100,
            max_speed: float = 0.0,
            mobile: bool = False
    ) -> None:
        super().__init__(name=name, position=position)
        self.anomaly_id: str = anomaly_id
        self.add_component(AIComponent())
        self.add_component(ContainmentComponent())
        if max_health > 0:
            self.add_component(HealthComponent(max_health))
        if mobile and max_speed > 0:
            self.add_component(MovementComponent(max_speed))

    @property
    def ai(self) -> Optional[AIComponent]:
        return self.get_component(AIComponent)

    @property
    def movement(self) -> Optional[MovementComponent]:
        return self.get_component(MovementComponent)

    @property
    def health(self) -> Optional[HealthComponent]:
        return self.get_component(HealthComponent)

    @property
    def containment(self) -> Optional[ContainmentComponent]:
        return self.get_component(ContainmentComponent)

    def update(self, dt: float) -> None:
        if not self.active:
            return
        super().update(dt)

    def is_alive(self) -> bool:
        health_comp = self.health
        return health_comp is None or health_comp.health > 0

    def move_towards(self, target_pos: Vector, dt: float) -> None:
        if not self.movement or not self.ai:
            return
        path_comp = self.movement
        if path_comp.path is None or (path_comp.path and path_comp.path[-1] != target_pos):
            path_comp.path = self.ai.find_path(self.position, target_pos)
            path_comp.path_index = 0
        self._follow_path(dt)

    def _follow_path(self, dt: float) -> None:
        path_comp = self.movement
        if not path_comp or not path_comp.path:
            self.velocity = Vector(0, 0)
            return
        if path_comp.path_index >= len(path_comp.path):
            self.velocity = Vector(0, 0)
            return
        waypoint = path_comp.path[path_comp.path_index]
        direction = (waypoint - self.position).normalize()
        path_comp.set_velocity(direction)
        self.position += self.velocity * dt
        if self.position.distance_to(waypoint) < 0.5:
            path_comp.path_index += 1
