"""Module with utility functions for number to text conversion."""


def n2t_0_19(num: int) -> str:
    """Convert a number from 0 to 19 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.
    """

    if not 0 <= num < 20:
        raise ValueError("number must be between 0 and 19")

    num_words = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]

    return num_words[num]


def n2t_20_99(num: int) -> str:
    """Convert a number from 20 to 99 to its text representation.
    Args:
        num (int): The number to convert.
    Returns:
        str: The text representation of the number.
    """
    if not 20 <= num < 100:
        raise ValueError("number must be between 20 and 99")

    tens = num // 10
    units = num % 10

    tens_text = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    units_text = [
        "", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]
    text = tens_text[tens]

    if units > 0:
        text += f" {units_text[units]}"

    return text
