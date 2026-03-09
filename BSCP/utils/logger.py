###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################

import os
from datetime import datetime

from jarbin_toolkit_log import Log as BaseLog


class BSCPLog:
    STATUS_COLORS = ["INFO", "VALID", "WARN", "ERROR", "DEBUG"]

    def __init__(self, path: str, file_name: str | None = None, json: bool = False) -> None:
        if not os.path.isdir(path):
            os.makedirs(path)
        self.file_path = path
        self.json = json
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.file_name = file_name or f"bscp_log_{timestamp}"
        self._log = BaseLog(path, self.file_name, json=json)

    def __str__(self) -> str:
        return str(self._log)

    def __repr__(self) -> str:
        return f"BSCPLog(path={self.file_path!r}, file_name={self.file_name!r}, json={self.json})"

    def log(self, status: str, title: str, description: str) -> None:
        status = status.upper()
        if status not in self.STATUS_COLORS:
            status = "INFO"
        self._log.log(status, title, description)

    def info(self, title: str, description: str) -> None:
        self.log("INFO", title, description)

    def valid(self, title: str, description: str) -> None:
        self.log("VALID", title, description)

    def warn(self, title: str, description: str) -> None:
        self.log("WARN", title, description)

    def error(self, title: str, description: str) -> None:
        self.log("ERROR", title, description)

    def debug(self, title: str, description: str) -> None:
        self.log("DEBUG", title, description)

    def comment(self, comment: str) -> None:
        self._log.comment(comment)

    def save_raw(self, log_str: str) -> None:
        self._log.save(log_str)

    def read(self) -> str:
        return self._log.read()

    def close(self) -> None:
        self._log.close()

    def delete(self) -> None:
        self._log.delete()
