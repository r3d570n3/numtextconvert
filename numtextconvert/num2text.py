"""Module to convert numbers to text representation."""


from numtextconvert.utils import n2t_1_999, split_digits
from numtextconvert.bignum import n2t_1000_power


def num2text(num: int) -> str:
    """Convert a number to its text representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: The text representation of the number.
    """
    if num == 0:
        return "zero"

    chunks = split_digits(num)
    chunks.reverse() # Process from the least significant digit

    # Process 3 rightmost digits first
    text = ""
    if chunks[0] != "000":
        text = n2t_1_999(int(chunks[0]))
    chunks.pop(0)  # Remove the first chunk

    for i, chunk in enumerate(chunks):
        if chunk == "000":
            continue
        text = f"{n2t_1_999(int(chunk))} {n2t_1000_power(i + 1)} {text}".strip()

    return text
