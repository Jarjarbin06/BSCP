###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Core.sprite import Sprite
from bscp.Entities.NPC.factions import FACTIONS_LOGO, ENEMIES
from bscp.Entities.NPC.npc import NPC


class ISD(NPC):

    def __init__(self, x: float, y: float, game: "Game | None" = None) -> None:
        super().__init__(x, y, Sprite(FACTIONS_LOGO["ISD"], game=game), ENEMIES["ISD"], "ISD", 1.0)
