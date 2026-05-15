# Conway's Game of Life

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Linux](https://img.shields.io/badge/Platform-Linux-informational) ![RISC-V](https://img.shields.io/badge/RISC--V-orange)

> Terminal-based cellular automaton — 2D grid simulation, iterative state updates, character rendering. Demonstrates portable Python scripting, Linux workflows, and iterative algorithm design relevant to RISC-V / HPC mentorship.

---

## Rules — at a glance

| Cell state | Condition | Next state |
|:----------:|-----------|:----------:|
| Alive | 2 or 3 neighbors | ✅ Survives |
| Alive | < 2 or > 3 neighbors | ❌ Dies |
| Dead | exactly 3 neighbors | ✅ Born |

---

## Run

**Check Python:**

```bash
python3 --version
```

**Run directly:**

```bash
chmod +x cgol_demo.py && ./cgol_demo.py
```

**Or:**

```bash
python3 cgol_demo.py
```

---

## Install Python (if needed)

**Ubuntu / Debian:**

```bash
sudo apt update && sudo apt install python3 -y
```

**Fedora:**

```bash
sudo dnf install python3 -y
```

**Arch:**

```bash
sudo pacman -S python
```

---

## GitHub

```bash
git init
git add .
git commit -m "Added Conway Game of Life demo"
git remote add origin https://github.com/yourusername/game_of_life.git
git branch -M main && git push -u origin main
```

---

## Source Code

<details>
<summary><code>cgol_demo.py</code> — click to expand</summary>

```python
#!/usr/bin/env python3

import os
import time
import random

WIDTH       = 30
HEIGHT      = 15
DELAY       = 0.15
GENERATIONS = 200

# ── Initial board ────────────────────────────────────────
def make_grid():
    return [
        [1 if random.random() < 0.25 else 0 for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]

# ── Count alive neighbors (wrapping edges) ───────────────
def count_neighbors(grid, x, y):
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            count += grid[(y + dy) % HEIGHT][(x + dx) % WIDTH]
    return count

# ── Apply Conway's rules → next generation ───────────────
def next_generation(grid):
    new_grid = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            n = count_neighbors(grid, x, y)
            alive = grid[y][x]
            row.append(1 if (alive and n in (2, 3)) or (not alive and n == 3) else 0)
        new_grid.append(row)
    return new_grid

# ── Render to terminal ────────────────────────────────────
def render(grid, generation):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Conway's Game of Life   Generation: {generation}")
    print("=" * WIDTH)
    for row in grid:
        print("".join("█" if cell else " " for cell in row))
    print("=" * WIDTH)
    print("Alive = █   Dead = space")

# ── Entry point ───────────────────────────────────────────
def main():
    grid = make_grid()
    for gen in range(GENERATIONS):
        render(grid, gen)
        time.sleep(DELAY)
        grid = next_generation(grid)

if __name__ == "__main__":
    main()
```

</details>

---

## Relevance — RISC-V / HPC Mentorship

| Concept | How this project applies |
|---------|--------------------------|
| Portable scripting | Runs unmodified on any Linux target, including RISC-V boards |
| Iterative algorithms | Nested-loop grid update mirrors patterns in physics / HPC simulations |
| Terminal I/O | Character rendering without dependencies — useful for headless embedded targets |
| Open-source workflow | Git-based project structure, documented and reproducible |

---

## File Structure

```
game_of_life/
├── cgol_demo.py
└── README.md
```
---
