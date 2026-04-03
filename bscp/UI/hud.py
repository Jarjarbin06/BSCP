###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Dict

import pygame

from bscp.Systems.logger_instance import open_log
from bscp.UI.hud_element import HUDElement_Text


class HUD:

    def __init__(
            self
    ):
        self.elements: Dict[str, HUDElement_Text] = {}
        self.size = pygame.display.get_window_size()

    def add_element(
            self,
            element: HUDElement_Text
    ):
        if element.name in self.elements:
            open_log().log("WARN", "HUD", f"failed to add {repr(element)}, {element.name} already exists")
        self.elements[element.name] = element

    def draw(
            self,
            surface
    ):
        for element in self.elements.values():
            element.draw(surface)

    def __repr__(
            self
    ) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"buttons={[element.name for element in list(self.elements.values())]} "
            f"count={len(self.elements)}>"
        )


class INGame(HUD):

    def __init__(
            self,
            game: "Game",
            clock: "Clock"
    ):
        super().__init__()
        self.add_element(
            HUDElement_Text(
                "FPS",
                "fps: {}",
                5,
                5,
                100,
                15,
                5,
                clock,
                "fps",
                round
            )
        )
        self.add_element(
            HUDElement_Text(
                "LOWEST_FPS",
                "(low: {})",
                5,
                25,
                100,
                15,
                5,
                game,
                "lowest_fps",
                round
            )
        )
        self.add_element(
            HUDElement_Text(
                "TEMP",
                "tmp: {}",
                110,
                5,
                100,
                15,
                5,
                game,
                "temp",
                len
            )
        )
        open_log().log("VALID", "INGame", f"created: {repr(self)}")

    def __repr__(
            self
    ) -> str:
        return (
            f"<Menu "
            f"size={self.size[0]}x{self.size[1]} "
            f"buttons={[element.name for element in list(self.elements.values())]}>"
        )
