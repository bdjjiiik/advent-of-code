"""Year 2025, Day 1"""

from __future__ import annotations

from typing import List, Tuple, Literal, cast

from pyparsing import (
    Char,
    ParseResults,
    ParserElement,
)

from pyparsing import pyparsing_common as ppc

START_POINT = 50

Direction = Literal["L", "R"]
Instruction = Tuple[Direction, int]

combination: ParserElement = Char("LR") + ppc.integer


def parse(text: str) -> List[Instruction]:
    result: List[Instruction] = []

    for line in text.strip().splitlines():
        if not line:
            continue

        tokens: ParseResults = combination.parse_string(line)
        raw_direction, raw_steps = tokens

        direction: Direction = cast(Direction, raw_direction)
        steps: int = cast(int, raw_steps)

        result.append((direction, steps))

    return result


def part1(data: List[Instruction]) -> int:
    """Solve part 1."""

    position = START_POINT

    count = 0
    for (direction, steps) in data:
        sign = 1 if direction == "R" else -1
        position = (position + sign * steps) % 100

        if position == 0:
            count += 1

    return count


def part2(data: List[Instruction]) -> int:
    """Solve part 2."""
    position = START_POINT

    count = 0
    for (direction, steps) in data:
        start_pos = position

        if direction == "R":
            rotation, position = divmod(position + steps, 100)
        else:
            position = (position - steps) % 100
            offset = 0 if start_pos == 0 else 100 - start_pos
            rotation = (steps + offset) // 100

        count += rotation

    return count
