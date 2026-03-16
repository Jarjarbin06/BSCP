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


def is_panel_active():
    return current_panel is None


def handle_event():
    def handle_key_press():
        global current_panel
        if is_panel_active():
            if event.key == pygame.K_ESCAPE:
                current_panel = "setting"
        if not is_panel_active():
            pass

    def handle_key_hold():
        global current_panel
        keys = pygame.key.get_pressed()
        if is_panel_active():
            if keys[pygame.K_z]:
                bscp.position.y -= 0.5 * (clock.delta_time * TARGET_FPS)
            if keys[pygame.K_s]:
                bscp.position.y += 0.5 * (clock.delta_time * TARGET_FPS)
            if keys[pygame.K_q]:
                bscp.position.x -= 0.5 * (clock.delta_time * TARGET_FPS)
            if keys[pygame.K_d]:
                bscp.position.x += 0.5 * (clock.delta_time * TARGET_FPS)
        if not is_panel_active():
            pass

    def handle_mouse_click():
        global current_panel
        if is_panel_active():
            pass
        if not is_panel_active():
            clicked = panels[current_panel].get_clicked()
            if current_panel == "menu":
                if clicked == "start_game":
                    current_panel = None
                elif clicked == "quit_game":
                    bscp.window.close()
            if current_panel == "setting":
                if clicked == "reset_map":
                    bscp.clear_entities()
                elif clicked == "return_to_game":
                    current_panel = None
                elif clicked == "return_to_menu":
                    current_panel = "menu"

    def handle_mouse_wheel():
        global current_panel
        if is_panel_active():
            if event.dict["y"] > 0:
                bscp.zoom += 0.05
            elif event.dict["y"] < 0:
                bscp.zoom -= 0.05
        if not is_panel_active():
            pass

    def handle_other():
        global current_panel
        if event.type == pygame.QUIT:
            bscp.window.close()
        if event.type == pygame.VIDEORESIZE:
            bscp.window.set_size(event.size)

    handle_key_hold()
    for event in bscp.window.poll_events():
        handle_other()
        if event.type == pygame.KEYDOWN:
            handle_key_press()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click()
        if event.type == pygame.MOUSEWHEEL:
            handle_mouse_wheel()


def update_and_calc():
    bscp.check_entities()
    bscp.update(clock.delta_time)


def draw():
    bscp.window.clear()
    if is_panel_active():
        update_and_calc()
        bscp.map.draw(bscp.window.surface, bscp.zoom, bscp.position)
        for faction in bscp.entities_factions.values():
            for entity in faction:
                entity.draw(bscp.window.surface, bscp.zoom, bscp.position)
    if current_panel and current_panel in panels:
        panels[current_panel].draw(bscp.window.surface)
    bscp.window.display()


if __name__ == "__main__":
    bscp = BSCP.Core.Game()
    clock = BSCP.Core.Clock()

    TARGET_FPS = BSCP.Systems.open_config().fps
    TARGET_FRAME_TIME = 1.0 / TARGET_FPS

    panels["menu"] = BSCP.UI.Panels.Menu()
    panels["setting"] = BSCP.UI.Panels.Setting()
    current_panel = "menu"
    bscp.map.tiles[99][99].set_spawn(BSCP.Entities.NPC.CD(99.0, 99.0, bscp))
    bscp.map.tiles[90][90].set_spawn(BSCP.Entities.NPC.CI(90.0, 90.0, bscp))
    bscp.map.tiles[80][80].set_spawn(BSCP.Entities.NPC.IA(80.0, 80.0, bscp))
    bscp.map.tiles[70][70].set_spawn(BSCP.Entities.NPC.ISD(70.0, 70.0, bscp))
    bscp.map.tiles[60][60].set_spawn(BSCP.Entities.NPC.MD(60.0, 60.0, bscp))
    bscp.map.tiles[50][50].set_spawn(BSCP.Entities.NPC.MTF(50.0, 50.0, bscp))
    bscp.map.tiles[40][40].set_spawn(BSCP.Entities.NPC.O5(40.0, 40.0, bscp))
    bscp.map.tiles[30][30].set_spawn(BSCP.Entities.NPC.RRT(30.0, 30.0, bscp))
    bscp.map.tiles[20][20].set_spawn(BSCP.Entities.NPC.SCD(20.0, 20.0, bscp))
    bscp.map.tiles[10][10].set_spawn(BSCP.Entities.NPC.SD(10.0, 10.0, bscp))
    bscp.map.tiles[0][0].set_spawn(BSCP.Entities.NPC.SID(0.0, 0.0, bscp))

    while bscp.window.running:
        clock.tick()
        handle_event()
        draw()

        frame_time = clock.delta_time
        if frame_time < TARGET_FRAME_TIME:
            clock.sleep(TARGET_FRAME_TIME - frame_time)

    bscp.destroy()


