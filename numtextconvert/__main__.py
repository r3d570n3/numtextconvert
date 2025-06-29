"""Main entry point for the numtextconvert package."""


import sys

from numtextconvert.num2text import num2text


def main():
    """Main function to convert numbers from command line arguments to text."""
    if len(sys.argv) < 2:
        print("Usage: python -m numtextconvert <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        text_representation = num2text(number)
        print(text_representation)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
