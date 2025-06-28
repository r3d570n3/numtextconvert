"""Tests for the num2text module."""


import unittest

from numtextconvert.num2text import num2text


class TestNum2Text(unittest.TestCase):
    """Unit tests for the num2text function."""

    def test_0_999(self):
        """Test numbers from 0 to 99."""
        # self.assertEqual(num2text(0), "zero")
        self.assertEqual(num2text(1), "one")
        self.assertEqual(num2text(9), "nine")
        self.assertEqual(num2text(10), "ten")
        self.assertEqual(num2text(11), "eleven")
        self.assertEqual(num2text(19), "nineteen")
        self.assertEqual(num2text(20), "twenty")
        self.assertEqual(num2text(21), "twenty one")
        self.assertEqual(num2text(29), "twenty nine")
        self.assertEqual(num2text(90), "ninety")
        self.assertEqual(num2text(99), "ninety nine")
        self.assertEqual(num2text(100), "one hundred")
        self.assertEqual(num2text(101), "one hundred one")
        self.assertEqual(num2text(119), "one hundred nineteen")
        self.assertEqual(num2text(120), "one hundred twenty")
        self.assertEqual(num2text(199), "one hundred ninety nine")
        self.assertEqual(num2text(200), "two hundred")
        self.assertEqual(num2text(999), "nine hundred ninety nine")

    def test_1000_and_above(self):
        """Test numbers from 1000 and above."""
        self.assertEqual(num2text(1_000), "one thousand")
        self.assertEqual(num2text(1_001), "one thousand one")
        self.assertEqual(num2text(1_010), "one thousand ten")
        self.assertEqual(num2text(1_100), "one thousand one hundred")
        self.assertEqual(num2text(1_200), "one thousand two hundred")
        self.assertEqual(num2text(1_999), "one thousand nine hundred ninety nine")
        self.assertEqual(num2text(2_000), "two thousand")
        self.assertEqual(num2text(1_000_000), "one million")
        self.assertEqual(num2text(1_000_000_000), "one billion")
        self.assertEqual(num2text(1_000_000_000_000), "one trillion")

        # Many different digits
        # pylint:disable=line-too-long
        self.assertEqual(num2text(1_234_567_890), "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety")
