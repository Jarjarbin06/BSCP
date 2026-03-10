# Game API

The `Game` class provides **core game management** for BSCP, including entity handling, game loop timing, saving/loading, and simulation updates. It acts as the central orchestrator for NPCs, SCPs, and other game systems.

---

# Class: `Game`

```python
Game()
```

Creates a new game instance.

### Attributes

| Name        | Type        | Description                                   |
|-------------|-------------|-----------------------------------------------|
| `npcs`      | `List[NPC]` | List of NPC entities                          |
| `scps`      | `List[SCP]` | List of SCP entities                          |
| `clock`     | `Clock`     | Game clock for delta time and FPS calculation |
| `dt`        | `float`     | Delta time for current update step            |
| `log`       | `BSCPLog`   | Central logging instance                      |
| `save_path` | `str`       | Directory where saves are stored              |

---

# NPC Management

## Add NPC

```python
game.add_npc(npc: NPC) -> None
```

Adds an NPC to the game.

**Example:**

```python
game.add_npc(NPC("ClassD Worker", Vector(10,5), faction_id="CD"))
```

---

## Get NPC

```python
game.get_npc(identifier: str | int) -> NPC | None
```

Retrieves a single NPC by **name or index**. Returns `None` if not found.

**Example:**

```python
npc = game.get_npc("ClassD Worker")
npc2 = game.get_npc(0)
```

---

## Get All NPCs

```python
game.get_all_npcs() -> List[NPC]
```

Returns a **copy of the list of all NPCs**.

---

# SCP Management

## Add SCP

```python
game.add_scp(scp: SCP) -> None
```

Adds an SCP entity to the game.

---

## Get SCP

```python
game.get_scp(identifier: str | int) -> SCP | None
```

Retrieves a single SCP by **name or index**. Returns `None` if not found.

---

## Get All SCPs

```python
game.get_all_scps() -> List[SCP]
```

Returns a **copy of the list of all SCPs**.

---

# Entity Updates

## Update All Entities

```python
game.update_entities() -> None
```

Updates all NPCs and SCPs with the **current delta time**.

**Example:**

```python
game.update_entities()
```

---

# Save / Load Game

## Save Game

```python
game.save_game(file_name: str = "game_save") -> None
```

Serializes all NPCs and SCPs into a **JSON save file**.

**Example:**

```python
game.save_game("level_1_save")
```

---

## Load Game

```python
game.load_game(file_name: str = "game_save") -> None
```

Loads a previously saved game, restoring all entities. If the file does not exist, the method **fails silently**.

**Example:**

```python
game.load_game("level_1_save")
```

---

# Game Loop

## Run Simulation

```python
game.run(steps: int = 10) -> None
```

Runs a simple **fixed-step simulation loop** for the given number of steps:

* Updates the clock
* Updates all entities
* Sleeps for ~16ms per step (60 FPS)

**Parameters:**

| Name  | Type | Description            |
|-------|------|------------------------|
| steps | int  | Number of update steps |

**Example:**

```python
game.run(steps=5)
```

---

# Typical Engine Usage

```python
game = Game()

# Add entities
game.add_npc(NPC("ClassD Worker", Vector(10,5), faction_id="CD"))
game.add_scp(SCP("SCP-173", Vector(5,5), mobile=True))

# Run simulation
game.run(steps=10)

# Save progress
game.save_game("session_1")

# Later: load game
game.load_game("session_1")

# Access entities
npc = game.get_npc("ClassD Worker")
scp = game.get_scp("SCP-173")
```

This class **centralizes entity management, simulation updates, and persistence**, forming the backbone of BSCP's core gameplay.

---

---

# Window API

The `Window` class provides a **lightweight wrapper around Pygame** for BSCP, handling window creation, resizing, event polling, rendering, and cleanup. It abstracts Pygame’s boilerplate while supporting a basic game loop.

---

# Class: `Window`

```python id="w1n0do"
Window(width: int = 1280, height: int = 720, title: str = "BSCP : Foundation Architect", vsync: bool = True)
```

Creates a new game window.

### Parameters

| Name   | Type | Description                           |
|--------|------|---------------------------------------|
| width  | int  | Window width in pixels                |
| height | int  | Window height in pixels               |
| title  | str  | Window title                          |
| vsync  | bool | Enable vertical sync (frame limiting) |

### Example

```python id="ex_window_init"
window = Window(1280, 720, "BSCP", vsync=True)
```

---

# Properties

## Running

```python id="w_running"
window.running -> bool
```

Indicates whether the window is still active.

---

## Surface

```python id="w_surface"
window.surface -> pygame.Surface
```

Returns the Pygame surface for drawing operations.

---

## Width & Height

```python id="w_size"
window.width -> int
window.height -> int
```

Returns the current window dimensions.

