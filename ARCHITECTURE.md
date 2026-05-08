# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- `fib_generator.py`: Core Fibonacci generation logic with a function `generate_fibonacci(limit: int) -> list[int]`
- `cli.py`: Command-line interface that parses arguments and displays results
- `tests/test_fib.py`: Unit tests for the Fibonacci generator

## Interfaces

- `fib_generator.py` exposes:
  - `generate_fibonacci(limit: int) -> list[int]`: Returns all Fibonacci numbers up to and including the limit
  - Raises `ValueError` if limit is negative

- `cli.py` depends on `fib_generator`:
  - Parses `--limit` argument (integer)
  - Calls `generate_fibonacci(limit)` and prints results

## Shared Data Structures

- Returns a list of integers representing Fibonacci sequence
- Empty list returned for limit < 1

## External Dependencies

- Standard library only (no external packages required)
