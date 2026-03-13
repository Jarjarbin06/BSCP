###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame

from bscp.Systems.logger_instance import open_log


class Window:

    def __init__(
            self,
            size: tuple[int, int],
            title: str = "BSCP : Foundation Architect",
            vsync: bool = True
    ) -> None:
        if not isinstance(size, tuple):
            open_log().log(
                "WARN",
                "Window",
                f"__init__: size must be a tuple (currently {repr(type(size))})"
            )
        if len(size) != 2:
            open_log().log(
                "ERROR",
                "Window",
                f"__init__: size be made of exactly 2 int (currently {repr(len(size))})"
            )
            return
        if not isinstance(size[0], int):
            open_log().log(
                "WARN",
                "Window",
                f"__init__: size[0] must be an int (currently {repr(type(size[0]))})"
            )
        if not isinstance(size[1], int):
            open_log().log(
                "WARN",
                "Window",
                f"__init__: size[1] must be an int (currently {repr(type(size[1]))})"
            )
        if not isinstance(title, str):
            open_log().log(
                "WARN",
                "Window",
                f"__init__: title must be a str (currently {repr(type(title))})"
            )
        if not isinstance(vsync, bool):
            open_log().log(
                "WARN",
                "Window",
                f"__init__: vsync must be a bool (currently {repr(type(vsync))})"
            )
        flags = pygame.constants.FULLSCREEN | pygame.constants.DOUBLEBUF
        self._title: str = title
        self._vsync: bool = vsync
        self._surface = pygame.display.set_mode(size, flags, vsync=1 if vsync else 0)
        self._size: tuple[int, int] = pygame.display.get_window_size()
        pygame.display.set_caption(title)
        self._running: bool = True
        open_log().log(
            "VALID",
            "Window",
            f"created: {repr(self)}"
        )

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
        if not isinstance(color, tuple):
            open_log().log(
                "WARN",
                "Window",
                f"clear: color must be a tuple (currently {repr(type(color))})"
            )
        if len(color) != 3:
            open_log().log(
                "ERROR",
                "Window",
                f"clear: color be made of exactly 3 int (currently {repr(len(color))})"
            )
            return
        if not isinstance(color[0], int):
            open_log().log(
                "WARN",
                "Window",
                f"clear: color[0] must be an int (currently {repr(type(color[0]))})"
            )
        if not isinstance(color[1], int):
            open_log().log(
                "WARN",
                "Window",
                f"clear: color[1] must be an int (currently {repr(type(color[1]))})"
            )
        if not isinstance(color[2], int):
            open_log().log(
                "WARN",
                "Window",
                f"clear: color[2] must be an int (currently {repr(type(color[2]))})"
            )

    def display(self) -> None:
        pygame.display.flip()

    def close(self) -> None:
        open_log().log(
            "INFO",
            "Window",
            "closed"
        )
        self._running = False

    def set_size(self, size: tuple[int, int]) -> None:
        if not isinstance(size, tuple):
            open_log().log(
                "WARN",
                "Window",
                f"set_size: size must be a tuple (currently {repr(type(size))})"
            )
        if len(size) != 2:
            open_log().log(
                "ERROR",
                "Window",
                f"set_size: size be made of exactly 2 int (currently {repr(len(size))})"
            )
            return
        if not isinstance(size[0], int):
            open_log().log(
                "WARN",
                "Window",
                f"set_size: size[0] must be an int (currently {repr(type(size[0]))})"
            )
        if not isinstance(size[1], int):
            open_log().log(
                "WARN",
                "Window",
                f"set_size: size[1] must be an int (currently {repr(type(size[1]))})"
            )
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)
        self._size = pygame.display.get_window_size()
        pygame.display.update()

    def get_size(self) -> tuple[int, int]:
        return self._size

    def __repr__(self) -> str:
        return (
            f"<Window "
            f"title='{self._title}' "
            f"size={self._size[0]}x{self._size[1]} "
            f"vsync={self._vsync} "
            f"running={self._running}>"
        )
