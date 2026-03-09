###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component


class ContainmentComponent(Component):

    def __init__(self, containment_level: int) -> None:
        super().__init__()
        if not isinstance(containment_level, int): raise TypeError()
        self.containment_level: int = containment_level
        self.breached: bool = False

    def breach(self) -> None:
        self.breached = True

    def contain(self) -> None:
        self.breached = False
