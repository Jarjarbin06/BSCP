###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


if __name__ == "__main__":
    print("[INFO] Launching BSCP...")

    import bscp as BSCP
    import pygame

    BSCP.Systems.open_log().delete()
    log: BSCP.Utils.BSCPLog = BSCP.Systems.open_log()

    # Initialize game
    game = BSCP.Core.Game()

    # Add NPCs
    game.add_npc(BSCP.Entities.Factions.NPC("ClassD Worker", BSCP.Utils.Vector(10, 5), faction_id="CD"))
    game.add_npc(BSCP.Entities.Factions.NPC("Researcher", BSCP.Utils.Vector(20, 8), faction_id="SCD"))

    # Add SCPs
    game.add_scp(BSCP.Entities.SCPs.SCP("SCP-173", BSCP.Utils.Vector(5, 5), mobile=True))
    game.add_scp(BSCP.Entities.SCPs.SCP("SCP-049", BSCP.Utils.Vector(10, 12), mobile=True))

    # Create window
    window = BSCP.Core.Window(width=1280, height=720, title="BSCP : Foundation Architect")

    # --------------------------
    # TileMap test
    # --------------------------
    from bscp.Map import Tile, TileMap, MapLoader

    tilemap = TileMap(width=20, height=15)
    tile_size = 32  # pixels per tile

    # Initialize tile colors
    for row in tilemap.tiles:
        for tile in row:
            tile.color = {
                "floor": (50, 50, 50),
                "wall": (100, 100, 100),
                "containment": (150, 0, 150),
                "spawn": (0, 150, 0),
            }.get(tile.type.lower(), (200, 200, 200))

    # Optional: modify some tiles for testing
    tilemap.tiles[5][5] = Tile(5, 5, type="wall", walkable=False)
    tilemap.tiles[6][5] = Tile(6, 5, type="containment", walkable=False)
    tilemap.tiles[5][5].color = (100, 100, 100)
    tilemap.tiles[6][5].color = (150, 0, 150)

    # Save initial map
    MapLoader.save(tilemap, "test_map.json")
    # Load map back to test
    MapLoader.load(tilemap, "test_map.json")

    # --------------------------
    # Main game loop with SCP chasing, NPC destruction, and tilemap rendering
    # --------------------------
    running = True
    steps = 0
    max_steps = 0  # 0 = unlimited
    chase_speed = 1.5  # units per second
    npc_radius = 0.2  # approximate collision radius
    scp_radius = 0.24  # slightly bigger than NPC

    while running and window.running:
        # Tick clock
        game.clock.tick()
        dt = game.clock.delta_time
        game.dt = dt

        # Poll window events
        for event in window.poll_events():
            if event.type == pygame.KEYDOWN:
                # Press S to save map during runtime
                if event.key == pygame.K_s:
                    MapLoader.save(tilemap, "test_map.json")
                    print("[INFO] Map saved during runtime")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                tx = mx // tile_size
                ty = my // tile_size
                if 0 <= tx < tilemap.width and 0 <= ty < tilemap.height:
                    tile = tilemap.tiles[ty][tx]
                    # Toggle walkable and update color
                    tile.walkable = not tile.walkable
                    tile.color = (0, 200, 0) if tile.walkable else (200, 0, 0)

        # Update game logic
        for scp in game.scps:
            if game.npcs:
                nearest_npc = min(game.npcs, key=lambda npc: (npc.position - scp.position).length())
                direction = (nearest_npc.position - scp.position)
                if direction.length() > 0:
                    move_vector = direction.normalize() * chase_speed * dt
                    scp.position += move_vector
                # Collision
                distance = (nearest_npc.position - scp.position).length()
                if distance <= (npc_radius + scp_radius):
                    game.log.info("SCP Attack", f"{scp.name} destroyed {nearest_npc.name}")
                    game.npcs.remove(nearest_npc)
                    if hasattr(game, "event_manager"):
                        game.event_manager.emit("ENTITY_DESTROYED", nearest_npc)

        game.update_entities()

        # Clear window
        window.clear((30, 30, 30))

        # Draw tilemap
        for y, row in enumerate(tilemap.tiles):
            for x, tile in enumerate(row):
                pygame.draw.rect(
                    window.surface,
                    tile.color,
                    pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                )

        # Draw entities
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
    tilemap.debug_print()

    print("[INFO] Simulation finished")
    game.save_game()
    MapLoader.save(tilemap, "test_map.json")  # final save
    window.destroy()
    log.close()
