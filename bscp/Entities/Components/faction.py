###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Entities.Components.component import Component


class FactionComponent(Component):

    def __init__(self, faction: str) -> None:
        super().__init__()
        if not isinstance(faction, str):
            raise TypeError()
        self.faction: str = faction
