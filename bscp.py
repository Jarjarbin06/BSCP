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

import bscp

BSCP_GAME: Optional[bscp.Core.Game] = None
CLOCK: Optional[bscp.Core.Clock] = None
HUD: Optional[bscp.UI.HUD.HUD] = None
PANELS: dict[str, bscp.UI.Panels.Panel] = {}
CURRENT_PANEL: Optional[str] = None
TARGET_FPS: int = 0
FIXED_TARGET_FRAME_TIME : float = 0.0
TARGET_FRAME_TIME: float = 0.0
EVENT_ACCUMULATOR: float = 0.0


def is_panel_active():
    return CURRENT_PANEL is None


def handle_event():
    def handle_key_press():
        global CURRENT_PANEL
        if is_panel_active():
            if event.key == pygame.K_ESCAPE:
                CURRENT_PANEL = "setting"
        if not is_panel_active():
            pass

    def handle_key_hold():
        global CURRENT_PANEL
        keys = pygame.key.get_pressed()
        if is_panel_active():
            if keys[pygame.K_z]:
                BSCP_GAME.camera_position.y -= 5 * CLOCK.delta_time
            if keys[pygame.K_s]:
                BSCP_GAME.camera_position.y += 5 * CLOCK.delta_time
            if keys[pygame.K_q]:
                BSCP_GAME.camera_position.x -= 5 * CLOCK.delta_time
            if keys[pygame.K_d]:
                BSCP_GAME.camera_position.x += 5 * CLOCK.delta_time
        if not is_panel_active():
            pass

    def handle_mouse_click():
        global CURRENT_PANEL
        if is_panel_active():
            pass
        if not is_panel_active():
            clicked = PANELS[str(CURRENT_PANEL)].get_clicked()
            if CURRENT_PANEL == "menu":
                if clicked == "start_game":
                    CURRENT_PANEL = None
                elif clicked == "quit_game":
                    BSCP_GAME.window.close()
            if CURRENT_PANEL == "setting":
                if clicked == "reset_map":
                    BSCP_GAME.clear_entities()
                elif clicked == "return_to_game":
                    CURRENT_PANEL = None
                elif clicked == "return_to_menu":
                    CURRENT_PANEL = "menu"

    def handle_mouse_wheel():
        global CURRENT_PANEL
        if is_panel_active():
            if event.dict["y"] > 0:
                BSCP_GAME.camera_zoom += 0.1
            elif event.dict["y"] < 0:
                BSCP_GAME.camera_zoom -= 0.1
        if not is_panel_active():
            pass

    def handle_other():
        global CURRENT_PANEL
        if event.type == pygame.QUIT:
            BSCP_GAME.window.close()
        if event.type == pygame.VIDEORESIZE:
            BSCP_GAME.window.set_size(event.size)

    global EVENT_ACCUMULATOR
    EVENT_ACCUMULATOR += CLOCK.delta_time

    while EVENT_ACCUMULATOR >= FIXED_TARGET_FRAME_TIME:

        for event in BSCP_GAME.window.poll_events():
            handle_other()
            if event.type == pygame.KEYDOWN:
                handle_key_press()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click()
            if event.type == pygame.MOUSEWHEEL:
                handle_mouse_wheel()

        handle_key_hold()
        EVENT_ACCUMULATOR -= FIXED_TARGET_FRAME_TIME


def update_and_compute():
    global COMPUTEPS
    if is_panel_active():
        BSCP_GAME.check_entities()
        BSCP_GAME.update(CLOCK.delta_time)


def draw():
    global DRAWPS
    BSCP_GAME.window.clear()
    if is_panel_active():
        BSCP_GAME.draw()
    if CURRENT_PANEL and CURRENT_PANEL in PANELS:
        PANELS[CURRENT_PANEL].draw(BSCP_GAME.window.surface)
    HUD.draw(BSCP_GAME.window.surface)
    BSCP_GAME.window.display()


