###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.entities.components.component import Component

from bscp.utils.vector import Vector


class PatrolComponent(Component):

    def __init__(self, points: list[Vector]) -> None:
        super().__init__()
        if not isinstance(points, list): raise TypeError()
        self.points = points
        self.current_index = 0

    def next_point(self) -> Vector:
        point = self.points[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.points)
        return point
