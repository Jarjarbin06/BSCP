# FileUtils API

The `FileUtils` class provides **robust file and directory management** for BSCP, supporting:

* JSON and binary serialization
* File existence checks
* Directory creation
* File deletion and listing

It is used across the engine for:

* Map saving/loading
* Entity state persistence
* Configuration and save game management

---

# Class: `FileUtils`

```python
FileUtils
```

Utility class; **all methods are static**. No instantiation required.

---

# Directory Management

## Ensure Directory

```python
FileUtils.ensure_dir(path: str) -> None
```

Creates the directory if it does not exist.

**Parameters:**

| Name | Type | Description           |
|------|------|-----------------------|
| path | str  | Path to the directory |

**Example:**

```python
FileUtils.ensure_dir("saves/maps")
```

---

# JSON Methods

## Save JSON

```python
FileUtils.save_json(data: Any, path: str, file_name: str) -> None
```

Saves Python data as a **JSON file**.

**Example:**

```python
FileUtils.save_json({"score": 100}, "saves", "game_state")
```

---

## Load JSON

```python
FileUtils.load_json(path: str, file_name: str) -> Any
```

Loads data from a JSON file. Raises `FileNotFoundError` if file does not exist.

**Example:**

```python
data = FileUtils.load_json("saves", "game_state")
```

---

# Binary Methods

## Save Binary

```python
FileUtils.save_binary(data: Any, path: str, file_name: str) -> None
```

Saves Python objects using **pickle** (binary format).

**Example:**

```python
FileUtils.save_binary(player_object, "saves/players", "player1")
```

---

## Load Binary

```python
FileUtils.load_binary(path: str, file_name: str) -> Any
```

Loads data from a binary file. Raises `FileNotFoundError` if file does not exist.

**Example:**

```python
player = FileUtils.load_binary("saves/players", "player1")
```

---

# File Utilities

## Check File Existence

```python
FileUtils.exists(path: str, file_name: str, extension: str) -> bool
```

Checks if a file exists with a specific extension.

**Example:**

```python
if FileUtils.exists("saves/maps", "level_1", "json"):
    print("Map exists!")
```

---

## Delete File

```python
FileUtils.delete(path: str, file_name: str, extension: str) -> None
```

Deletes a file if it exists.

**Example:**

```python
FileUtils.delete("saves/maps", "level_1", "json")
```

---

## List Files

```python
FileUtils.list_files(path: str, extension: str | None = None) -> list[str]
```

Lists files in a directory. Optionally filters by extension.

**Example:**

```python
files = FileUtils.list_files("saves/maps", "json")
print(files)
# ["level_1.json", "level_2.json"]
```

---

# Typical Engine Usage

### Save a Map

```python
map_data = {"tiles": [...], "entities": [...]}
FileUtils.save_json(map_data, "saves/maps", "level_1")
```

---

### Load a Map

```python
map_data = FileUtils.load_json("saves/maps", "level_1")
```

---

### Save Player Data

```python
FileUtils.save_binary(player_object, "saves/players", "player1")
```

---

### Manage Files

```python
# Check
FileUtils.exists("saves/maps", "level_1", "json")

# Delete
FileUtils.delete("saves/maps", "level_1", "json")

# List
files = FileUtils.list_files("saves/maps", "json")
```

---

---

# BSCPLog API

The `BSCPLog` class provides a **structured logging system** for BSCP.
It wraps `jarbin_toolkit_log` and offers:

* multiple log levels
* automatic file creation with timestamps
* optional JSON output
* convenience methods for common log statuses

---

# Class: `BSCPLog`

```python
BSCPLog(path: str, file_name: str | None = None, json: bool = False)
```

Creates a log manager instance.

### Parameters

| Name      | Type   | Description                                             |
|-----------|--------|---------------------------------------------------------|
| path      | `str`  | Directory to store log files                            |
| file_name | `str`  | Optional custom file name; defaults to timestamped name |
| json      | `bool` | Whether to save logs in JSON format                     |

**Example:**

```python
log = BSCPLog("log/")
```

---

# Logging Methods

## General Log

```python
log.log(status: str, title: str, description: str)
```

Logs a message with a given status.