---

# Event Handling

## Poll Events

```python id="w_poll"
window.poll_events() -> Generator[pygame.event.EventType, None, None]
```

Yields events from the Pygame event queue. Automatically handles:

* `QUIT` event → closes the window
* `VIDEORESIZE` → updates the window surface and dimensions

**Example:**

```python id="w_poll_example"
for event in window.poll_events():
    if event.type == pygame.KEYDOWN:
        print("Key pressed:", event.key)
```

---

# Rendering

## Clear

```python id="w_clear"
window.clear(color: tuple[int, int, int] = (0,0,0)) -> None
```

Clears the window with the specified color.

---

## Display

```python id="w_display"
window.display() -> None
```

Flips the display buffer, rendering all drawings to the screen.

---

# Window Control

## Close

```python id="w_close"
window.close() -> None
```

Marks the window as **no longer running**. Used to exit the main loop.

---

## Destroy

```python id="w_destroy"
window.destroy() -> None
```

Quits Pygame and cleans up resources. Should be called when the window is no longer needed.

---

# Representation

```python id="w_repr"
repr(window) -> str
```

Returns a descriptive string:

```
<Window 1280x720 running=True>
```

---

# Typical Engine Usage

```python id="w_usage"
window = Window(1280, 720, "BSCP", vsync=True)

while window.running:
    # Handle events
    for event in window.poll_events():
        if event.type == pygame.KEYDOWN:
            print("Key pressed:", event.key)

    # Clear, draw, display
    window.clear((50, 50, 50))
    # ... draw game objects here ...
    window.display()

window.destroy()
```

This class **centralizes window management** and integrates seamlessly with the game loop, event system, and rendering pipeline in BSCP.

---

---

# Clock API

The `Clock` class provides a **high-precision timing system** for BSCP, used to:

* track frame-to-frame time (`delta_time`)
* control simulation speed via `time_scale`
* compute frames per second (FPS)
* implement sleep and frame pacing

It is integrated into the main game loop to ensure **consistent timing** regardless of system performance.

---

# Class: `Clock`

```python id="clk1"
Clock()
```

Creates a new clock instance, initialized with the current high-precision time.

### Properties

| Property   | Type  | Description                              |
|------------|-------|------------------------------------------|
| delta_time | float | Time elapsed since the last tick, scaled |
| time_scale | float | Factor to scale time; 1.0 = real time    |
| fps        | float | Current frames per second                |

---

# Time Scale

## Get / Set Time Scale

```python id="clk2"
clock.time_scale -> float
clock.time_scale = scale
```

* `scale` must be **positive**
* Used to **speed up or slow down** the simulation

**Example:**

```python id="clk3"
clock.time_scale = 2.0   # time runs twice as fast
clock.time_scale = 0.5   # half-speed
```

---

# Tick

```python id="clk4"
clock.tick() -> None
```

Updates the clock:

* Calculates `delta_time` since last tick
* Updates FPS every second
* Increments internal frame counter

**Example:**

```python id="clk5"
clock.tick()
print(clock.delta_time)
print(clock.fps)
```

---

# Sleep

```python id="clk6"
clock.sleep(duration: float) -> None
```

Pauses execution for a duration in seconds, **scaled by `time_scale`**.

* `duration` must be non-negative

**Example:**

```python id="clk7"
clock.sleep(0.016)  # ~16ms per frame (~60 FPS)
```

---

# Reset

```python id="clk8"
clock.reset() -> None
```

Resets the internal timers and frame counters. Use when restarting a simulation or resetting timing.

**Example:**

```python id="clk9"
clock.reset()
```

---

# Representation

```python id="clk10"
repr(clock) -> str
```

Returns a human-readable string showing:

* `delta_time`
* `fps`
* `time_scale`

**Example:**

```python id="clk11"
print(clock)
# <Clock delta_time=0.0167 fps=60.12 time_scale=1.0>
```

---

# Typical Engine Usage

### Main Game Loop

```python id="clk12"
while running:
    clock.tick()           # update timing
    dt = clock.delta_time  # scaled delta time

    update_entities(dt)    # move NPCs, SCPs, etc.

    clock.sleep(0.016)     # pace to ~60 FPS
```

---

### Time Manipulation

```python id="clk13"
clock.time_scale = 0.5  # slow-motion effect
clock.time_scale = 2.0  # fast-forward effect
```

The `Clock` ensures **consistent simulation timing** independent of actual frame execution speed, making it ideal for physics, AI, and animation updates.

---

---

# EventManager API

The `EventManager` class provides a **centralized event dispatching system** for BSCP, supporting:

* entity, SCP, and facility events
* player and UI interactions
* queuing and processing events
* subscription and unsubscription of listeners

It enables **decoupled communication** between systems, entities, and game logic.

---

