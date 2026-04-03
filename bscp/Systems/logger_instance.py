###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Systems.config_instance import open_config
from bscp.Utils.logger import BSCPLog

_log_instance: BSCPLog | None = None


def open_log() -> BSCPLog | None:
    global _log_instance
    if _log_instance is None:
        if open_config().log_enabled:
            BSCPLog(
                path=str(__file__).removesuffix("bscp/Systems/logger_instance.py") + "log/",
                file_name="bscp",
                json=open_config().log_json
            ).delete()
            _log_instance = BSCPLog(
                path=str(__file__).removesuffix("bscp/Systems/logger_instance.py") + "log/",
                file_name="bscp",
                json=open_config().log_json
            )
        else:
            raise RuntimeError("Logging is disabled in config")
    return _log_instance
