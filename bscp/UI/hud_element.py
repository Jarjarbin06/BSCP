###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from collections.abc import Callable
from typing import Optional

import pygame

from bscp.Systems.logger_instance import open_log


class HUDElement_Text:

    def __init__(
            self,
            name: str,
            text_template: str,
            x: float,
            y: float,
            width: float,
            height: float,
            border_size: int,
            to_watch_object: object,
            to_watch_attribute: str,
            data_modifier: Optional[Callable] = lambda data: data,
    ):
        if "{}" not in text_template:
            open_log().log("WARN", "Button", f"text_template invalid: {repr(text_template)} (must contain '{{}}')")
        self.name = name
        self.text_template = text_template
        self.rect = pygame.Rect(x, y, width, height)
        self.rect_back = pygame.Rect(x - border_size, y - border_size, width + (border_size * 2), height + (border_size * 2))
        self.to_watch_object = to_watch_object
        self.to_watch_attribute = to_watch_attribute
        self.data_modifier = data_modifier
        self.font = pygame.font.SysFont('Corbel', 20)
        open_log().log("VALID", "Button", f"created: {repr(self)}")

    def draw(
            self,
            surface
    ):
        data = self.data_modifier(getattr(self.to_watch_object, self.to_watch_attribute))
        text: str = self.text_template.format(str(data))
        text_surface = self.font.render(text, True, (0, 255, 0))
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def __repr__(
            self
    ) -> str:
        return (
            f"<Element "
            f"text_template='{self.text_template}' "
            f"pos=({self.rect.x},{self.rect.y}) "
            f"size=({self.rect.width}x{self.rect.height}) "
            f"border_size={self.rect.x - self.rect_back.x} "
            f"to_watch_object={repr(self.to_watch_object)} "
            f"to_watch_attribute={repr(self.to_watch_attribute)}"
            f">"
        )
