###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import heapq
from typing import List, Optional

from bscp.entities.components.component import Component
from bscp.utils.vector import Vector


class AIComponent(Component):

    def __init__(self) -> None:
        super().__init__()
        self.state: str = "idle"
        self.target_position: Optional[Vector] = None

    def update(self, dt: float) -> None:
        super().update(dt)
        if not isinstance(dt, float):
            raise TypeError()

        # Placeholder: could expand with behaviors per state
        if self.state == "idle":
            # Example: could search for nearby targets
            pass
        elif self.state == "moving":
            # Movement is handled in NPC.move_towards()
            pass
        elif self.state == "alert":
            # Example: chasing, attacking, or patrolling
            pass

    def find_path(self, start: Vector, goal: Vector, grid: Optional[List[List[int]]] = None) -> List[Vector]:
        if grid is None:
            return [goal]
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}

        def heuristic(a: Vector, b: Vector) -> float:
            return (b - a).length()

        def neighbors(pos: Vector) -> List[Vector]:
            dirs = [Vector(1, 0), Vector(-1, 0), Vector(0, 1), Vector(0, -1)]
            result = []
            for d in dirs:
                neighbor = pos + d
                x, y = int(neighbor.x), int(neighbor.y)
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 0:
                    result.append(neighbor)
            return result

        while open_set:
            _, current = heapq.heappop(open_set)
            if current.distance_to(goal) < 0.5:
                path = [goal]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return list(reversed(path))

            for neighbor in neighbors(current):
                tentative_g = g_score.get(current, float("inf")) + 1
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return []
