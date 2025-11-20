# src/aoc/cli.py
"""CLI for running Advent of Code solutions."""

from __future__ import annotations

import click

from aoc.template import get_template
from aoc.runner import run_solution
from aoc.paths import year_dir, solution_file, input_file


@click.group()
def main() -> None:
    """Advent of Code solution runner."""
    ...


@main.command()
@click.option("-y", "--year", type=int, required=True, help="Year (e.g., 2024)")
@click.option(
    "-d",
    "--day",
    type=click.IntRange(1, 25),
    required=True,
    help="Day (1–25)",
)
def create(year: int, day: int) -> None:
    """Create template files for a new day."""
    # Ensure year package directory exists
    ydir = year_dir(year)
    ydir.mkdir(parents=True, exist_ok=True)

    # Ensure package __init__.py
    init_file = ydir / "__init__.py"
    if not init_file.exists():
        init_file.write_text(
            f'"""Advent of Code {year} solutions."""\n',
            encoding="utf-8",
        )

    # Create solution file
    sol_file = solution_file(year, day)
    if sol_file.exists():
        click.echo(f"Solution file already exists: {sol_file}", err=True)
        return

    sol_file.write_text(get_template(year, day), encoding="utf-8")
    click.echo(f"✓ Created: {sol_file}")

    # Create input file (uses SAME config as get_data)
    inp_path = input_file(year, day)
    inp_path.parent.mkdir(parents=True, exist_ok=True)

    if not inp_path.exists():
        inp_path.touch()
        click.echo(f"✓ Created: {inp_path}")

    click.echo("\nNext steps:")
    click.echo(f"  1. Add your puzzle input to: {inp_path}")
    click.echo(f"  2. Run with: aoc run -y {year} -d {day}")


@main.command()
@click.option("-y", "--year", type=int, required=True, help="Year (e.g., 2024)")
@click.option(
    "-d",
    "--day",
    type=click.IntRange(1, 25),
    required=True,
    help="Day (1–25)",
)
def run(year: int, day: int) -> None:
    """Run solution for a specific year and day."""
    click.echo(f"Year {year}, Day {day:02d}")
    click.echo("-" * 50)

    try:
        run_solution(year, day)
    except ModuleNotFoundError:
        click.echo(f"Solution not found for year {year}, day {day:02d}", err=True)
        click.echo(f"Create it with: aoc create -y {year} -d {day}", err=True)
    except FileNotFoundError as exception:
        click.echo(f"{exception}", err=True)
    except Exception as exception:  # noqa: BLE001 - top-level CLI handler
        click.echo(f"Error: {exception}", err=True)


if __name__ == "__main__":
    main()
