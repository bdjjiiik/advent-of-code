"""Context management for Advent of Code solutions."""

from __future__ import annotations

from contextvars import ContextVar
from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class SolutionContext:
    """Represents the currently active solution (year + day)."""

    year: int
    day: int


_context: Final[ContextVar[SolutionContext]] = ContextVar("solution_context")


class ContextNotSetError(RuntimeError):
    """Raised when the solution context is accessed before being set."""


def set_context(year: int, day: int) -> None:
    """Set the current solution context."""
    _context.set(SolutionContext(year=year, day=day))


def get_context() -> SolutionContext:
    """Return the current solution context.

    Raises:
        ContextNotSetError: if no context has been set.
    """
    try:
        return _context.get()
    except LookupError as exc:
        raise ContextNotSetError(
            "No solution context set. Call set_context first."
        ) from exc


def get_year() -> int:
    """Get the current year from context."""
    return get_context().year


def get_day() -> int:
    """Get the current day from context."""
    return get_context().day
