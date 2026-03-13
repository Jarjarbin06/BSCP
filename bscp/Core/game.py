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
from bscp.Entities.NPC.SCP.scp import SCP
from bscp.Entities.NPC.npc import NPC
from bscp.Map.tilemap import TileMap
from bscp.Systems.config_instance import open_config
from bscp.Systems.logger_instance import open_log
from bscp.Utils import Vector


class Game:

    def __init__(
            self,
            size: tuple[int, int] = open_config().window_size,
            title: str = "BSCP : Foundation Architect",
            vsync: bool = open_config().vsync
    ):
        if not isinstance(size, tuple):
            open_log().log(
                "WARN",
                "Game",
                f"__init__: size must be a tuple (currently {repr(type(size))})"
            )
        if len(size) != 2:
            open_log().log(
                "WARN",
                "Game",
                f"__init__: size be made of exactly 2 int (currently {repr(len(size))})"
            )
        if not isinstance(size[0], int):
            open_log().log(
                "WARN",
                "Game",
                f"__init__: size[0] must be an int (currently {repr(type(size[0]))})"
            )
        if not isinstance(size[1], int):
            open_log().log(
                "WARN",
                "Game",
                f"__init__: size[1] must be an int (currently {repr(type(size[1]))})"
            )
        if not isinstance(title, str):
            open_log().log(
                "WARN",
                "Game",
                f"__init__: title must be a str (currently {repr(type(title))})"
            )
        if not isinstance(vsync, bool):
            open_log().log(
                "WARN",
                "Game",
                f"__init__: vsync must be a bool (currently {repr(type(vsync))})"
            )
        pygame.init()
        open_log().log(
            "DEBUG",
            "PyGame",
            "initialized"
        )
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
        open_log().log(
            "VALID",
            "Game",
            f"created: {repr(self)}"
        )

    @property
    def window(self) -> Window:
        return self._window

    def display(self):
        self.window.display()

    def destroy(self) -> None:
        pygame.quit()
        open_log().log(
            "INFO",
            "PyGame",
            "destroyed")
        open_log().log(
            "INFO",
            "Game",
            f"destroyed"
        )
        open_log().close()

    def add_entity(self, entity) -> bool:
        if not isinstance(entity, (NPC, SCP)):
            open_log().log(
                "WARN",
                "Game",
                f"add_entity: entity must be a NPC or an SCP (currently {repr(type(entity))})"
            )
        if self.max_entities_per_factions[entity.faction_name] == -1 or (
                len(self.entities_factions[entity.faction_name]) < self.max_entities_per_factions[entity.faction_name]
        ):
            self.entities_factions[entity.faction_name].append(entity)
            open_log().log(
                "INFO",
                "Game",
                f"entity added to the game: {repr(entity)}"
            )
            return True
        return False

    def update(self, dt: float) -> None:
        if not isinstance(dt, float):
            open_log().log(
                "WARN",
                "Game",
                f"update: dt must be a float (currently {repr(type(dt))})"
            )
        if dt < 0:
            open_log().log(
                "WARN",
                "Game",
                f"update: dt must be a greater or equal to 0 (currently {repr(dt)})"
            )
        for row in self.map.tiles:
            for tile in row:
                if tile.entity is not None:
                    tile.entity.update(dt, self.map)

    def check_entities(self) -> None:

        def check_positions():
            for row in self.map.tiles:
                for tile in row:
                    tile.remove_entity()
            for faction in self.entities_factions.values():
                for entity in faction:
                    self.map.tiles[int(entity.position.x)][int(entity.position.y)].set_entity(entity)

        def check_spawn():
            for row in self.map.tiles:
                for tile in row:
                    entity_class = tile.get_spawn()
                    if entity_class is None:
                        continue
                    faction = entity_class.faction_name
                    max_amount = self.max_entities_per_factions[faction]
                    if max_amount != -1 and len(self.entities_factions[faction]) >= max_amount:
                        continue
                    entity = type(entity_class)(tile.x, tile.y)
                    if self.add_entity(entity):
                        tile.set_entity(entity)
                        if max_amount != -1 and len(self.entities_factions[faction]) >= max_amount:
                            open_log().log(
                                "DEBUG",
                                "Game",
                                f"{repr(faction)} is now at max spawned capacity ({len(self.entities_factions[faction])}/{max_amount})"
                            )
                    else:
                        tile.remove_entity()

        check_spawn()
        check_positions()

    def clear_entities(self) -> None:
        for faction in self.entities_factions.keys():
            self.entities_factions[faction].clear()
        open_log().log(
            "INFO",
            "Game",
            f"map cleared from all entities"
        )

    def __repr__(self) -> str:
        map_width = len(self.map.tiles[0]) if self.map.tiles else 0
        map_height = len(self.map.tiles)
        total_entities = sum(len(faction) for faction in self.entities_factions.values())
        return (
            f"<Game "
            f"window={self.window.width}x{self.window.height} "
            f"map={map_width}x{map_height} "
            f"zoom={self.zoom:.2f} "
            f"camera={self.position} "
            f"factions={len(self.entities_factions)} "
            f"entities={total_entities}>"
        )
