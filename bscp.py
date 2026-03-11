###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import pygame

import bscp as BSCP

if __name__ == "__main__":
    bscp = BSCP.Core.Game((1920, 1080))
    menu = BSCP.UI.Panels.Menu()

    while bscp.window.running:
        for event in bscp.window.poll_events():
            if event.type == pygame.QUIT:
                bscp.window.close()
            if event.type == pygame.VIDEORESIZE:
                print("resize")
                bscp.window.set_size(event.size)

        bscp.window.clear((255, 255, 255))
        menu.draw(bscp.window.surface)
        bscp.window.display()

    bscp.destroy()
