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


class O5(NPC):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, Sprite(FACTIONS_LOGO["O5"]), ENEMIES["O5"], "O5", 1.0)
