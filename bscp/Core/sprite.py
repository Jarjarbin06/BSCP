###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame

from bscp.Systems.config_instance import open_config


class Sprite(pygame.sprite.Sprite):

    def __init__(self, texture_path: str, position=(0, 0), size=(open_config().tile_size, open_config().tile_size)) -> None:
        if not isinstance(texture_path, str): raise TypeError("texture_path must be a string")
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(texture_path).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    @property
    def sprite(self):
        return self._sprite

    def draw(self, surface):
        surface.blit(self.image, self.rect)
