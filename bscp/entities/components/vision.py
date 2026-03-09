###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component


class VisionComponent(Component):

    def __init__(self, range: float, fov: float) -> None:
        super().__init__()
        if not isinstance(range, float): raise TypeError()
        if not isinstance(fov, float): raise TypeError()
        self.range: float = range
        self.fov: float = fov