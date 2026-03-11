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
            size: tuple[int, int],
            title: str = "BSCP : Foundation Architect",
            vsync: bool = True
    ) -> None:
        if not isinstance(title, str): raise TypeError()
        flags = pygame.constants.FULLSCREEN | pygame.constants.DOUBLEBUF
        self._title: str = title
        self._vsync: bool = vsync
        self._surface = pygame.display.set_mode(size, flags, vsync=1 if vsync else 0)
        self._size: tuple[int, int] = pygame.display.get_window_size()
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
        return self._size[0]

    @property
    def height(self) -> int:
        return self._size[1]

    def poll_events(self):
        return pygame.event.get()

    def clear(self, color=(0, 0, 0)) -> None:
        self._surface.fill(color)

    def display(self) -> None:
        pygame.display.flip()

    def close(self) -> None:
        self._running = False

    def destroy(self) -> None:
        pygame.quit()

    def set_size(self, size: tuple[int, int]) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)
        self._size = pygame.display.get_window_size()
        pygame.display.update()
