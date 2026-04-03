###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from os import remove
from pathlib import Path
from typing import Dict, List, Any, Type

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
                "ERROR",
                "Game",
                f"__init__: size be made of exactly 2 int (currently {repr(len(size))})"
            )
            return
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
        self._flags: dict[str, tuple[tuple[str, ...], Any, Type]] = {
            "debug": (("-d", "--debug"), False, bool),
            "profile": (("-p", "--profile"), "None", str),
            "trace-assets": (("-t", "--trace-assets"), False, bool),
            "log-level": (("--log-level",), "ERROR", str),
            "log-open": (("-L", "--log-open"), False, bool),
            "show-log": (("-l", "--show-log"), False, bool),
            "fullscreen": (("-f", "--fullscreen"), False, bool),
            "windowed": (("-w", "--windowed"), False, bool),
            "no-vsync": (("--no-vsync",), False, bool),
            "fps": (("--fps",), open_config().fps, int),
            "map-editor": (("-e", "--map-editor"), False, bool),
            "no-npc": (("-n", "--no-npc"), False, bool),
            "spawn-test": (("-S", "--spawn-test"), False, bool),
            "about": (("-a", "--about"), False, bool),
            "help": (("-h", "--help"), False, bool),
            "fast-sim": (("-F", "--fast-sim"), False, bool),
            "pause-on-start": (("-P", "--pause-on-start"), False, bool),
            "ai-debug": (("-A", "--ai-debug"), False, bool),
            "generate-map": (("-g", "--generate-map"), False, bool),
            "map-size": (("--map-size",), open_config().map_size, tuple),
            "infinite-entities": (("-I", "--infinite-entities"), False, bool),
            "infinite-resources": (("--infinite-resources",), False, bool),
            "safe-mode": (("-s", "--safe-mode"), False, bool),
            "benchmark": (("-b", "--benchmark"), False, bool)
        }
        self.check_flag()
        self._window: Window = Window(size, title, vsync)
        self.rendering_limit: pygame.Rect = pygame.Surface.get_rect(self._window.surface)
        self.map: TileMap = TileMap(open_config().map_size)
        self.camera_zoom: float = 1.0
        self.camera_position: Vector = Vector(0, 0)
        self.fps_list_limit: int = self.get_flag("fps") * 5
        self.fps_list: list[float] = [0.00000]
        self._temp_paths: set[Path | str] = set()
        self.entities_factions: Dict[str, List[NPC | SCP]] = {
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
    def window(
            self
    ) -> Window:
        return self._window

    @property
    def flags(
            self
    ) -> dict[str, tuple[tuple[str, ...], Any, Type]]:
        return self._flags

    def get_flag(
            self,
            flag: str
    ) -> Any:
        if flag not in self._flags:
            open_log().log("WARN", "Game", f"invalid flag: {repr(flag)}")
            return None
        return self._flags[flag][2](self._flags[flag][1])

    @property
    def temp(
            self
    ) -> set[Path | str]:
        return self._temp_paths

    @property
    def lowest_fps(
            self
    ) -> float:
        return min(self.fps_list)

    def add_fps(
            self,
            fps: float
    ) -> None:
        self.fps_list.append(fps)
        if len(self.fps_list) > self.fps_list_limit:
            self.fps_list.pop(0)

    def check_flag(
            self
    ) -> None:
        from sys import argv
        lookup = {
            call: name
            for name, (calls, _, _) in self._flags.items()
            for call in calls
        }
        i = 1

        while i < len(argv):
            arg = argv[i]
            if arg not in lookup:
                i += 1
                continue
            name = lookup[arg]
            calls, default, expected_type = self._flags[name]
            if expected_type is bool:
                self._flags[name] = (calls, True, expected_type)
                i += 1
                continue
            if i + 1 >= len(argv):
                open_log().log("ERROR", "Flags", f"Missing value for {arg}")
                break
            raw_value = argv[i + 1]

            try:
                if expected_type is tuple:
                    value = tuple(map(int, raw_value.split(",")))
                else:
                    value = expected_type(raw_value)

            except Exception:
                open_log().log("ERROR", "Flags", f"Invalid value for {arg}: {raw_value}")
                i += 2
                continue

            self._flags[name] = (calls, value, expected_type)
            i += 2

    def add_temp(
            self,
            path: Path | str
    ) -> bool:
        if path in self.temp:
            return False
        self.temp.add(path)
        return True

    def display(
            self
    ):
        self.window.display()

    def destroy(
            self
    ) -> None:
        pygame.quit()
        open_log().log(
            "DEBUG",
            "PyGame",
            "destroyed")
        for temp_file in self.temp:
            try:
                remove(temp_file)
                open_log().log(
                    "INFO",
                    "Game",
                    f"temp file removed: {repr(temp_file)}"
                )
            except FileNotFoundError:
                open_log().log(
                    "WARN",
                    "Game",
                    f"failed to remove temp file: {repr(temp_file)}"
                )
        open_log().log(
            "VALID",
            "Game",
            f"game's temporary files removed"
        )
        open_log().log(
            "INFO",
            "Game",
            f"destroyed"
        )
        open_log().close()
        open_log().clean(open_log().file_name, True, False)

    def add_entity(
            self,
            entity
    ) -> bool:
        if not isinstance(entity, (NPC, SCP)):
            open_log().log(
                "ERROR",
                "Game",
                f"add_entity: entity must be a NPC or an SCP (currently {repr(type(entity))})"
            )
            return False
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

    def update(
            self,
            dt: float
    ) -> None:
        if not isinstance(dt, float):
            open_log().log(
                "WARN",
                "Game",
                f"update: dt must be a float (currently {repr(type(dt))})"
            )
        if dt < 0:
            open_log().log(
                "ERROR",
                "Game",
                f"update: dt must be a greater or equal to 0 (currently {repr(dt)})"
            )
            return
        for row in self.map.tiles:
            for tile in row:
                if tile.entity is not None:
                    tile.entity.update(dt, self.map)

    def draw(
            self
    ) -> None:
        self.map.draw(self.window.surface, self.camera_zoom, self.camera_position)

        for faction in self.entities_factions.values():

            for entity in faction:
                entity.draw(self.window.surface, self.camera_zoom, self.camera_position, self.rendering_limit)

    def check_entities(
            self
    ) -> None:
        def check_tmps():
            from os.path import exists
            to_remove: list = []
            for tmp in self._temp_paths:
                if not exists(tmp):
                    to_remove.append(tmp)
            for tmp in to_remove:
                self._temp_paths.remove(tmp)
                open_log().log(
                    "WARN",
                    "Game",
                    f"temp file was removed: {repr(tmp)}"
                )

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
                    if tile.spawn is not None:
                        entity_class = tile.get_spawn()
                        if entity_class is None:
                            continue
                        faction = entity_class.faction_name
                        max_amount = self.max_entities_per_factions[faction]
                        if max_amount != -1 and len(self.entities_factions[faction]) >= max_amount:
                            continue
                        entity = type(entity_class)(float(tile.x), float(tile.y), self)
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

        check_tmps()
        check_spawn()
        check_positions()

    def clear_entities(
            self
    ) -> None:
        for faction in self.entities_factions.keys():
            self.entities_factions[faction].clear()
        open_log().log(
            "INFO",
            "Game",
            f"map cleared from all entities"
        )

    def show_log(
            self,
            all: bool = False
    ):
        if all:
            print(open_log())
        else:
            string = str(open_log().filter(["WARN", "ERROR", "CRIT"] + (["DEBUG"] if open_config().get_bool("GAME", "debug") else [])))
            if string.count("\n") > 4:
                print(string)
            else:
                print("No log to show")

    def __repr__(
            self
    ) -> str:
        map_width = len(self.map.tiles[0]) if self.map.tiles else 0
        map_height = len(self.map.tiles)
        total_entities = sum(len(faction) for faction in self.entities_factions.values())
        return (
            f"<Game "
            f"window={self.window.width}x{self.window.height} "
            f"map={map_width}x{map_height} "
            f"camera_zoom={self.camera_zoom:.2f} "
            f"camera_position={self.camera_position} "
            f"factions={len(self.entities_factions)} "
            f"entities={total_entities}>"
        )
