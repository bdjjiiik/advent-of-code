"""Template management for solutions."""


def get_template(year: int, day: int) -> str:
    """Generate solution template."""
    return f'''"""Year {year}, Day {day}"""

from typing import Any


def parse(data: str) -> Any:
    """Parse input data."""
    lines = data.strip().split("\\n")
    # TODO: Implement parsing
    return lines


def part1(data: Any) -> int:
    """Solve part 1."""
    # TODO: Implement solution
    return 0


def part2(data: Any) -> int:
    """Solve part 2."""
    # TODO: Implement solution
    return 0
'''