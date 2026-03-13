###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from jarbin_toolkit_action import Action

from bscp.Systems.config_instance import open_config
from bscp.Utils.logger import BSCPLog

log_path = str(__file__).removesuffix("bscp/Systems/logger_instance.py") + "log/"

open_log = Action("open log", BSCPLog, log_path, file_name="bscp", json=open_config().log_json) if open_config().log_enabled else None
