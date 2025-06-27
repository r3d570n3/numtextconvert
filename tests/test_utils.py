"""Tests for the utils module."""


import unittest

from numtextconvert import utils


class TestUtils(unittest.TestCase):
    """Unit tests for the utility functions."""

    def test_n2t_0_19(self):
        """Test numbers from 0 to 19."""
        self.assertEqual(utils.n2t_0_19(0), "zero")
        self.assertEqual(utils.n2t_0_19(1), "one")
        self.assertEqual(utils.n2t_0_19(9), "nine")
        self.assertEqual(utils.n2t_0_19(10), "ten")
        self.assertEqual(utils.n2t_0_19(11), "eleven")
        self.assertEqual(utils.n2t_0_19(19), "nineteen")

    def test_n2t_20_99(self):
        """Test numbers from 20 to 99."""
        self.assertEqual(utils.n2t_20_99(20), "twenty")
        self.assertEqual(utils.n2t_20_99(21), "twenty one")
        self.assertEqual(utils.n2t_20_99(29), "twenty nine")
        self.assertEqual(utils.n2t_20_99(30), "thirty")
        self.assertEqual(utils.n2t_20_99(40), "forty")
        self.assertEqual(utils.n2t_20_99(50), "fifty")
        self.assertEqual(utils.n2t_20_99(60), "sixty")
        self.assertEqual(utils.n2t_20_99(70), "seventy")
        self.assertEqual(utils.n2t_20_99(80), "eighty")
        self.assertEqual(utils.n2t_20_99(90), "ninety")
        self.assertEqual(utils.n2t_20_99(99), "ninety nine")
