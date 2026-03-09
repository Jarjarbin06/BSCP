###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################
from math import atan2, degrees

from utils import Vector


def distance(p1: Vector, p2: Vector) -> float:
    return (p2 - p1).length()


def angle_between(p1: Vector, p2: Vector, in_degrees: bool = True) -> float:
    angle = atan2(p2.y - p1.y, p2.x - p1.x)
    return degrees(angle) if in_degrees else angle


def lerp(v1: Vector, v2: Vector, t: float) -> Vector:
    """Linear interpolation between two vectors."""
    return v1 + (v2 - v1) * t


def clamp(val: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(max_val, val))