| Status Options | Description           |
|----------------|-----------------------|
| INFO           | Informational message |
| VALID          | Success / validation  |
| WARN           | Warning               |
| ERROR          | Error                 |
| DEBUG          | Debugging message     |

**Example:**

```python
log.log("INFO", "GameStart", "The game has started successfully")
```

---

## Convenience Methods

Shortcut methods for each log status:

```python
log.info(title, description)
log.valid(title, description)
log.warn(title, description)
log.error(title, description)
log.debug(title, description)
```

**Example:**

```python
log.info("Init", "Engine initialized")
log.warn("Performance", "Low FPS detected")
```

---

# Comments

```python
log.comment(comment: str)
```

Adds a plain comment to the log without a status.

**Example:**

```python
log.comment("Checkpoint reached in level 1")
```

---

# File Operations

## Save Raw Log

```python
log.save_raw(log_str: str)
```

Saves a raw string directly into the log file.

---

## Read Log

```python
log.read() -> str
```

Returns the log content as a string.

---

## Close Log

```python
log.close()
```

Closes the log file safely.

---

## Delete Log

```python
log.delete()
```

Removes the log file from disk.

---

# Typical Engine Usage

### Logging Game Events

```python
log = BSCPLog("log/")
log.info("Init", "Engine started")
log.valid("Map", "Map loaded successfully")
log.warn("Performance", "Frame drop detected")
log.error("AI", "NPC pathfinding failed")
log.debug("Physics", "Velocity vector: (5, 0)")
```

---

### Adding Comments

```python
log.comment("Reached the first checkpoint")
```

---

---

# Math Utilities API

The `math_utils` module provides **helper functions for vector mathematics, interpolation, angles, and value clamping**.
Used throughout the engine for:

* distance calculations
* angle computations
* linear interpolation (lerp)
* clamping values within ranges

Works seamlessly with the `Vector` class.

---

# Functions

## Distance

```python
distance(p1: Vector, p2: Vector) -> float
```

Returns the Euclidean distance between two vectors.

### Parameters

| Name | Type   | Description  |
|------|--------|--------------|
| p1   | Vector | First point  |
| p2   | Vector | Second point |

**Example:**

```python
from bscp.utils.vector import Vector
from bscp.utils.math_utils import distance

a = Vector(0,0)
b = Vector(3,4)
distance(a,b)
# 5.0
```

---

## Angle Between

```python
angle_between(p1: Vector, p2: Vector, in_radians: bool = True) -> float
```

Computes the angle from `p1` to `p2`.

### Parameters

| Name       | Type   | Description                              |
|------------|--------|------------------------------------------|
| p1         | Vector | First point/vector                       |
| p2         | Vector | Second point/vector                      |
| in_radians | bool   | If `True`, returns radians; else degrees |

**Example:**

```python
angle_between(Vector(1,0), Vector(0,1))
# 1.5707963267948966 (radians)

angle_between(Vector(1,0), Vector(0,1), in_radians=False)
# 90.0 (degrees)
```

---

## Linear Interpolation (Lerp)

```python
lerp(v1: Vector, v2: Vector, t: float) -> Vector
```

Returns a **point along the line** between `v1` and `v2`, based on interpolation factor `t`.

### Parameters

| Name | Type   | Description                      |
|------|--------|----------------------------------|
| v1   | Vector | Start vector                     |
| v2   | Vector | End vector                       |
| t    | float  | Interpolation factor (0.0 — 1.0) |

**Example:**

```python
lerp(Vector(0,0), Vector(10,10), 0.5)
# Vector(5, 5)
```

---

## Clamp

```python
clamp(val: float, min_val: float, max_val: float) -> float
```

Clamps a value within a range `[min_val, max_val]`.

### Parameters

| Name    | Type  | Description           |
|---------|-------|-----------------------|
| val     | float | Value to clamp        |
| min_val | float | Minimum allowed value |
| max_val | float | Maximum allowed value |

**Example:**

```python
clamp(15.0, 0.0, 10.0)
# 10.0

clamp(-5.0, 0.0, 10.0)
# 0.0
```

---

# Typical Engine Usage

### Distance Check

```python
if distance(player.position, enemy.position) < 50:
    alert()
```

---

### Angle Computation

```python
angle = angle_between(player.position, target.position)
```

---

### Smooth Movement

