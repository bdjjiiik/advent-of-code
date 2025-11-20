"""Year 2024, Day 3"""

from __future__ import annotations

from typing import Final, Iterable, Tuple

from pyparsing import (
    Empty,
    Literal,
    ParseResults,
    ParserElement,
    Suppress,
)
from pyparsing import pyparsing_common as ppc

FUNC_MUL: Final[str] = "mul"
FUNC_DO: Final[str] = "do"
FUNC_DONT: Final[str] = "don't"

ParserElement.enablePackrat()

left_parenthesis, right_parenthesis, comma = map(Suppress, "(),")
integer = ppc.integer


def func_call(name: str, body: ParserElement) -> ParserElement:
    """
    Generic function-call pattern
    with 'kind' result name set to the function name.
    """
    return (
            Literal(name)("kind")
            + left_parenthesis
            + body
            + right_parenthesis
    )


# mul(a, b)
mul_call: ParserElement = func_call(
    FUNC_MUL,
    integer("a") + comma + integer("b"),
)

# do()
do_call: ParserElement = func_call(FUNC_DO, Empty())

# don't()
dont_call: ParserElement = func_call(FUNC_DONT, Empty())

any_func: ParserElement = dont_call | do_call | mul_call

Call = ParseResults


def parse(text: str) -> ParseResults:
    """
    Parse input data and return all function-like tokens (mul/do/don't)
    in the order they appear.
    """
    return any_func.searchString(text)


def _mul_products(calls: Iterable[Call]) -> Iterable[int]:
    """Yield a * b for every mul(a, b) instruction."""
    return (
        call.a * call.b
        for call in calls
        if call.kind == FUNC_MUL
    )


def _conditional_mul_products(calls: Iterable[Call]) -> Iterable[int]:
    """
    Yield a * b for mul(a, b) calls that are currently enabled by
    do()/don't() toggling.
    """
    enabled = True

    def mark(call: Call) -> Tuple[bool, Call]:
        nonlocal enabled

        kind = call.kind
        if kind == FUNC_DO:
            enabled = True
        elif kind == FUNC_DONT:
            enabled = False

        return enabled, call

    return (
        call.a * call.b
        for enabled, call in map(mark, calls)
        if enabled and call.kind == FUNC_MUL
    )


def part1(data: ParseResults) -> int:
    """Solve part 1."""
    return sum(_mul_products(data))


def part2(data: ParseResults) -> int:
    """Solve part 2."""
    return sum(_conditional_mul_products(data))
