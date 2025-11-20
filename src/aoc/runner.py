"""Solution runner with context management."""

from __future__ import annotations

import importlib
from typing import Any

from aoc.context import set_context
from aoc.utils import get_data


def _import_solution_module(year: int, day: int):
    """Import the solution module for the given year and day."""
    module_name = f"year_{year}.day_{day:02d}"
    return importlib.import_module(module_name)


def run_solution(year: int, day: int) -> None:
    """Run a solution with proper context and print results.

    Args:
        year: Advent of Code year (e.g., 2024).
        day: Day number (1–25).
    """
    # Set context BEFORE importing
    set_context(year, day)

    module = _import_solution_module(year, day)

    if not hasattr(module, "parse"):
        raise AttributeError(
            f"Module '{module.__name__}' does not define required function 'parse'."
        )

    raw_data = get_data()
    data = module.parse(raw_data)

    def _run_part(part_name: str) -> None:
        fn = getattr(module, part_name, None)
        if fn is None:
            return
        result: Any = fn(data)
        part_number = part_name[-1]
        print(f"Part {part_number}: {result}")

    _run_part("part1")
    _run_part("part2")
