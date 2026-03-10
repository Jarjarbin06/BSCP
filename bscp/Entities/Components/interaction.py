###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Entities.Components.component import Component


class InteractionComponent(Component):

    def __init__(self, interaction_range: float) -> None:
        super().__init__()
        if not isinstance(interaction_range, float): raise TypeError()
        self.range: float = interaction_range

    def interact(self, target) -> None:
        pass
