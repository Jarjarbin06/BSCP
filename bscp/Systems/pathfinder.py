###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from heapq import heappush, heappop
from typing import List, Dict, Optional

from bscp.Utils.vector import Vector


class Pathfinder:

    @staticmethod
    def neighbors(
            node: Vector,
            tilemap: "TileMap"
    ) -> List[Vector]:
        directions = [
            Vector(1, 0),
            Vector(-1, 0),
            Vector(0, 1),
            Vector(0, -1)
        ]
        result = []
        for d in directions:
            n = node + d
            if (
                    0 <= int(n.y) < len(tilemap.tiles)
                    and 0 <= int(n.x) < len(tilemap.tiles[0])
            ):
                tile = tilemap.tiles[int(n.y)][int(n.x)]
                if tile.entity is None:  # walkable
                    result.append(n)
        return result

    @staticmethod
    def heuristic(
            a: Vector,
            b: Vector
    ) -> float:
        return a.distance_to(b)

    @staticmethod
    def reconstruct(
            came_from: Dict[Vector, Vector],
            current: Vector
    ) -> List[Vector]:
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    @staticmethod
    def find_path(
            start: Vector,
            goal: Vector,
            tilemap: "TileMap"
    ) -> Optional[List[Vector]]:
        open_set = []
        heappush(open_set, (0, start))
        came_from: Dict[Vector, Vector] = {}
        g_score = {start: 0}
        f_score = {start: Pathfinder.heuristic(start, goal)}
        visited = set()
        while open_set:
            _, current = heappop(open_set)
            if current == goal:
                return Pathfinder.reconstruct(came_from, current)
            visited.add(current)
            for neighbor in Pathfinder.neighbors(current, tilemap):
                tentative = g_score[current] + 1
                if neighbor in visited and tentative >= g_score.get(neighbor, float("inf")):
                    continue
                if tentative < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative
                    f = tentative + Pathfinder.heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heappush(open_set, (f, neighbor))
        return None
