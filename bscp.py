###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################
from typing import Optional

import pygame

import bscp as BSCP

panels: dict[str, BSCP.UI.Panels.Panel] = {}
current_panel: Optional[str] = None

def handle_event():

    def handle_key():
        global current_panel
        if event.key == pygame.K_ESCAPE and current_panel is None:
            current_panel = "setting"

    def handle_mouse():
        global current_panel
        if current_panel == "menu":
            if panels[current_panel].get_hovered() == "start":
                current_panel = None
            elif panels[current_panel].get_hovered() == "quit":
                bscp.window.close()
        if current_panel == "setting":
            if panels[current_panel].get_hovered() == "reset":
                pass
            elif panels[current_panel].get_hovered() == "return":
                current_panel = None
            elif panels[current_panel].get_hovered() == "exit":
                current_panel = "menu"

    def handle_other():
        if event.type == pygame.QUIT:
            bscp.window.close()
        if event.type == pygame.VIDEORESIZE:
            bscp.window.set_size(event.size)

    for event in bscp.window.poll_events():
        handle_other()
        if event.type == pygame.KEYDOWN:
            handle_key()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse()

def update_and_calc():
    bscp.check_entities()

def draw():
    bscp.window.clear()
    if current_panel is None:
        update_and_calc()
        bscp.map.draw(bscp.window.surface)
        for entity in bscp.entities:
            entity.draw(bscp.window.surface, bscp.map.tile_size)
    if current_panel and current_panel in panels:
        panels[current_panel].draw(bscp.window.surface)
    bscp.window.display()

if __name__ == "__main__":
    bscp = BSCP.Core.Game((1920, 1080))

    panels["menu"] = BSCP.UI.Panels.Menu()
    panels["setting"] = BSCP.UI.Panels.Setting()
    current_panel = "menu"
    bscp.map.tiles[5][5].set_spawn(BSCP.Entities.Factions.CD(5, 5))

    while bscp.window.running:
        handle_event()
        draw()

    print(bscp.entities)
    bscp.destroy()
