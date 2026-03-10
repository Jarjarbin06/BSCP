###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import json
from pathlib import Path
from typing import Any

from bscp.Map.tilemap import TileMap, Tile


class MapLoader:
    TILE_COLORS = {
        "floor": (50, 50, 50),
        "wall": (100, 100, 100),
        "containment": (150, 0, 150),
        "spawn": (0, 150, 0),
    }

    @staticmethod
    def save(tilemap: TileMap, file_name: str) -> None:
        data = {
            "width": tilemap.width,
            "height": tilemap.height,
            "tiles": [
                [
                    {
                        "type": tile.type,
                        "walkable": tile.walkable
                    }
                    for tile in row
                ]
                for row in tilemap.tiles
            ]
        }
        path = Path("saves/map_save_" + file_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"[INFO] Map saved to {'saves/map_save_' + file_name}")

    @staticmethod
    def load(tilemap: TileMap, file_name: str) -> None:
        path = Path("saves/map_save_" + file_name)
        if not path.exists():
            raise FileNotFoundError(f"Map file not found: {'saves/map_save_' + file_name}")
        with path.open("r", encoding="utf-8") as f:
            data: dict[str, Any] = json.load(f)
        width = data.get("width", tilemap.width)
        height = data.get("height", tilemap.height)
        tiles_data = data.get("tiles", [])
        tilemap.width = width
        tilemap.height = height
        tilemap.tiles = [
            [
                Tile(
                    x=col,
                    y=row,
                    type=tiles_data[row][col].get("type", "floor"),
                    walkable=tiles_data[row][col].get("walkable", True)
                )
                for col in range(len(tiles_data[row]))
            ]
            for row in range(len(tiles_data))
        ]
        for row in tilemap.tiles:
            for tile in row:
                tile.color = MapLoader.TILE_COLORS.get(tile.type, (200, 200, 200))
        print(f"[INFO] Map loaded from {'saves/map_save_' + file_name}")
