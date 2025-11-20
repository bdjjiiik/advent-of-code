"""Year 2025, Day 1"""

from __future__ import annotations

from collections import Counter
from typing import TypeAlias

from aoc.utils import parse_lines

Columns: TypeAlias = tuple[list[int], list[int]]


def parse_two_lists(text: str) -> Columns:
    """Parse input into two integer lists: left and right columns."""
    pairs = [
        tuple(map(int, line.split()))
        for line in parse_lines(text)
    ]

    left_part, right_part = zip(*pairs)
    left = list(left_part)
    right = list(right_part)
    return left, right


def parse(data: str) -> Columns:
    return parse_two_lists(data)


def part1(data: Columns) -> int:
    """Solve part 1."""
    left, right = data

    left_sorted = sorted(left)
    right_sorted = sorted(right)

    differences = (abs(a - b) for a, b in zip(left_sorted, right_sorted))
    return sum(differences)


def part2(data: Columns) -> int:
    """Solve part 2."""
    left, right = data
    counts = Counter(right)

    return sum(value * counts[value] for value in left)
