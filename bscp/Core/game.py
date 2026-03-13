###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import Dict, List

import pygame

from bscp.Core.window import Window
from bscp.Map.tilemap import TileMap
from bscp.Systems.config_instance import open_config
from bscp.Utils import Vector


class Game:

    def __init__(
            self,
            size: tuple[int, int] = open_config().window_size,
            title: str = "BSCP : Foundation Architect",
            vsync: bool = open_config().vsync
    ):
        pygame.init()
        self._window = Window(size, title, vsync)
        self.map = TileMap(open_config().map_size)
        self.zoom = 1.0
        self.position: Vector = Vector(0, 0)
        self.entities_factions: Dict[str, List["NPC" | "SCP"]] = {
            "FP": [],
            "SCP": [],
            "CD": [],
            "CI": [],
            "IA": [],
            "ISD": [],
            "MD": [],
            "MTF": [],
            "O5": [],
            "RRT": [],
            "SCD": [],
            "SD": [],
            "SID": []
        }
        self.max_entities_per_factions: dict[str, int] = {
            "FP": open_config().get_int("FACTIONS", "fp"),
            "SCP": open_config().get_int("FACTIONS", "scp"),
            "CD": open_config().get_int("FACTIONS", "cd"),
            "CI": open_config().get_int("FACTIONS", "ci"),
            "IA": open_config().get_int("FACTIONS", "ia"),
            "ISD": open_config().get_int("FACTIONS", "isd"),
            "MD": open_config().get_int("FACTIONS", "md"),
            "MTF": open_config().get_int("FACTIONS", "mtf"),
            "O5": open_config().get_int("FACTIONS", "o5"),
            "RRT": open_config().get_int("FACTIONS", "rrt"),
            "SCD": open_config().get_int("FACTIONS", "scd"),
            "SD": open_config().get_int("FACTIONS", "sd"),
            "SID": open_config().get_int("FACTIONS", "sid")
        }

    @property
    def window(self) -> Window:
        return self._window

    def display(self):
        self.window.display()

    def destroy(self) -> None:
        self.window.destroy()

    def add_entity(self, entity) -> bool:
        if self.max_entities_per_factions[entity.faction_name] == -1 or (
                len(self.entities_factions[entity.faction_name]) < self.max_entities_per_factions[entity.faction_name]
        ):
            self.entities_factions[entity.faction_name].append(entity)
            return True
        return False

    def update(self, dt: float) -> None:
        for row in self.map.tiles:
            for tile in row:
                if tile.entity is not None:
                    tile.entity.update(dt, self.map)

    def check_entities(self) -> None:
        for row in self.map.tiles:
            for tile in row:
                new_entity = tile.spawn_new_entity()
                if new_entity is None or not self.add_entity(new_entity):
                    tile.remove_entity()
        for row in self.map.tiles:
            for tile in row:
                tile.remove_entity()
        for faction in self.entities_factions.values():
            for entity in faction:
                self.map.tiles[int(entity.position.x)][int(entity.position.y)].set_entity(entity)
