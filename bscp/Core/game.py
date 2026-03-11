###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame

from bscp.Core.window import Window


class Game:

    def __init__(
            self,
            size: tuple[int, int],
            title: str = "BSCP : Foundation Architect",
            vsync: bool = True
    ):
        pygame.init()
        self._window = Window(size, title, vsync)

    @property
    def window(self) -> Window:
        return self._window

    def destroy(self) -> None:
        self.window.destroy()
