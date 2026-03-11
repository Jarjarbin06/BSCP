###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame


class Window:

    def __init__(
            self,
            width: int = 1280,
            height: int = 720,
            title: str = "BSCP : Foundation Architect",
            vsync: bool = True
    ) -> None:
        if not isinstance(width, int): raise TypeError()
        if not isinstance(height, int): raise TypeError()
        if not isinstance(title, str): raise TypeError()
        flags = pygame.FULLSCREEN | pygame.WINDOWCLOSE
        self._width: int = width
        self._height: int = height
        self._title: str = title
        self._vsync: bool = vsync
        self._surface = pygame.display.set_mode(
            (width, height),
            flags,
            vsync=1 if vsync else 0
        )
        pygame.display.set_caption(title)
        self._running: bool = True

    @property
    def running(self) -> bool:
        return self._running

    @property
    def surface(self):
        return self._surface

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            if event.type == pygame.VIDEORESIZE:
                self._width, self._height = event.size
                self._surface = pygame.display.set_mode(
                    (self._width, self._height),
                    pygame.RESIZABLE
                )
            yield event

    def clear(self, color=(0, 0, 0)) -> None:
        self._surface.fill(color)

    def display(self) -> None:
        pygame.display.flip()

    def close(self) -> None:
        self._running = False