```python
entity.position = lerp(entity.position, target.position, 0.1)
```

---

### Value Limiting

```python
health = clamp(health, 0.0, 100.0)
```

---

---

# Vector API

The `Vector` class provides a lightweight **2D mathematical vector implementation** used throughout the engine for:

* positions
* directions
* velocities
* distances
* rotations

It supports **vector arithmetic, normalization, geometry operations, and rotation**.

---

# Class: `Vector`

```python
Vector(x: Real, y: Real)
```

Creates a 2D vector.

### Parameters

| Name | Type   | Description          |
|------|--------|----------------------|
| x    | `Real` | Horizontal component |
| y    | `Real` | Vertical component   |

Example:

```python
pos = Vector(10, 5)
```

---

# Basic Operations

## Addition

```python
v1 + v2
v1 += v2
```

Returns the sum of two vectors.

Example:

```python
Vector(1, 2) + Vector(3, 4)
# Vector(4, 6)
```

---

## Subtraction

```python
v1 - v2
v1 -= v2
```

Example:

```python
Vector(5, 3) - Vector(2, 1)
# Vector(3, 2)
```

---

## Scalar Multiplication

```python
v * scalar
v *= scalar
```

Example:

```python
Vector(2, 3) * 2
# Vector(4, 6)
```

---

## Scalar Division

```python
v / scalar
v /= scalar
```

Division by zero raises `ZeroDivisionError`.

---

## Negation

```python
-v
```

Example:

```python
-Vector(2, 3)
# Vector(-2, -3)
```

---

# Vector Properties

## Length

```python
v.length()
```

Returns the magnitude of the vector.

Example:

```python
Vector(3, 4).length()
# 5
```

---

## Normalization

```python
v.normalize()
```

Returns a **unit vector** pointing in the same direction.

If the vector length is zero, `(0,0)` is returned.

Example:

```python
Vector(10, 0).normalize()
# Vector(1, 0)
```

---

## Distance Between Vectors

```python
v1.distance_to(v2)
```

Returns the Euclidean distance.

Example:

```python
Vector(0,0).distance_to(Vector(3,4))
# 5
```

---

## Direction Between Vectors

```python
v1.direction_to(v2)
```

Returns a **normalized direction vector** pointing to `v2`.

Example:

```python
Vector(0,0).direction_to(Vector(10,0))
# Vector(1,0)
```

---

# Geometry Operations

## Dot Product

```python
v1.dot(v2)
```

Used for:

* projections
* angle checks
* lighting
* AI vision

Example:

```python
Vector(1,0).dot(Vector(0,1))
# 0
```

---

## Cross Product

```python
v1.cross(v2)
```

Returns the **2D scalar cross product**.

Useful for:

* orientation tests
* left/right turn detection

Example:

```python
Vector(1,0).cross(Vector(0,1))
# 1
```

---

# Angles

## Vector Angle

```python
v.angle(radians=False)
```

Returns the vector angle from the **X axis**.

Default output is **degrees**.

Example:

```python
Vector(0,1).angle()
# 90
```

---

## Rotate Vector

```python
v.rotate(angle, radians=False)
```

Returns a rotated copy of the vector.

Example:

```python
Vector(1,0).rotate(90)
# Vector(0,1)
```

---

# Utility Methods

## Copy

```python
v.copy()
```

Returns a duplicate vector.

---

## Tuple Conversion

```python
v.to_tuple()
```

Example:

```python
Vector(1,2).to_tuple()
# (1.0, 2.0)
```

---

## Create From Tuple

```python
Vector.from_tuple((x, y))
```

Example:

```python
Vector.from_tuple((5, 10))
```

---

# Built-in Python Support

The class integrates with Python operators.

| Operation      | Description           |
|----------------|-----------------------|
| `abs(v)`       | Returns vector length |
| `v1 == v2`     | Equality comparison   |
| `for x,y in v` | Vector unpacking      |

Example:

```python
x, y = Vector(10, 20)
```

---

# Typical Engine Usage

### Position

```python
entity.position += entity.velocity * dt
```

---

### Direction

```python
direction = player.position.direction_to(enemy.position)
```

---

### Distance Check

```python
if player.position.distance_to(enemy.position) < 50:
    alert()
```
