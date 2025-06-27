"""Tests for the num2text module."""


import unittest

from numtextconvert.num2text import num2text


class TestNum2Text(unittest.TestCase):
    """Unit tests for the num2text function."""

    def test_0_99(self):
        """Test numbers from 0 to 99."""
        self.assertEqual(num2text(0), "zero")
        self.assertEqual(num2text(1), "one")
        self.assertEqual(num2text(9), "nine")
        self.assertEqual(num2text(10), "ten")
        self.assertEqual(num2text(11), "eleven")
        self.assertEqual(num2text(19), "nineteen")
        self.assertEqual(num2text(20), "twenty")
        self.assertEqual(num2text(21), "twenty one")
        self.assertEqual(num2text(29), "twenty nine")
        self.assertEqual(num2text(30), "thirty")
        self.assertEqual(num2text(40), "forty")
        self.assertEqual(num2text(50), "fifty")
        self.assertEqual(num2text(60), "sixty")
        self.assertEqual(num2text(70), "seventy")
        self.assertEqual(num2text(80), "eighty")
        self.assertEqual(num2text(90), "ninety")
        self.assertEqual(num2text(99), "ninety nine")
