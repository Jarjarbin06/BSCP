###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################

from math import (
    hypot,
    atan2,
    degrees as deg,
    radians as rad,
    sin,
    cos
)
from numbers import Real
from typing import Self


class Vector:
    def __init__(self, x: Real, y: Real) -> None:
        if not isinstance(x, Real): raise TypeError()
        if not isinstance(y, Real): raise TypeError()
        self.x: float = float(x)
        self.y: float = float(y)

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Vector): raise TypeError()
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __iadd__(self, other: Self):
        if not isinstance(other, Vector): raise TypeError()
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, Vector): raise TypeError()
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __isub__(self, other: Self):
        if not isinstance(other, Vector): raise TypeError()
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other: Real) -> Self:
        if not isinstance(other, Real): raise TypeError()
        return Vector(
            self.x * other,
            self.y * other
        )

    def __imul__(self, other: Real):
        if not isinstance(other, Real): raise TypeError()
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other: Real) -> Self:
        if not isinstance(other, Real): raise TypeError()
        if other == 0: raise ZeroDivisionError()
        return Vector(
            self.x / other,
            self.y / other
        )

    def __itruediv__(self, other: Real):
        if not isinstance(other, Real): raise TypeError()
        if other == 0: raise ZeroDivisionError()
        self.x /= other
        self.y /= other
        return self

    def __neg__(self) -> Self:
        return Vector(-self.x, -self.y)

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Vector): return NotImplemented
        return round(self.x, 5) == round(other.x, 5) and round(self.y, 5) == round(other.y, 5)

    def __abs__(self) -> float:
        return self.length()

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def length(self) -> float:
        return hypot(self.x, self.y)

    def normalize(self) -> Self:
        l = self.length()
        if l == 0:
            return Vector(0.0, 0.0)
        return self / l

    def distance_to(self, other: Self) -> float:
        if not isinstance(other, Vector): raise TypeError()
        return (other - self).length()

    def direction_to(self, other: Self) -> Self:
        if not isinstance(other, Vector): raise TypeError()
        return (other - self).normalize()

    def dot(self, other: Self) -> float:
        if not isinstance(other, Vector): raise TypeError()
        return self.x * other.x + self.y * other.y

    def cross(self, other: Self) -> float:
        if not isinstance(other, Vector): raise TypeError()
        return self.x * other.y - self.y * other.x

    def angle(self, radians: bool = False) -> float:
        if not isinstance(radians, bool): raise TypeError()
        angle = atan2(self.y, self.x)
        return angle if radians else deg(angle)

    def rotate(self, angle: Real, radians: bool = False) -> Self:
        if not isinstance(angle, Real): raise TypeError()
        if not isinstance(radians, bool): raise TypeError()
        angle = angle if radians else rad(angle)
        c = cos(angle)
        s = sin(angle)
        return Vector(
            self.x * c - self.y * s,
            self.x * s + self.y * c
        )

    def copy(self) -> Self:
        return Vector(
            self.x,
            self.y
        )

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    @classmethod
    def from_tuple(cls, t: tuple[float, float]) -> Self:
        if not isinstance(t, tuple): raise TypeError()
        if len(t) != 2: raise ValueError()
        return cls(t[0], t[1])
