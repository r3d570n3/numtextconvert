"""Module for converting large numbers to their text representation."""


WORDS_SMALL = (
    "thousand", "million", "billion", "trillion", "quadrillion",
    "quintillion", "sextillion", "septillion", "octillion", "nonillion"
)

PREFIXES_UNITS = (
    "un", "duo", "tre", "quattuor", "quin",
    "se", "septe", "octo", "nove"
)

PREFIXES_TENS = (
    "deci", "viginti", "triginti", "quadraginti", "quinquaginti",
    "sexaginti", "septuaginti", "octoginti", "nonaginti"
)

PREFIXES_HUNDREDS = (
    "centi", "ducenti", "trecenti", "quadringenti", "quingenti",
    "sescenti", "septingenti", "octingenti", "nongenti"
)


def n2t_1000_power(power: int) -> str:
    """
    Convert a power of 1000 to its text representation.

    Args:
        power (int): The power of 1000.

    Returns:
        str: The text representation of the power of 1000.

    Raises:
        ValueError: If the power is not positive.
    """
    if power < 1:
        raise ValueError("power must be positive")
    if power > 1000:  # Limiting to 3 digits for simplicity
        raise ValueError("power must be less than 1000")

    # Iterative approach to convert power to a list of digits
    # indeces: list[int] = []
    # power_: int = power
    # while power_ > 0:
    #     indeces.append(power_ % 10)
    #     power_ //= 10
    # indeces.reverse()

    # For small powers (1 to 10), return directly
    if power <= 10:
        return WORDS_SMALL[power - 1]

    # Adjust to short scale (1 = million, 2 = billion, etc.)
    power -= 1

    # Convert power to indices
    digit_units = power % 10
    digit_tens = (power // 10) % 10
    digit_hundreds = (power // 100) % 10

    prefix: str = ""

    if digit_units > 0:
        prefix += PREFIXES_UNITS[digit_units - 1]
    if digit_tens > 0:
        prefix += PREFIXES_TENS[digit_tens - 1]
    if digit_hundreds > 0:
        prefix += PREFIXES_HUNDREDS[digit_hundreds - 1]

    return f"{prefix}llion"
