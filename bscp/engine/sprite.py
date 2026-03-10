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


class Sprite:

    def __init__(
            self,
            texture,
            position: Optional[Vector] = None,
            rotation: float = 0.0,
            scale: float = 1.0,
            origin: Optional[Vector] = None,
            layer: int = 0
    ) -> None:
        if position is not None and not isinstance(position, Vector): raise TypeError()
        if not isinstance(rotation, (float, int)): raise TypeError()
        if not isinstance(scale, (float, int)): raise TypeError()
        if origin is not None and not isinstance(origin, Vector): raise TypeError()
        if not isinstance(layer, int): raise TypeError()
        self.texture = texture
        self.position: Vector = position if position else Vector(0, 0)
        self.rotation: float = float(rotation)
        self.scale: float = float(scale)
        self.origin: Vector = origin if origin else Vector(0, 0)
        self.layer: int = layer
        self.visible: bool = True
        self.width: int | None = None
        self.height: int | None = None

    def set_position(self, position: Vector) -> None:
        if not isinstance(position, Vector): raise TypeError()
        self.position = position

    def move(self, delta: Vector) -> None:
        if not isinstance(delta, Vector): raise TypeError()
        self.position += delta

    def set_rotation(self, rotation: float) -> None:
        if not isinstance(rotation, (float, int)): raise TypeError()
        self.rotation = float(rotation)

    def rotate(self, angle: float) -> None:
        if not isinstance(angle, (float, int)): raise TypeError()
        self.rotation += float(angle)

    def set_scale(self, scale: float) -> None:
        if not isinstance(scale, (float, int)): raise TypeError()
        self.scale = float(scale)

    def show(self) -> None:
        self.visible = True

    def hide(self) -> None:
        self.visible = False

    def __repr__(self) -> str:
        return (
            f"<Sprite pos={self.position} "
            f"rot={self.rotation:.2f} "
            f"scale={self.scale:.2f} "
            f"layer={self.layer}>"
        )
