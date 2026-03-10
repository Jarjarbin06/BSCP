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

    dt = 0.016  # simulate ~60 FPS
    target = BSCP.Utils.Vector(5, 10)

    # Create a mobile SCP with health
    scp = BSCP.Entities.SCPs.SCP(
        name="SCP-001",
        position=BSCP.Utils.Vector(10, 5),
        anomaly_id="SCP-001",
        max_health=100,
        max_speed=5.0,
        mobile=True
    )

    print(f"Initial position: {scp.position}")
    print(f"Is alive? {scp.is_alive()}")
    print(f"Health: {scp.health.health if scp.health else 'N/A'}")
    print(f"Containment active? {scp.containment.active if scp.containment else 'N/A'}")

    # Test movement towards a target
    scp.move_towards(target, dt)
    scp.update(dt)
    print(f"Position after move_towards: {scp.position}")

    # Test damage and is_alive
    if scp.health:
        scp.health.damage(50)
    print(f"Health after 50 damage: {scp.health.health if scp.health else 'N/A'}")
    print(f"Is alive? {scp.is_alive()}")

    # Apply more damage to kill
    if scp.health:
        scp.health.damage(60)
    scp.update(dt)
    print(f"Health after 60 more damage: {scp.health.health if scp.health else 'N/A'}")
    print(f"Is alive? {scp.is_alive()}")

    # Test path reset by moving to a new target
    new_target = BSCP.Utils.Vector(15, 15)
    scp.move_towards(new_target, dt)
    scp.update(dt)
    print(f"Position after new target move: {scp.position}")