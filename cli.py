import argparse
import sys

from fib_generator import generate_fibonacci


def main():
    parser = argparse.ArgumentParser(
        description="Generate Fibonacci numbers up to a specified limit."
    )
    parser.add_argument(
        "--limit",
        type=int,
        required=True,
        help="Upper bound for Fibonacci numbers (inclusive)"
    )
    
    args = parser.parse_args()
    
    try:
        result = generate_fibonacci(args.limit)
        print(" ".join(map(str, result)))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
