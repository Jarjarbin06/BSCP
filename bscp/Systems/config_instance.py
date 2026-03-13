###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from jarbin_toolkit_action import Action

from bscp.Utils.config import BSCPConfig

config_path = str(__file__).removesuffix("bscp/Systems/config_instance.py") + "config/"

open_config = Action("open config", BSCPConfig, config_path, file_name="bscp")
