"""Todo List Application - CLI Entry Point."""
import argparse
import sys


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="todo_list",
        description="Todo List Application - Task Management System",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    return parser


def main() -> int:
    """Main entry point for the application."""
    parser = create_parser()
    parser.parse_args()
    return 0


if __name__ == "__main__":
    sys.exit(main())
