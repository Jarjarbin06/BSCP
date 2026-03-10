###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.entities.components.component import Component


class TargetComponent(Component):

    def __init__(self) -> None:
        super().__init__()
        self.target = None

    def set_target(self, entity) -> None:
        self.target = entity

    def clear(self) -> None:
        self.target = None
