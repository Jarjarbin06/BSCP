###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component


class CollisionComponent(Component):

    def __init__(self, radius: float) -> None:
        super().__init__()
        if not isinstance(radius, float): raise TypeError()
        self.radius: float = radius
