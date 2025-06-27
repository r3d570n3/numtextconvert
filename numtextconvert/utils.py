"""Module with utility functions for number to text conversion."""


# Let's do zero to nineteen as well
def zero_nineteen_to_text(num: int) -> str:
    """Convert a number from 0 to 19 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.
    """
    if not 0 <= num < 20:
        raise ValueError("number must be between 0 and 19")

    numbers = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]

    return numbers[num]
