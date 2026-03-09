###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component


class AIComponent(Component):

    def __init__(self) -> None:
        super().__init__()
        self.state: str = "idle"

    def update(self, dt: float) -> None:
        super().update(dt)
        if not isinstance(dt, float): raise TypeError()
        # placeholder for behavior logic
        pass
