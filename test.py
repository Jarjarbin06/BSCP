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
    from bscp.Entities.Components.ai import AIComponent

    # --------------------------
    # Game
    # --------------------------

    BSCP.Systems.open_log().delete()
    log: BSCP.Utils.BSCPLog = BSCP.Systems.open_log()

    pygame.init()

    # Initialize game
    game = BSCP.Core.Game()

    # --------------------------
    # TileMap
    # --------------------------

    from bscp.Map import Tile, TileMap, MapLoader

    tilemap = TileMap(width=17, height=17)
    for row in tilemap.tiles:
        for tile in row:
            tile.color = {
                "floor": (50, 50, 50),
                "wall": (100, 100, 100),
                "containment": (150, 0, 150),
                "spawn": (0, 150, 0),
            }.get(tile.type.lower(), (200, 200, 200))

    # Walls / containment
    for y in range(1, 8):
        tilemap.tiles[y][7] = Tile(7, y, type="wall", walkable=False)

    game.tilemap = tilemap

    MapLoader.save(tilemap, "test_map.json")
    MapLoader.load(tilemap, "test_map.json")

    # --------------------------
    # Entity
    # --------------------------

    # Add NPCs
    npc1 = BSCP.Entities.Factions.NPC("ClassD Worker", BSCP.Utils.Vector(10, 5), faction_id="CD")
    npc2 = BSCP.Entities.Factions.NPC("Researcher", BSCP.Utils.Vector(12, 8), faction_id="SCD")
    game.add_npc(npc1)
    game.add_npc(npc2)
    BSCP.Map.Map.move_entity(npc1, npc1.position, tilemap)
    BSCP.Map.Map.move_entity(npc2, npc2.position, tilemap)

    # Add SCPs
    scp1 = BSCP.Entities.SCPs.SCP("SCP-173", BSCP.Utils.Vector(5, 5), mobile=True, max_speed=5.0)
    scp2 = BSCP.Entities.SCPs.SCP("SCP-049", BSCP.Utils.Vector(5, 7), mobile=True, max_speed=2.5)
    game.add_scp(scp1)
    game.add_scp(scp2)
    BSCP.Map.Map.move_entity(scp1, scp1.position, tilemap)
    BSCP.Map.Map.move_entity(scp2, scp2.position, tilemap)

    # Create window
    window = BSCP.Core.Window(width=500, height=500, title="BSCP : Foundation Architect")

    # --------------------------
    # SPRITE LOADING
    # --------------------------

    SPRITES = {
        "ClassD Worker": pygame.image.load(BSCP.Entities.Factions.Factions.FACTIONS_LOGO["CD"]).convert_alpha(),
        "Researcher": pygame.image.load(BSCP.Entities.Factions.Factions.FACTIONS_LOGO["SCD"]).convert_alpha(),
        "SCP-173": pygame.image.load(BSCP.Entities.SCPs.SCPs.SCPS_LOGO["SCPB"]).convert_alpha(),
        "SCP-049": pygame.image.load(BSCP.Entities.SCPs.SCPs.SCPS_LOGO["SCPB"]).convert_alpha()
    }

    TILE_SIZE = 30
    for key in SPRITES:
        SPRITES[key] = pygame.transform.scale(SPRITES[key], (TILE_SIZE, TILE_SIZE))

    # --------------------------
    # Main Loop
    # --------------------------

    running = True
    npc_radius = 0.2
    scp_radius = 0.24

    while running and window.running:
        game.clock.tick()
        dt = game.clock.delta_time
        game.dt = dt

        for event in window.poll_events():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                MapLoader.save(tilemap, "test_map.json")
                print("[INFO] Map saved")

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                tx, ty = mx // TILE_SIZE, my // TILE_SIZE
                if 0 <= tx < tilemap.width and 0 <= ty < tilemap.height:
                    tile = tilemap.tiles[ty][tx]
                    tile.walkable = not tile.walkable
                    tile.color = (0, 200, 0) if tile.walkable else (200, 0, 0)

        # --------------------------
        # SCP AI with pathfinding
        # --------------------------

        for scp in game.scps:
            if not game.npcs:
                continue

            nearest = min(game.npcs, key=lambda npc: (npc.position - scp.position).length())

            # Generate path if missing or target changed
            if scp.movement:
                # Only recompute path if empty or target changed
                if not scp.movement.path or scp.movement.path[-1] != nearest.position:
                    # find_path returns tile positions; convert to world coordinates if needed
                    path_tiles = scp.ai.find_path(scp.position, nearest.position)
                    print(path_tiles)
                    if path_tiles:
                        scp.movement.path = path_tiles  # keep as Vector list
                        scp.movement.path_index = 0

            # Follow path
            if scp.movement and scp.movement.path:
                scp._follow_path(dt, tilemap)

            # Attack
            if (nearest.position - scp.position).length() <= npc_radius + scp_radius:
                game.log.info("SCP Attack", f"{scp.name} destroyed {nearest.name}")
                game.npcs.remove(nearest)

        game.update_entities()

        # --------------------------
        # DRAW
        # --------------------------

        window.clear((30, 30, 30))

        for y, row in enumerate(tilemap.tiles):
            for x, tile in enumerate(row):
                pygame.draw.rect(window.surface, tile.color, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        for npc in game.npcs:
            sprite = SPRITES.get(npc.name)
            if sprite:
                window.surface.blit(sprite, (int(npc.position.x * TILE_SIZE), int(npc.position.y * TILE_SIZE)))

        for scp in game.scps:
            sprite = SPRITES.get(scp.name)
            if sprite:
                window.surface.blit(sprite, (int(scp.position.x * TILE_SIZE), int(scp.position.y * TILE_SIZE)))

        window.display()
        game.clock.sleep(0.016)

    # --------------------------
    # Shutdown
    # --------------------------

    tilemap.debug_print()
    print("[INFO] Simulation finished")
    game.save_game()
    MapLoader.save(tilemap, "test_map.json")
    window.destroy()
    log.close()