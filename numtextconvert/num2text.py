"""Module to convert numbers to text representation."""


from numtextconvert.utils import n2t_1_19, n2t_20_99, n2t_100_999


def num2text(num: int) -> str:
    """Convert a number to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.
    """
    text: str = ""

    if num == 0:
        return "zero"

    # if num < 0:
    #     text += 'minus '
    #     num = -num

    # Last 3 digits
    if num < 20:
        text += n2t_1_19(num)
    elif num < 100:
        text += n2t_20_99(num)
    else:
        text += n2t_100_999(num)

    return text
