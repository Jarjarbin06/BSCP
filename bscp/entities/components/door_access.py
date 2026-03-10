###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.entities.components.component import Component


class DoorAccessComponent(Component):

    def __init__(self, clearance_level: int) -> None:
        super().__init__()
        if not isinstance(clearance_level, int): raise TypeError()
        self.clearance_level: int = clearance_level
