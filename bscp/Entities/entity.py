###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Optional, Type, TypeVar
from uuid import uuid4

from bscp.Utils.vector import Vector
from bscp.Entities.Components.component import Component

T = TypeVar("T", bound=Component)


class Entity:

    def __init__(
            self, name: str = "Entity", position: Optional[Vector] = None) -> None:
        if not isinstance(name, str): raise TypeError()
        if not isinstance(position, (Vector | None)): raise TypeError()
        self.id: str = str(uuid4())
        self.name: str = name
        self.position: Vector = position if position else Vector(0, 0)
        self.rotation: float = 0.0
        self.velocity: Vector = Vector(0, 0)
        self.active: bool = True
        self.visible: bool = True
        self._components: dict[type[Component], Component] = {}

    def add_component(self, component: Component) -> None:
        if not isinstance(component, Component):
            raise TypeError()
        component._bind(self)
        self._components[type(component)] = component

    def get_component(self, component_type: Type[T]) -> Optional[T]:
        return self._components.get(component_type)

    def has_component(self, component_type: Type[Component]) -> bool:
        return component_type in self._components

    def remove_component(self, component_type: Type[Component]) -> None:
        if component_type in self._components:
            del self._components[component_type]

    def update(self, dt: float) -> None:
        if not isinstance(dt, float): raise TypeError()
        self.position += self.velocity * dt
        for component in self._components.values():
            component.update(dt)

    def destroy(self) -> None:
        self.active = False

    def move(self, delta: Vector) -> None:
        if not isinstance(delta, Vector): raise TypeError()
        self.position += delta

    def set_position(self, position: Vector) -> None:
        if not isinstance(position, Vector): raise TypeError()
        self.position = position

    def set_velocity(self, velocity: Vector) -> None:
        if not isinstance(velocity, Vector): raise TypeError()
        self.velocity = velocity

    def __repr__(self) -> str:
        return (
            f"<Entity name={self.name} "
            f"id={self.id[:8]} "
            f"pos={self.position}>"
        )
