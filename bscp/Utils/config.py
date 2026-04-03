###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from os import makedirs
from os.path import isdir

from jarbin_toolkit_config import Config as BaseConfig


class BSCPConfig:
    DEFAULT_CONFIG = {
        "GAME": {
            "tile_size": "10",
            "map_width": "100",
            "map_height": "100",
            "debug": "False"
        },
        "WINDOW": {
            "width": "1920",
            "height": "1080",
            "vsync": "True",
            "fps": "60"
        },
        "FACTIONS": {
            "FP": "10",
            "SCP": "-1",
            "CD": "20",
            "CI": "10",
            "IA": "4",
            "ISD": "4",
            "MD": "6",
            "MTF": "20",
            "O5": "3",
            "RRT": "15",
            "SCD": "5",
            "SD": "20",
            "SID": "5"
        },
        "LOG": {
            "enabled": "True",
            "json": "False",
        }
    }

    def __init__(
            self,
            path: str,
            file_name: str | None = None
    ) -> None:
        if not isdir(path):
            makedirs(path)
        self.path = path if path.endswith("/") else path + "/"
        self.file_name = file_name or "bscp_config"
        self._config = BaseConfig(
            path,
            file_name=f"{self.file_name}.ini",
            data=(None if BaseConfig.exist(self.path, file_name=self.file_name + ".ini") else self.DEFAULT_CONFIG),
        )

    def __repr__(
            self
    ) -> str:
        return f"BSCPConfig(path={self.path!r}, file_name={self.file_name!r})"

    def __str__(
            self
    ) -> str:
        return f"BSCPConfig<{self.path}{self.file_name}>"

    def set(
            self,
            section: str,
            option: str,
            value
    ) -> None:
        self._config.set(section, option, value)

    def get(
            self,
            section: str,
            option: str
    ):
        return self._config.get(section, option)

    def get_int(
            self,
            section: str,
            option: str
    ) -> int:
        return self._config.get_int(section, option)

    def get_float(
            self,
            section: str,
            option: str
    ) -> float:
        return self._config.get_float(section, option)

    def get_bool(
            self,
            section: str,
            option: str
    ) -> bool:
        return self._config.get_bool(section, option)

    @property
    def tile_size(
            self
    ) -> int:
        return self.get_int("GAME", "tile_size")

    @property
    def map_size(
            self
    ) -> tuple[int, int]:
        return (
            self.get_int("GAME", "map_width"),
            self.get_int("GAME", "map_height")
        )

    @property
    def debug(
            self
    ) -> bool:
        return self.get_bool("GAME", "debug")

    @property
    def window_size(
            self
    ) -> tuple[int, int]:
        return (
            self.get_int("WINDOW", "width"),
            self.get_int("WINDOW", "height")
        )

    @property
    def vsync(
            self
    ) -> bool:
        return self.get_bool("WINDOW", "vsync")

    @property
    def fps(
            self
    ) -> int:
        return self.get_int("WINDOW", "fps")

    @property
    def log_enabled(
            self
    ) -> bool:
        return self.get_bool("LOG", "enabled")

    @property
    def log_json(
            self
    ) -> bool:
        return self.get_bool("LOG", "json")
