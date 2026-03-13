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

from bscp.Systems.logger_instance import open_log
from bscp.UI.button import Button


class Panel:

    def __init__(self):
        self.buttons: Dict[str, Button] = {}
        self.size = pygame.display.get_window_size()

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

    def get_clicked(self, click: int = 0) -> Optional[str]:
        for name in self.buttons:
            if self.buttons[name].is_clicked()[click]:
                return name
        return None

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"buttons={list(self.buttons.keys())} "
            f"count={len(self.buttons)}>"
        )


class Menu(Panel):
    def __init__(self):
        super().__init__()
        self.add_button("start_game", Button("start_game", "START", 50, (self.size[1] - 50) / 2, self.size[0] / 3, 50, (150, 150, 150), (50, 50, 50), 5))
        self.add_button("quit_game", Button("quit_game", "QUIT", 50, ((self.size[1] - 50) / 2) + 70, self.size[0] / 3, 50, (150, 50, 50), (50, 50, 50), 5))
        open_log().log("VALID", "Menu", f"created: {repr(self)}")

    def __repr__(self) -> str:
        return (
            f"<Menu "
            f"size={self.size[0]}x{self.size[1]} "
            f"buttons={list(self.buttons.keys())}>"
        )


class Setting(Panel):
    def __init__(self):
        super().__init__()
        self.add_button("return_to_game", Button("return_to_game", "RETURN", 50, (self.size[1] - 50) / 2, self.size[0] / 3, 50, (150, 150, 150), (50, 50, 50), 5))
        self.add_button("reset_map", Button("reset_map", "RESET", 50, ((self.size[1] - 50) / 2) + 70, self.size[0] / 3, 50, (150, 50, 50), (50, 50, 50), 5))
        self.add_button("return_to_menu", Button("return_to_menu", "MENU", 50, ((self.size[1] - 50) / 2) + 140, self.size[0] / 3, 50, (150, 50, 50), (50, 50, 50), 5))
        open_log().log("VALID", "Setting", f"created: {repr(self)}")

    def __repr__(self) -> str:
        return (
            f"<Setting "
            f"size={self.size[0]}x{self.size[1]} "
            f"buttons={list(self.buttons.keys())}>"
        )
