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
from bscp.Systems.config_instance import open_config
from bscp.Utils.vector import Vector


class Sprite(pygame.sprite.Sprite):

    def __init__(self, texture_path: str, position=(0, 0), size=(open_config().tile_size, open_config().tile_size)) -> None:
        if not isinstance(texture_path, str):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: texture_path must be an str (currently {repr(type(texture_path))})"
            )
        if not isinstance(position, tuple):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: position must be a tuple (currently {repr(type(position))})"
            )
        if len(position) != 2:
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: position be made of exactly 2 int (currently {repr(len(position))})"
            )
        if not isinstance(position[0], int):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: position[0] must be an int (currently {repr(type(position[0]))})"
            )
        if not isinstance(position[1], int):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: position[1] must be an int (currently {repr(type(position[1]))})"
            )
        if not isinstance(size, tuple):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: size must be a tuple (currently {repr(type(size))})"
            )
        if len(size) != 2:
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: size be made of exactly 2 int (currently {repr(len(size))})"
            )
        if not isinstance(size[0], int):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: size[0] must be an int (currently {repr(type(size[0]))})"
            )
        if not isinstance(size[1], int):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: size[1] must be an int (currently {repr(type(size[1]))})"
            )
        super().__init__()
        self.size = Vector(size[0], size[1])
        self.position = Vector(position[0], position[1])
        self.tile_size = size[0]
        self.original_image = pygame.image.load(texture_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, self.size.to_tuple())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        open_log().log("VALID", "Sprite", f"created: {repr(self)}")

    def draw(self, surface, zoom: float, camera_pos: Vector) -> None:
        scaled_w = max(1, int(self.size.x * zoom))
        scaled_h = max(1, int(self.size.y * zoom))
        if zoom <= 2:
            temp_image = pygame.transform.smoothscale(self.original_image, (scaled_w, scaled_h))
        else:
            temp_image = pygame.transform.scale(self.original_image, (scaled_w, scaled_h))
        screen_x = (self.position.x - camera_pos.x) * open_config().tile_size * zoom
        screen_y = (self.position.y - camera_pos.y) * open_config().tile_size * zoom
        surface.blit(temp_image, (screen_x, screen_y))

    def __repr__(self) -> str:
        return (
            f"<Sprite "
            f"pos={self.position} "
            f"size={self.size.x}x{self.size.y}>"
        )
