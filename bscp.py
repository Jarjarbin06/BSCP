###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import bscp as BSCP


if __name__ == "__main__":
    bscp = BSCP.Core.Game()

    while bscp.window.running:
        BSCP
        pass

    bscp.destroy()