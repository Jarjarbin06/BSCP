###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component
from utils.vector import Vector
from engine.sprite import Sprite


class SpriteComponent(Component):

    def __init__(
        self,
        sprite: Sprite,
        offset: Vector | None = None,
        layer: int = 0
    ) -> None:
        super().__init__()

        if not isinstance(sprite, Sprite):
            raise TypeError()

        if offset is not None and not isinstance(offset, Vector):
            raise TypeError()

        if not isinstance(layer, int):
            raise TypeError()

        self.sprite: Sprite = sprite
        self.offset: Vector = offset if offset else Vector(0, 0)
        self.layer: int = layer

    def update(self, dt: float) -> None:
        super().update(dt)

        entity = self.require_entity()

        # Sync sprite position with entity
        self.sprite.position = entity.position + self.offset

        # Optional rotation sync
        self.sprite.rotation = entity.rotation