###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import uuid
from typing import Optional, List


class Entity:

    def __init__(self) -> None:
        self.id = uuid.uuid4()
        self.sprite: Optional["Sprite"]
        self.faction_name: Optional[str]
        self.enemy: Optional[List[str]]
