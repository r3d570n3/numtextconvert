"""Module to convert numbers to text representation."""


from numtextconvert.utils import zero_nineteen_to_text


def num2text(num: int) -> str:
    """Convert a number to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.
    """
    text: str = ''
    # First, let's start with numbers from 0 to 9
    if num < 0:
        text += 'minus '
        num = -num

    if num < 20:
        text += zero_nineteen_to_text(num)

    return text
