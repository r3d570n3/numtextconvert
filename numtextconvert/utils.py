"""Module with utility functions for number to text conversion."""


WORDS_UNITS = (
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "zero"
)

WORDS_TEENS = (
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
)

WORDS_TENS = (
    "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
)


def n2t_1_19(num: int) -> str:
    """
    Convert a number from 1 to 19 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.

    Raises:
        ValueError: If the number is not in the range of 1 to 19.
    """
    if not 0 < num < 20:
        raise ValueError("number must be in the range of 1 to 19")

    if num < 10:
        return WORDS_UNITS[num - 1]
    if num == 10:
        return "ten"
    return WORDS_TEENS[num - 11]


def n2t_20_99(num: int) -> str:
    """
    Convert a number from 20 to 99 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.

    Raises:
        ValueError: If the number is not in the range of 20 to 99.
    """
    if not 20 <= num < 100:
        raise ValueError("number must be in the range of 20 to 99")

    tens = num // 10
    units = num % 10

    if units == 0:
        return WORDS_TENS[tens - 2]
    return f"{WORDS_TENS[tens - 2]} {WORDS_UNITS[units - 1]}"


def n2t_100_999(num: int) -> str:
    """
    Convert a number from 100 to 999 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.

    Raises:
        ValueError: If the number is not in the range of 100 to 999.
    """
    if not 100 <= num < 1000:
        raise ValueError("number must be in the range of 100 to 999")

    hundreds = num // 100
    remainder = num % 100

    text = f"{WORDS_UNITS[hundreds - 1]} hundred"

    if remainder == 0:
        return text
    if remainder < 20:
        return f"{text} {n2t_1_19(remainder)}"
    return f"{text} {n2t_20_99(remainder)}"
