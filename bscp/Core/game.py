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
            width: int = 1280,
            height: int = 720,
            title: str = "BSCP : Foundation Architect",
            vsync: bool = True
    ):
        pygame.init()
        self._window = Window(width, height, title, vsync)

    @property
    def window(self) -> Window:
        return self._window

    def destroy(self) -> None:
        pygame.quit()
