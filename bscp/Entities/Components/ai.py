###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import List, Optional

from bscp.Entities.Components.component import Component
from bscp.Utils.vector import Vector
from bscp.AI.pathfinding import Pathfinder


class AIComponent(Component):

    def __init__(self) -> None:
        super().__init__()
        self.state: str = "idle"
        self.target_position: Optional[Vector] = None

    def update(self, dt: float) -> None:
        super().update(dt)
        if not isinstance(dt, float):
            raise TypeError()
        # Placeholder for future AI states
        if self.state == "idle":
            pass
        elif self.state == "moving":
            pass
        elif self.state == "alert":
            pass

    def find_path(self, start: Vector, goal: Vector) -> List[Vector]:
        Vector(int(start.x), int(start.y))
        if not self.entity:
            return []
        game = getattr(self.entity, "game", None)
        if not game:
            return []
        tilemap = getattr(game, "tilemap", None)
        if not tilemap:
            return []
        path = Pathfinder.find_path(tilemap, start, goal)
        if len(path) <= 1:
            return []
        return path