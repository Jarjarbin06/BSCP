###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from bscp.Utils.config import BSCPConfig

_config_instance: BSCPConfig | None = None


def open_config() -> BSCPConfig:
    global _config_instance
    if _config_instance is None:
        config_path = str(__file__).removesuffix("bscp/Systems/config_instance.py") + "config/"
        BSCPConfig(config_path)
        _config_instance = BSCPConfig(config_path)
    return _config_instance
