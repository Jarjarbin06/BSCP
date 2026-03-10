###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional
from bscp.utils.vector import Vector
from bscp.entities.components.ai import AIComponent
from bscp.entities.components.faction import FactionComponent
from bscp.entities.components.health import HealthComponent
from bscp.entities.components.movement import MovementComponent
from bscp.entities.entity import Entity


class NPC(Entity):

    def __init__(
        self,
        name: str = "NPC",
        position: Optional[Vector] = None,
        faction_id: str = "neutral"
    ) -> None:
        super().__init__(name=name, position=position)
        self.add_component(AIComponent())
        self.add_component(MovementComponent(max_speed=10.0))
        self.add_component(HealthComponent(100))
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
