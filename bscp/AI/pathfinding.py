###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import heapq
from typing import List, Tuple

from bscp.Utils.vector import Vector
from bscp.Map.tilemap import TileMap


class Pathfinder:

    @staticmethod
    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def neighbors(tilemap: TileMap, node: Tuple[int, int], goal: Tuple[int, int] = None) -> List[Tuple[int, int]]:
        x, y = node
        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
        ]
        valid = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < tilemap.width and 0 <= ny < tilemap.height:
                tile = tilemap.tiles[ny][nx]
                if tile.walkable and (not tile.occupants or (goal and (nx, ny) == goal)):
                    valid.append((nx, ny))
        return valid

    @staticmethod
    def find_path(tilemap: TileMap, start: Vector, goal: Vector):
        start_node = (int(start.x), int(start.y))
        goal_node = (int(goal.x), int(goal.y))
        frontier = []
        heapq.heappush(frontier, (0, start_node))
        came_from = {}
        cost_so_far = {}
        came_from[start_node] = None
        cost_so_far[start_node] = 0
        while frontier:
            _, current = heapq.heappop(frontier)
            if current == goal_node:
                break
            for next_node in Pathfinder.neighbors(tilemap, current, goal_node):
                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + Pathfinder.heuristic(goal_node, next_node)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current
        path = []
        current = goal_node
        while current != start_node:
            path.append(Vector(current[0], current[1]))
            if current not in came_from:
                return []
            current = came_from[current]
        path.reverse()
        return path
