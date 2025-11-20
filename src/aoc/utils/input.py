"""Input handling utilities."""

from __future__ import annotations

from typing import Callable, TypeVar, overload

from aoc.context import get_year, get_day
from aoc.paths import input_file

T = TypeVar("T")


def get_data() -> str:
    """Return raw input data for the current (year, day) context."""
    year = get_year()
    day = get_day()
    path = input_file(year, day)

    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        # Re-wrap with a clearer message, but keep the original traceback.
        raise FileNotFoundError(f"Input file not found: {path}") from exc


@overload
def parse_lines(
        text: str,
        transform: None = ...,
        skip_empty: bool = ...,
) -> list[str]:
    ...


@overload
def parse_lines(
        text: str,
        transform: Callable[[str], T],
        skip_empty: bool = ...,
) -> list[T]:
    ...


def parse_lines(
        text: str,
        transform: Callable[[str], T] | None = None,
        skip_empty: bool = True,
) -> list[str] | list[T]:
    """Split input into lines, with optional transformation.

    Args:
        text: Raw input text.
        transform: Optional function applied to each line (e.g., int).
        skip_empty: If True, drop empty / whitespace-only lines.

    Returns:
        A list of lines (str) or transformed values.
    """
    lines = text.splitlines()

    if skip_empty:
        lines = [line for line in lines if line.strip()]

    if transform is not None:
        return [transform(line) for line in lines]

    return lines


def parse_grid(text: str) -> list[list[str]]:
    """Parse input into a 2D grid of characters."""
    return [list(line) for line in parse_lines(text)]
