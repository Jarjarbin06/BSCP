###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame
from PIL import Image

from bscp.Systems.config_instance import open_config
from bscp.Systems.logger_instance import open_log
from bscp.Utils.vector import Vector


class Sprite(pygame.sprite.Sprite):

    def __init__(
            self,
            texture_path: str,
            position=(0, 0),
            size=(open_config().tile_size, open_config().tile_size),
            game: "Game | None" = None
    ) -> None:

        def clean_texture(
                texture_path: str
        ):
            file_name = texture_path.split("/")[-1]
            path = texture_path.removesuffix(file_name)
            new_texture_path = f"{path}bscp_clean_{file_name}"
            if game.add_temp(new_texture_path):
                im = Image.open(texture_path)
                mode = im.mode
                if mode == "L":
                    im = im.convert("L")
                    open_log().log(
                        "DEBUG",
                        "Sprite",
                        f"image converted: {repr(mode)} -> {repr(im.mode)}"
                    )
                mode = im.mode
                if mode != "RGBA":
                    im = im.convert("RGBA")
                    open_log().log("INFO", "Sprite", f"image converted: {repr(mode)} -> {repr(im.mode)}")
                im.save(new_texture_path, icc_profile=None)
                open_log().log(
                    "DEBUG",
                    "Sprite",
                    f"image cleaned: {repr(texture_path)} -> {repr(new_texture_path)}"
                )
            return new_texture_path

        if not isinstance(texture_path, str):
            open_log().log(
                "ERROR",
                "Sprite",
                f"__init__: texture_path must be an str (currently {repr(type(texture_path))})"
            )
            return
        if not isinstance(position, tuple):
            open_log().log(
                "WARN",
                "Sprite",
                f"__init__: position must be a tuple (currently {repr(type(position))})"
            )
        if len(position) != 2:
            open_log().log(
                "ERROR",
                "Sprite",
                f"__init__: position be made of exactly 2 int (currently {repr(len(position))})"
            )
            return
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
                "ERROR",
                "Sprite",
                f"__init__: size be made of exactly 2 int (currently {repr(len(size))})"
            )
            return
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
        if game is not None:
            texture_path = clean_texture(texture_path)
        self.original_image = pygame.image.load(texture_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, self.size.to_tuple())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        open_log().log("VALID", "Sprite", f"created: {repr(self)}")

    def draw(
            self,
            surface,
            zoom: float,
            camera_pos: Vector,
            view_rect=None
    ) -> None:
        if not isinstance(surface, pygame.Surface):
            open_log().log(
                "ERROR",
                "Sprite",
                f"draw: surface must be a pygame.Surface (currently {repr(type(surface))})"
            )
            return
        if not isinstance(zoom, float):
            open_log().log(
                "WARN",
                "Sprite",
                f"draw: zoom must be a float (currently {repr(type(zoom))})"
            )
        if not isinstance(camera_pos, Vector):
            open_log().log(
                "ERROR",
                "Sprite",
                f"draw: camera_pos must be a Vector (currently {repr(type(camera_pos))})"
            )
            return
        if view_rect is None:
            view_rect = surface.get_rect()
        scaled_w = max(1, int(self.size.x * zoom))
        scaled_h = max(1, int(self.size.y * zoom))
        screen_x = (self.position.x - camera_pos.x) * open_config().tile_size * zoom
        screen_y = (self.position.y - camera_pos.y) * open_config().tile_size * zoom
        sprite_rect = pygame.Rect(screen_x, screen_y, scaled_w, scaled_h)
        if not view_rect.colliderect(sprite_rect):
            return
        if zoom <= 2:
            temp_image = pygame.transform.smoothscale(self.original_image, (scaled_w, scaled_h))
        else:
            temp_image = pygame.transform.scale(self.original_image, (scaled_w, scaled_h))
        surface.blit(temp_image, (screen_x, screen_y))

    def __repr__(
            self
    ) -> str:
        return (
            f"<Sprite "
            f"pos={self.position} "
            f"size={self.size.x}x{self.size.y}>"
        )
