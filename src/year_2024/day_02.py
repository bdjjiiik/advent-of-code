"""Year 2024, Day 2"""

from __future__ import annotations

from typing import TypeAlias

from aoc.utils import parse_lines

Report: TypeAlias = list[int]


def parse(text: str) -> list[Report]:
    """Parse input data."""
    reports = [
        list(map(int, line.split()))
        for line in parse_lines(text)
    ]

    return reports


def _diffs(report: Report) -> list[int]:
    """Adjacent differences for a report"""
    return [b - a for a, b in zip(report, report[1:])]


def _has_valid_steps(diffs: list[int]) -> bool:
    """All steps are non-zero and have magnitude between 1 and 3."""
    return all(1 <= abs(diff) <= 3 for diff in diffs)


def _is_monotonic(diffs: list[int]) -> bool:
    """All diffs strictly positive (increasing) or strictly negative (decreasing)."""
    return all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)


def is_safe(report: Report) -> bool:
    diffs = _diffs(report)
    return _has_valid_steps(diffs) and _is_monotonic(diffs)


def is_safe_with_dampener(report: Report) -> bool:
    return any(
        is_safe(report[:i] + report[i + 1:])
        for i in range(len(report) + 1)
    )


def part1(data: list[Report]) -> int:
    """Solve part 1."""
    return sum(1 for report in data if is_safe(report))


def part2(data: list[Report]) -> int:
    """Solve part 2."""
    return sum(1 for report in data if is_safe_with_dampener(report))
