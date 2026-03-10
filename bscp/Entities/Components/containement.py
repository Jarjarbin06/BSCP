###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Entities.Components.component import Component


class ContainmentComponent(Component):

    def __init__(self) -> None:
        super().__init__()
        self.breached: bool = False

    def breach(self) -> None:
        self.breached = True

    def contain(self) -> None:
        self.breached = False
