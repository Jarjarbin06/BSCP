###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################
from typing import Optional, Dict

import pygame

from bscp.UI.button import Button


class Panel:

    def __init__(self):
        self.buttons: Dict[str, Button] = {}

    def add_button(self, name: str, button: Button):
        self.buttons[name] = button

    def draw(self, surface):
        for button in self.buttons.values():
            button.draw(surface)

    def get_hovered(self) -> Optional[str]:
        for name in self.buttons:
            if self.buttons[name].is_hovered():
                return name
        return None


class Menu(Panel):
    def __init__(self):
        super().__init__()
        self._size = pygame.display.get_window_size()
        self.add_button("start", Button("START", 50, (self.size[1] - 50) / 2, self.size[0] / 3, 50, (150, 150, 150), (50, 50, 50), 5))
        self.add_button("quit", Button("QUIT", 50, ((self.size[1] - 50) / 2) + 70, self.size[0] / 3, 50, (150, 50, 50), (50, 50, 50), 5))

    @property
    def size(self):
        return self._size


class Setting(Panel):
    def __init__(self):
        super().__init__()
        self._size = pygame.display.get_window_size()
        self.add_button("return", Button("RETURN", 50, (self.size[1] - 50) / 2, self.size[0] / 3, 50, (150, 150, 150), (50, 50, 50), 5))
        self.add_button("reset", Button("RESET", 50, ((self.size[1] - 50) / 2) + 70, self.size[0] / 3, 50, (150, 50, 50), (50, 50, 50), 5))
        self.add_button("exit", Button("EXIT", 50, ((self.size[1] - 50) / 2) + 140, self.size[0] / 3, 50, (150, 50, 50), (50, 50, 50), 5))

    @property
    def size(self):
        return self._size