# Class: `EventManager`

```python
EventManager()
```

Creates a new event manager instance.

### Attributes

| Name       | Type                    | Description                               |
|------------|-------------------------|-------------------------------------------|
| _listeners | `dict[str, list]`       | Registered event listeners per event name |
| _queue     | `list[tuple[str, Any]]` | Queued events waiting to be processed     |

---

# Subscription

## Subscribe to an Event

```python
event_manager.subscribe(event: str, listener: Callable) -> None
```

Registers a listener callback for a specific event.

**Parameters:**

| Name     | Type     | Description                       |
|----------|----------|-----------------------------------|
| event    | str      | Event name                        |
| listener | Callable | Function called when event occurs |

**Example:**

```python
def on_entity_spawned(data):
    print("Entity spawned:", data.name)

event_manager.subscribe("entity_spawned", on_entity_spawned)
```

---

## Unsubscribe from an Event

```python
event_manager.unsubscribe(event: str, listener: Callable) -> None
```

Removes a listener from an event.

**Example:**

```python
event_manager.unsubscribe("entity_spawned", on_entity_spawned)
```

---

# Emitting Events

## Emit Immediately

```python
event_manager.emit(event: str, data: Any = None) -> None
```

Triggers the event and **calls all listeners immediately**.

**Example:**

```python
event_manager.emit("entity_spawned", npc_instance)
```

---

## Queue Event

```python
event_manager.queue(event: str, data: Any = None) -> None
```

Adds an event to the **queue** for deferred processing.

**Example:**

```python
event_manager.queue("scp_breach", scp_instance)
```

---

## Process Queued Events

```python
event_manager.process() -> None
```

Processes all queued events by calling the associated listeners.

**Example:**

```python
event_manager.process()
```

---

# Utility Methods

## Clear All

```python
event_manager.clear() -> None
```

Removes all listeners and clears the event queue.

---

# Representation

```python
repr(event_manager) -> str
```

Returns a string showing the **number of listeners** and **queued events**.

**Example:**

```python
print(event_manager)
# <EventManager listeners=12 queued=3>
```

---

# Common Event Names

### Entity Events

| Event              | Description        |
|--------------------|--------------------|
| `ENTITY_SPAWNED`   | Entity created     |
| `ENTITY_DESTROYED` | Entity removed     |
| `ENTITY_MOVED`     | Entity moved       |
| `ENTITY_DAMAGED`   | Entity took damage |

### SCP Events

| Event           | Description              |
|-----------------|--------------------------|
| `SCP_BREACH`    | SCP containment breached |
| `SCP_CONTAINED` | SCP secured              |
| `SCP_DETECTED`  | SCP detected by systems  |

### Facility Events

| Event              | Description              |
|--------------------|--------------------------|
| `ALARM_TRIGGERED`  | Facility alarm activated |
| `ALARM_CLEARED`    | Alarm deactivated        |
| `LOCKDOWN_STARTED` | Lockdown activated       |
| `LOCKDOWN_ENDED`   | Lockdown ended           |
| `POWER_FAILURE`    | Power failure occurred   |
| `POWER_RESTORED`   | Power restored           |

### Door Events

| Event           | Description   |
|-----------------|---------------|
| `DOOR_OPENED`   | Door opened   |
| `DOOR_CLOSED`   | Door closed   |
| `DOOR_LOCKED`   | Door locked   |
| `DOOR_UNLOCKED` | Door unlocked |

### Interaction Events

| Event            | Description             |
|------------------|-------------------------|
| `BUTTON_PRESSED` | Physical button pressed |
| `CONSOLE_USED`   | Console interacted with |

### Player Events

| Event            | Description           |
|------------------|-----------------------|
| `PLAYER_SPAWNED` | Player created        |
| `PLAYER_DIED`    | Player death occurred |
| `PLAYER_MOVED`   | Player moved          |

### UI Events

| Event               | Description          |
|---------------------|----------------------|
| `UI_BUTTON_CLICKED` | Button clicked in UI |
| `UI_PANEL_OPENED`   | Panel opened         |
| `UI_PANEL_CLOSED`   | Panel closed         |

---

# Typical Engine Usage

```python
event_manager = EventManager()

# Listen for an SCP breach
def alert_scp_breach(scp):
    print("ALERT! SCP breached:", scp.name)

event_manager.subscribe(SCP_BREACH, alert_scp_breach)

# Emit an event
event_manager.emit(SCP_BREACH, scp_instance)

# Queue multiple events
event_manager.queue(ENTITY_MOVED, npc_instance)
event_manager.queue(PLAYER_MOVED, player_instance)

# Process queued events
event_manager.process()
```

This system allows BSCP to **react to all game events in a decoupled, modular manner**, making it easy to connect gameplay logic, UI updates, and logging.
