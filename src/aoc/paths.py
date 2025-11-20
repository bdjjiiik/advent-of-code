"""Path configuration and helpers for Advent of Code project."""

from __future__ import annotations

from pathlib import Path

# Root of the source tree (where `aoc`, `year_2024`, `year_2024`, ... live)
SRC_ROOT = Path("src")

# Name of the directory inside each year package where input data lives.
INPUT_DIR_NAME = "data"


def year_dir(year: int) -> Path:
    """Directory for a given year package, e.g. src/year_2024."""
    return SRC_ROOT / f"year_{year}"


def solution_file(year: int, day: int) -> Path:
    """Python source file for a given year/day."""
    return year_dir(year) / f"day_{day:02d}.py"


def input_file(year: int, day: int, *, test: bool = False) -> Path:
    """Input file path for a given year/day."""
    filename = f"day{day:02d}.txt"
    return year_dir(year) / INPUT_DIR_NAME / filename
