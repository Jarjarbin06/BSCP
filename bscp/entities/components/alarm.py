###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.entities.components.component import Component


class AlarmComponent(Component):

    def __init__(self) -> None:
        super().__init__()
        self.triggered: bool = False

    def trigger(self) -> None:
        self.triggered = True

    def reset(self) -> None:
        self.triggered = False
