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
from bscp.Entities.Components.faction import FactionComponent
from bscp.Entities.Components.health import HealthComponent
from bscp.Entities.Components.movement import MovementComponent
from bscp.Entities.entity import Entity
from bscp.Utils.vector import Vector


class NPC(Entity):

    def __init__(
            self,
            name: str = "NPC",
            position: Optional[Vector] = None,
            max_health: int = 100,
            max_speed: float = 10.0,
            faction_id: str = "neutral"
    ) -> None:
        super().__init__(name=name, position=position)
        self.add_component(AIComponent())
        self.add_component(MovementComponent(max_speed=max_speed))
        self.add_component(HealthComponent(max_health))
        self.add_component(FactionComponent(faction=faction_id))

    @property
    def ai(self) -> AIComponent:
        return self.get_component(AIComponent)

    @property
    def movement(self) -> MovementComponent:
        return self.get_component(MovementComponent)

    @property
    def health(self) -> HealthComponent:
        return self.get_component(HealthComponent)

    @property
    def faction(self) -> FactionComponent:
        return self.get_component(FactionComponent)

    def update(self, dt: float) -> None:
        if not self.active:
            return
        self._follow_path(dt)
        super().update(dt)

    def is_alive(self) -> bool:
        health_comp = self.health
        return health_comp is not None and health_comp.health > 0

    def move_towards(self, target_pos: "Vector", dt: float) -> None:
        if not self.ai or not self.movement:
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
        path_comp.set_velocity(direction * dt)
        if self.position.distance_to(waypoint) < 0.5:
            path_comp.path_index += 1

    def is_enemy(self, other):
        pass
