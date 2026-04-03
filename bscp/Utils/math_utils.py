###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from math import atan2, degrees

from bscp.Utils.vector import Vector


def distance(
        p1: Vector,
        p2: Vector
) -> float:
    if not isinstance(p1, Vector): raise TypeError()
    if not isinstance(p2, Vector): raise TypeError()
    return (p2 - p1).length()


def angle_between(
        p1: Vector,
        p2: Vector,
        in_radians: bool = True
) -> float:
    if not isinstance(p1, Vector): raise TypeError()
    if not isinstance(p2, Vector): raise TypeError()
    if not isinstance(in_radians, bool): raise TypeError()
    angle = atan2(p2.y - p1.y, p2.x - p1.x)
    return angle if in_radians else degrees(angle)


def lerp(
        v1: Vector,
        v2: Vector,
        t: float
) -> Vector:
    if not isinstance(v1, Vector): raise TypeError()
    if not isinstance(v2, Vector): raise TypeError()
    if not isinstance(t, float): raise TypeError()
    return v1 + (v2 - v1) * t


def clamp(
        val: float,
        min_val: float,
        max_val: float
) -> float:
    if not isinstance(val, float): raise TypeError()
    if not isinstance(min_val, float): raise TypeError()
    if not isinstance(max_val, float): raise TypeError()
    return max(min_val, min(max_val, val))
