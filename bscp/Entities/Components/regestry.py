###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Entities.Components.ai import AIComponent
from bscp.Entities.Components.alarm import AlarmComponent
from bscp.Entities.Components.collision import CollisionComponent
from bscp.Entities.Components.containement import ContainmentComponent
from bscp.Entities.Components.door_access import DoorAccessComponent
from bscp.Entities.Components.faction import FactionComponent
from bscp.Entities.Components.health import HealthComponent
from bscp.Entities.Components.interaction import InteractionComponent
from bscp.Entities.Components.inventory import InventoryComponent
from bscp.Entities.Components.movement import MovementComponent
from bscp.Entities.Components.patrol import PatrolComponent
from bscp.Entities.Components.sprite import SpriteComponent
from bscp.Entities.Components.stamina import StaminaComponent
from bscp.Entities.Components.target import TargetComponent
from bscp.Entities.Components.vision import VisionComponent

COMPONENT_REGISTRY = {
    "AIComponent": AIComponent,
    "AlarmComponent": AlarmComponent,
    "CollisionComponent": CollisionComponent,
    "ContainmentComponent": ContainmentComponent,
    "DoorAccessComponent": DoorAccessComponent,
    "FactionComponent": FactionComponent,
    "HealthComponent": HealthComponent,
    "InteractionComponent": InteractionComponent,
    "InventoryComponent": InventoryComponent,
    "MovementComponent": MovementComponent,
    "PatrolComponent": PatrolComponent,
    "SpriteComponent": SpriteComponent,
    "StaminaComponent": StaminaComponent,
    "TargetComponent": TargetComponent,
    "VisionComponent": VisionComponent
}