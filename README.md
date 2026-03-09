# BSCP: Foundation Architect

**Build. Secure. Contain. Protect.**

BSCP: Foundation Architect is a **2D/2.5D SCP facility map creator and simulation tool** built in **Python with pygame**.  
It allows you to design containment facilities, place tiles, NPCs, and SCP entities, and simulate basic behaviors within your custom facility maps.

---

## Features (Planned)

- **Map Editor:** Create and edit SCP Foundation sites with tiles and structures.
- **NPCs:** Add and manage different personnel:
  - ScD, MD, SD, CD, MTF, RRT, IA, O5, ISD, SiD
- **SCP Entities:** Place and configure SCPs with individual behaviors.
- **Simulation:** Test AI movement, patrols, and containment interactions.
- **Modular Architecture:** All sprites, windows, maps, and entities are implemented in separate classes for clarity and scalability.
- **2D Pixel Art Style:** With optional 2.5D isometric view for more depth.

---

## Project Structure

```

scp-map-creator/
├── main.py
├── config/
├── core/
├── engine/
├── map/
├── entities/
├── ai/
├── systems/
├── ui/
├── utils/
├── assets/
└── tests/

````

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BSCP-Foundation-Architect.git
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

---

## Contributing

This is a **long-term side project**. Contributions, suggestions, and bug reports are welcome.
Please follow **modular and clean code practices**, and respect the **BSCP coding conventions**.

---

## License

[GNU License](LICENSE) – free to use, modify, and distribute.
