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


class RRT(NPC):

    def __init__(
            self,
            x: float,
            y: float,
            game: "Game | None" = None
    ) -> None:
        super().__init__(
            x,
            y,
            Sprite(
                FACTIONS_LOGO["RRT"],
                game=game
            ),
            ENEMIES["RRT"],
            "RRT",
            1.5
        )
