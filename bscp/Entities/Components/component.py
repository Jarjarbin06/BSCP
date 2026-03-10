###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from __future__ import annotations

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from bscp.Entities.entity import Entity


class Component:

    def __init__(self) -> None:
        self.entity: Optional[Entity] = None
        self.active: bool = True
        self.started: bool = False

    def _bind(self, entity: Entity) -> None:
        from bscp.Entities.entity import Entity

        if not isinstance(entity, Entity):
            raise TypeError()
        self.entity = entity
        self.start()

    def start(self) -> None:
        self.started = True

    def update(self, dt: float) -> None:
        if not isinstance(dt, float):
            raise TypeError()

    def destroy(self) -> None:
        self.active = False

    def require_entity(self) -> Entity:
        if self.entity is None:
            raise RuntimeError("Component not attached to an entity")
        return self.entity

    def __repr__(self) -> str:
        entity_id = self.entity.id[:8] if self.entity else "None"
        return f"<Component {self.__class__.__name__} entity={entity_id}>"