def init():
    def game():
        global BSCP_GAME, CLOCK, HUD
        BSCP_GAME = bscp.Core.Game()
        CLOCK = bscp.Core.Clock()
        HUD = bscp.UI.HUD.INGame(BSCP_GAME, CLOCK)

    def rendering():
        global TARGET_FPS, FIXED_TARGET_FRAME_TIME, TARGET_FRAME_TIME
        TARGET_FPS = (
            bscp.Systems.open_config().fps
            if not BSCP_GAME.get_flag("fast-sim")
            else
            10000
        )
        FIXED_TARGET_FRAME_TIME = 1.0 /  bscp.Systems.open_config().fps
        TARGET_FRAME_TIME = 1.0 / TARGET_FPS

    def panels():
        global PANELS, CURRENT_PANEL
        PANELS["menu"] = bscp.UI.Panels.Menu()
        PANELS["setting"] = bscp.UI.Panels.Setting()
        CURRENT_PANEL = "menu"

    def spawners():
        BSCP_GAME.map.tiles[99][99].set_spawn(bscp.Entities.NPC.CD(99.0, 99.0, BSCP_GAME))
        BSCP_GAME.map.tiles[90][90].set_spawn(bscp.Entities.NPC.CI(90.0, 90.0, BSCP_GAME))
        BSCP_GAME.map.tiles[80][80].set_spawn(bscp.Entities.NPC.IA(80.0, 80.0, BSCP_GAME))
        BSCP_GAME.map.tiles[70][70].set_spawn(bscp.Entities.NPC.ISD(70.0, 70.0, BSCP_GAME))
        BSCP_GAME.map.tiles[60][60].set_spawn(bscp.Entities.NPC.MD(60.0, 60.0, BSCP_GAME))
        BSCP_GAME.map.tiles[50][50].set_spawn(bscp.Entities.NPC.MTF(50.0, 50.0, BSCP_GAME))
        BSCP_GAME.map.tiles[40][40].set_spawn(bscp.Entities.NPC.O5(40.0, 40.0, BSCP_GAME))
        BSCP_GAME.map.tiles[30][30].set_spawn(bscp.Entities.NPC.RRT(30.0, 30.0, BSCP_GAME))
        BSCP_GAME.map.tiles[20][20].set_spawn(bscp.Entities.NPC.SCD(20.0, 20.0, BSCP_GAME))
        BSCP_GAME.map.tiles[10][10].set_spawn(bscp.Entities.NPC.SD(10.0, 10.0, BSCP_GAME))
        BSCP_GAME.map.tiles[0][0].set_spawn(bscp.Entities.NPC.SID(0.0, 0.0, BSCP_GAME))

    game()
    rendering()
    panels()
    spawners()


def launch():
    init()
    accumulated_time = 0.0

    try:
        while BSCP_GAME.window.running:
            CLOCK.tick()
            dt = CLOCK.delta_time
            handle_event()
            update_and_compute()
            accumulated_time += dt
            if accumulated_time >= TARGET_FRAME_TIME:
                draw()
                CLOCK.frame()
                BSCP_GAME.add_fps(CLOCK.fps)
                accumulated_time -= TARGET_FRAME_TIME

    except KeyboardInterrupt:
        bscp.Systems.open_log().log("WARN", "BSCP", f"Game forcefully exited")

    finally:
        BSCP_GAME.destroy()
        if BSCP_GAME.get_flag("show-log"):
            BSCP_GAME.show_log()


if __name__ == "__main__":
    error: bool = False

    try:
        launch()

    except KeyboardInterrupt:
        error = True
        bscp.Systems.open_log().log("ERROR", "BSCP", f"Game forcefully exited before successfully opened")

    except BaseException as e:
        error = True
        bscp.Systems.open_log().log("CRIT", "BSCP", f"Unknown Exception: {repr(e)}")

    finally:
        if error:
            bscp.Systems.open_log().close()
            print(str(bscp.Systems.open_log().filter(["WARN", "ERROR", "CRIT"] + (["DEBUG"] if bscp.Systems.open_config().get_bool("GAME", "debug") else []))))
