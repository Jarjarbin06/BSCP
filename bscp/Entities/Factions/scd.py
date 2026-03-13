###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Core.sprite import Sprite
from bscp.Entities.Factions.factions import FACTIONS_LOGO, ENEMIES
from bscp.Entities.Factions.npc import NPC


class SCD(NPC):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, Sprite(FACTIONS_LOGO["SCD"]), ENEMIES["SCD"], "SCD", 0.9)
