###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame

from bscp.UI.button import Button


class Panel:

    def __init__(self):
        self.buttons: list[Button] = []

    def add_button(self, button: Button):
        self.buttons.append(button)

    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface)


class Menu(Panel):
    def __init__(self):
        super().__init__()
        self._size = pygame.display.get_window_size()
        self.add_button(Button("START", 50, (self.size[1] - 50) / 2, self.size[0] / 3, 50, (150, 150, 150), (50, 50, 50)))
        self.add_button(Button("QUIT", 50, ((self.size[1] - 50) / 2) + 55, self.size[0] / 3, 50, (150, 150, 150), (50, 50, 50)))

    @property
    def size(self):
        return self._size
