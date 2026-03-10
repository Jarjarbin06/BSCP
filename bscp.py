###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import jarbin_toolkit as JTK


if __name__ == "__main__":
    import bscp as BSCP
    import pygame

    BSCP.Systems.open_log().delete()
    log: BSCP.Utils.BSCPLog = BSCP.Systems.open_log()

    # Initialize game
    game = BSCP.Core.Game()

    # Add NPCs
    game.add_npc(BSCP.Entities.Factions.NPC("ClassD Worker", BSCP.Utils.Vector(10, 5), faction_id="CD"))
    game.add_npc(BSCP.Entities.Factions.NPC("Researcher", BSCP.Utils.Vector(12, 8), faction_id="SCD"))

    # Add SCPs
    game.add_scp(BSCP.Entities.SCPs.SCP("SCP-173", BSCP.Utils.Vector(5, 5), mobile=True))
    game.add_scp(BSCP.Entities.SCPs.SCP("SCP-049", BSCP.Utils.Vector(15, 10), mobile=True))

    # Create window
    window = BSCP.Core.Window(width=1280, height=720, title="BSCP : Foundation Architect")

    # --------------------------
    # Main game loop
    # --------------------------
    running = True
    steps = 0
    max_steps = 0  # 0 = unlimited
    while running and window.running:
        # Tick clock
        game.clock.tick()
        game.dt = game.clock.delta_time

        # Poll window events
        for event in window.poll_events():
            pass  # add input handling if needed

        # Update game logic
        game.update_entities()

        # Clear window
        window.clear((30, 30, 30))

        # Draw entities (simple placeholder)
        for npc in game.npcs:
            pygame.draw.circle(
                window.surface,
                (0, 255, 0),
                (int(npc.position.x * 50), int(npc.position.y * 50)),
                10
            )
        for scp in game.scps:
            pygame.draw.circle(
                window.surface,
                (255, 0, 0),
                (int(scp.position.x * 50), int(scp.position.y * 50)),
                12
            )

        # Display frame
        window.display()

        # Optional debug logging
        for npc in game.npcs:
            game.log.debug("NPC Update", f"{npc.name} at {npc.position}")
        for scp in game.scps:
            game.log.debug("SCP Update", f"{scp.name} at {scp.position}")

        steps += 1
        if max_steps != 0 and steps >= max_steps:
            running = False

        # Cap frame rate (~60 FPS)
        game.clock.sleep(0.016)

    # --------------------------
    # After loop
    # --------------------------
    print("[INFO] Simulation finished")
    game.save_game()
    window.destroy()
    log.close()
