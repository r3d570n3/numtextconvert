"""Tests for the utils module."""


import unittest

from numtextconvert import utils


class TestUtils(unittest.TestCase):
    """Unit tests for the utility functions."""

    def test_n2t_1_19(self):
        """Test numbers from 1 to 19."""
        self.assertEqual(utils.n2t_1_19(1), "one")
        self.assertEqual(utils.n2t_1_19(9), "nine")
        self.assertEqual(utils.n2t_1_19(10), "ten")
        self.assertEqual(utils.n2t_1_19(11), "eleven")
        self.assertEqual(utils.n2t_1_19(19), "nineteen")

    def test_n2t_20_99(self):
        """Test numbers from 20 to 99."""
        self.assertEqual(utils.n2t_20_99(20), "twenty")
        self.assertEqual(utils.n2t_20_99(21), "twenty one")
        self.assertEqual(utils.n2t_20_99(29), "twenty nine")
        self.assertEqual(utils.n2t_20_99(90), "ninety")
        self.assertEqual(utils.n2t_20_99(99), "ninety nine")

    def test_n2t_100_999(self):
        """Test numbers from 100 to 999."""
        self.assertEqual(utils.n2t_100_999(100), "one hundred")
        self.assertEqual(utils.n2t_100_999(101), "one hundred one")
        self.assertEqual(utils.n2t_100_999(119), "one hundred nineteen")
        self.assertEqual(utils.n2t_100_999(120), "one hundred twenty")
        self.assertEqual(utils.n2t_100_999(199), "one hundred ninety nine")
        self.assertEqual(utils.n2t_100_999(200), "two hundred")
        self.assertEqual(utils.n2t_100_999(999), "nine hundred ninety nine")
