###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Tuple


class Tile:
    DEFAULT_COLORS = {
        "floor": (200, 200, 200),  # light gray
        "wall": (100, 100, 100),  # dark gray
        "water": (0, 0, 255),  # blue
        "lava": (255, 0, 0),  # red
    }

    def __init__(
            self,
            x: int,
            y: int,
            type: str = "floor",
            walkable: bool = True,
            color: Tuple[int, int, int] = None
    ):
        self.x: int = x
        self.y: int = y
        self.type: str = type
        self.walkable: bool = walkable
        self.occupants: list = []

        if color is not None:
            self.color: Tuple[int, int, int] = color
        else:
            base_color = self.DEFAULT_COLORS.get(type, (150, 150, 150))
            self.color = base_color if walkable else tuple(max(0, c // 2) for c in base_color)

    def is_occupied(self) -> bool:
        return len(self.occupants) > 0

    def set_walkable(self, walkable: bool) -> None:
        self.walkable = walkable
        base_color = self.DEFAULT_COLORS.get(self.type, (150, 150, 150))
        self.color = base_color if walkable else tuple(max(0, c // 2) for c in base_color)

    def __repr__(self) -> str:
        return (
            f"<Tile ({self.x}, {self.y}) type={self.type} "
            f"walkable={self.walkable} occupants={len(self.occupants)} color={self.color}>"
        )
