"""Module with utility functions for number to text conversion."""


def n2t_0_19(num: int) -> str:
    """
    Convert a number from 0 to 19 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.

    Raises:
        ValueError: If the number is not between 0 and 19.
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
    """
    Convert a number from 20 to 99 to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.

    Raises:
        ValueError: If the number is not between 20 and 99.
    """
    if not 20 <= num < 100:
        raise ValueError("number must be between 20 and 99")

    tens_words = [
        '', '', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    units_words = [
        '', ' one', ' two', ' three', ' four',
        ' five', ' six', ' seven', ' eight', ' nine'
    ]

    tens = num // 10
    units = num % 10
    text = tens_words[tens] + units_words[units]

    return text
