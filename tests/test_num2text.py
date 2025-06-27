"""Tests for the num2text module."""


import unittest

from numtextconvert.num2text import num2text


class TestNum2Text(unittest.TestCase):
    """Unit tests for the num2text function."""

    def test_zero_nineteen(self):
        """Test numbers from 0 to 19."""
        self.assertEqual(num2text(0), "zero")
        self.assertEqual(num2text(1), "one")
        self.assertEqual(num2text(9), "nine")
        self.assertEqual(num2text(10), "ten")
        self.assertEqual(num2text(11), "eleven")
        self.assertEqual(num2text(19), "nineteen")
