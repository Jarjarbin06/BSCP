###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################
import pygame

from bscp.Core.sprite import Sprite
from bscp.Entities.Factions.factions import FACTIONS_LOGO
from bscp.Entities.Factions.npc import NPC


class CD(NPC):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
        self.sprite = Sprite(FACTIONS_LOGO["CD"])
        self.faction_name = "CD"

    def draw(self, surface, tile_size: tuple[int, int] = (10, 10)) -> None:
        if self.sprite:
            self.sprite.rect.topleft = (int(self.position.x * tile_size[0]), int(self.position.y * tile_size[1]))
            self.sprite.draw(surface)