###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.entities.components.component import Component


class InventoryComponent(Component):

    def __init__(self, capacity: int) -> None:
        super().__init__()
        if not isinstance(capacity, int): raise TypeError()
        self.capacity: int = capacity
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        if not isinstance(item, str): raise TypeError()
        if len(self.items) >= self.capacity:
            return
        self.items.append(item)

    def remove_item(self, item: str) -> None:
        if not isinstance(item, str): raise TypeError()
        if item in self.items:
            self.items.remove(item)
