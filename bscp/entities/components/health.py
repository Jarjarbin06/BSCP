###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from entities.components.component import Component


class HealthComponent(Component):

    def __init__(self, max_health: int) -> None:
        super().__init__()
        if not isinstance(max_health, int):
            raise TypeError()
        self.max_health: int = max_health
        self.health: int = max_health

    def damage(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError()
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.require_entity().destroy()

    def heal(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError()
        self.health = min(self.max_health, self.health + amount)