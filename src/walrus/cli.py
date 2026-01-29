"""Command-line interface for walrus."""

import argparse
import sys

from walrus import __version__
from walrus.api import get_capital, hello


def main(args=None):
    """Main entry point for the walrus CLI."""
    parser = argparse.ArgumentParser(
        prog="walrus",
        description="Look up country capitals and more.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # hello command
    hello_parser = subparsers.add_parser("hello", help="Say hello")
    hello_parser.add_argument(
        "-l",
        "--language",
        type=str,
        default=None,
        help="Language code for greeting (requires plugin)",
    )

    # capital command
    capital_parser = subparsers.add_parser(
        "capital", help="Look up the capital of a country"
    )
    capital_parser.add_argument(
        "countries",
        nargs="+",
        help="One or more country names to look up",
    )

    parsed_args = parser.parse_args(args)

    if parsed_args.command is None:
        parser.print_help()
        return 0

    if parsed_args.command == "hello":
        try:
            result = hello(language=parsed_args.language)
            print(result)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    elif parsed_args.command == "capital":
        countries = parsed_args.countries
        if len(countries) == 1:
            result = get_capital(countries[0])
            if result is None:
                print(f"Capital not found for: {countries[0]}", file=sys.stderr)
                return 1
            print(result)
        else:
            results = get_capital(countries)
            for country, capital in results.items():
                if capital is None:
                    print(f"{country}: Not found")
                else:
                    print(f"{country}: {capital}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
