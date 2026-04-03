###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import json
import pickle
from pathlib import Path
from typing import Any


class FileUtils:

    @staticmethod
    def ensure_dir(
            path: str
    ) -> None:
        dir_path = Path(path)
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def save_json(
            data: Any,
            path: str,
            file_name: str
    ) -> None:
        FileUtils.ensure_dir(path)
        full_path = Path(path) / f"{file_name}.json"
        with full_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_json(
            path: str,
            file_name: str
    ) -> Any:
        full_path = Path(path) / f"{file_name}.json"
        if not full_path.exists(): raise FileNotFoundError(f"File not found: {full_path}")
        with full_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def save_binary(
            data: Any,
            path: str,
            file_name: str
    ) -> None:
        FileUtils.ensure_dir(path)
        full_path = Path(path) / f"{file_name}.bin"
        with full_path.open("wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def load_binary(
            path: str,
            file_name: str
    ) -> Any:
        full_path = Path(path) / f"{file_name}.bin"
        if not full_path.exists(): raise FileNotFoundError(f"File not found: {full_path}")
        with full_path.open("rb") as f:
            return pickle.load(f)

    @staticmethod
    def exists(
            path: str,
            file_name: str,
            extension: str
    ) -> bool:
        return (Path(path) / f"{file_name}.{extension}").exists()

    @staticmethod
    def delete(
            path: str,
            file_name: str,
            extension: str
    ) -> None:
        file_path = Path(path) / f"{file_name}.{extension}"
        if file_path.exists():
            file_path.unlink()

    @staticmethod
    def list_files(
            path: str,
            extension: str | None = None
    ) -> list[str]:
        dir_path = Path(path)
        if not dir_path.exists() or not dir_path.is_dir():
            return []
        files = [f.name for f in dir_path.iterdir() if f.is_file()]
        if extension:
            files = [f for f in files if f.endswith(f".{extension}")]
        return files
