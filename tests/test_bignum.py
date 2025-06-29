"""Tests for the bignum module."""


import unittest

from numtextconvert.bignum import n2t_1000_power


class TestBignum(unittest.TestCase):
    """Test cases for the bignum module."""

    def test_n2t_1000_power(self):
        """Test the n2t_1000_power function."""
        self.assertEqual(n2t_1000_power(1), "thousand")
        self.assertEqual(n2t_1000_power(10), "nonillion")
        self.assertEqual(n2t_1000_power(11), "decillion")
        self.assertEqual(n2t_1000_power(12), "undecillion")
        self.assertEqual(n2t_1000_power(20), "novedecillion")
        self.assertEqual(n2t_1000_power(21), "vigintillion")
        self.assertEqual(n2t_1000_power(100), "novenonagintillion")
        self.assertEqual(n2t_1000_power(101), "centillion")
        self.assertEqual(n2t_1000_power(200), "novenonaginticentillion")
        self.assertEqual(n2t_1000_power(201), "ducentillion")
        self.assertEqual(n2t_1000_power(1_000), "novenonagintinongentillion")

        self.assertRaises(ValueError, n2t_1000_power, 0)
        self.assertRaises(ValueError, n2t_1000_power, 1_001)
