###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component


class StaminaComponent(Component):

    def __init__(self, max_stamina: float) -> None:
        super().__init__()
        if not isinstance(max_stamina, float): raise TypeError()
        self.max_stamina: float = max_stamina
        self.stamina: float = max_stamina
        self.regen_rate: float = 5.0

    def update(self, dt: float) -> None:
        super().update(dt)
        if not isinstance(dt, float): raise TypeError()
        self.stamina = min(
            self.max_stamina,
            self.stamina + self.regen_rate * dt
        )