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


class Button:

    def __init__(self, name: str, text: str, x: float, y: float, width: float, height: float, color: tuple[int, int, int], border_color: tuple[int, int, int], border_size: int):
        self.name = name
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.rect_back = pygame.Rect(x - border_size, y - border_size, width + (border_size * 2), height + (border_size * 2))
        self.color = color
        self.border_color = border_color
        self.selected_color = (int(color[0] / 2), int(color[1] / 2), int(color[2] / 2))
        self.font = pygame.font.SysFont('Corbel', 30)
        open_log().log("VALID", "Button", f"created: {repr(self)}")

    def draw(self, surface):
        if self.is_hovered():
            pygame.draw.rect(surface, self.border_color, self.rect_back)
            pygame.draw.rect(surface, self.selected_color, self.rect)
        else:
            pygame.draw.rect(surface, self.border_color, self.rect_back)
            pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_hovered(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            return True
        return False

    def is_clicked(self) -> tuple[bool, bool, bool]:
        click = pygame.mouse.get_pressed()

        if self.is_hovered():
            open_log().log("INFO", "Button", f"{repr(self)} clicked with {[] + ["LEFT"] if click[0] else [] + ["MIDDLE"] if click[1] else [] + ["RIGHT"] if click[2] else []}")
            return click
        return False, False, False

    def __repr__(self) -> str:
        return (
            f"<Button "
            f"text='{self.text}' "
            f"pos=({self.rect.x},{self.rect.y}) "
            f"size=({self.rect.width}x{self.rect.height}) "
            f"color={self.color} "
            f"border={self.border_color} "
            f"border_size={self.rect.x - self.rect_back.x}"
            f">"
        )
