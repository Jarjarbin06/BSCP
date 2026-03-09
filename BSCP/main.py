###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import jarbin_toolkit as JTK

import ai as AI
import core as CORE
import engine as ENGINE
import entities as ENTITIES
import map as MAP
import systems as SYSTEMS
import ui as UI
import utils as UTILS

SYSTEMS.open_log().delete()
log = SYSTEMS.open_log()
log.close()
print(log)
