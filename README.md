# Shooting-game

A simple Space Shooter game built with Python and Pygame.

## Overview

This project contains a basic arcade-style shooting game where the player controls a spaceship, fires bullets at incoming enemies, and earns points for each enemy destroyed.

## Requirements

- Python 3.10+ (or compatible)
- Pygame

## Installation

1. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install pygame
```

## Run the game

```bash
python main.py
```

## Controls

- Left arrow / A: move left
- Right arrow / D: move right
- Space: shoot

## Notes

- The game uses a single `main.py` entry point.
- Score increases when enemies are destroyed.
- The game resets enemies after they leave the bottom of the screen.
