#!/usr/bin/python3
"""
Script markdown2html.py that takes an argument 2 strings:
    first argument is the name of the markdown file
    second argument is the output file name
"""
import sys
import os


def main():
    # Check is number of argument is less than 2
    if len(sys.argv) < 3:
        print(("Usage: ./markdown2html.py"
                "README.md README.html"), file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    # Check if the markdown file doesn't exist
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # If all checks pass
    sys.exit(0)

if __name__ == "__main__":
    main()
