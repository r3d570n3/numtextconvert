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

        with self.assertRaises(ValueError):
            utils.n2t_1_19(0)
        with self.assertRaises(ValueError):
            utils.n2t_1_19(20)

    def test_n2t_20_99(self):
        """Test numbers from 20 to 99."""
        self.assertEqual(utils.n2t_20_99(20), "twenty")
        self.assertEqual(utils.n2t_20_99(21), "twenty one")
        self.assertEqual(utils.n2t_20_99(29), "twenty nine")
        self.assertEqual(utils.n2t_20_99(90), "ninety")
        self.assertEqual(utils.n2t_20_99(99), "ninety nine")

        with self.assertRaises(ValueError):
            utils.n2t_20_99(19)
        with self.assertRaises(ValueError):
            utils.n2t_20_99(100)

    def test_n2t_100_999(self):
        """Test numbers from 100 to 999."""
        self.assertEqual(utils.n2t_100_999(100), "one hundred")
        self.assertEqual(utils.n2t_100_999(101), "one hundred one")
        self.assertEqual(utils.n2t_100_999(119), "one hundred nineteen")
        self.assertEqual(utils.n2t_100_999(120), "one hundred twenty")
        self.assertEqual(utils.n2t_100_999(199), "one hundred ninety nine")
        self.assertEqual(utils.n2t_100_999(200), "two hundred")
        self.assertEqual(utils.n2t_100_999(999), "nine hundred ninety nine")

        with self.assertRaises(ValueError):
            utils.n2t_100_999(99)
        with self.assertRaises(ValueError):
            utils.n2t_100_999(1000)

    def test_n2t_1_999(self):
        """Test numbers from 1 to 999."""
        self.assertEqual(utils.n2t_1_999(1), "one")
        self.assertEqual(utils.n2t_1_999(9), "nine")
        self.assertEqual(utils.n2t_1_999(10), "ten")
        self.assertEqual(utils.n2t_1_999(11), "eleven")
        self.assertEqual(utils.n2t_1_999(19), "nineteen")
        self.assertEqual(utils.n2t_1_999(20), "twenty")
        self.assertEqual(utils.n2t_1_999(21), "twenty one")
        self.assertEqual(utils.n2t_1_999(29), "twenty nine")
        self.assertEqual(utils.n2t_1_999(90), "ninety")
        self.assertEqual(utils.n2t_1_999(99), "ninety nine")
        self.assertEqual(utils.n2t_1_999(100), "one hundred")
        self.assertEqual(utils.n2t_1_999(101), "one hundred one")
        self.assertEqual(utils.n2t_1_999(119), "one hundred nineteen")
        self.assertEqual(utils.n2t_1_999(120), "one hundred twenty")
        self.assertEqual(utils.n2t_1_999(199), "one hundred ninety nine")
        self.assertEqual(utils.n2t_1_999(200), "two hundred")
        self.assertEqual(utils.n2t_1_999(999), "nine hundred ninety nine")

        with self.assertRaises(ValueError):
            utils.n2t_1_999(0)
        with self.assertRaises(ValueError):
            utils.n2t_1_999(1000)

    def test_split_digits(self):
        """Test splitting digits."""
        self.assertEqual(utils.split_digits(1), ['1'])
        self.assertEqual(utils.split_digits(12), ['12'])
        self.assertEqual(utils.split_digits(123), ['123'])
        self.assertEqual(utils.split_digits(1234), ['1', '234'])
        self.assertEqual(utils.split_digits(123456789), ['123', '456', '789'])

        with self.assertRaises(ValueError):
            utils.split_digits(0)

    def test_power_of_1000_text(self):
        """Test power of 1000 text representation."""
        self.assertEqual(utils.power_of_1000_text(1), "thousand")
        self.assertEqual(utils.power_of_1000_text(2), "million")
        self.assertEqual(utils.power_of_1000_text(3), "billion")
        self.assertEqual(utils.power_of_1000_text(4), "trillion")
        self.assertEqual(utils.power_of_1000_text(5), "quadrillion")
        self.assertEqual(utils.power_of_1000_text(6), "quintillion")
        self.assertEqual(utils.power_of_1000_text(7), "sextillion")
        self.assertEqual(utils.power_of_1000_text(8), "septillion")
        self.assertEqual(utils.power_of_1000_text(9), "octillion")
        self.assertEqual(utils.power_of_1000_text(10), "nonillion")
        self.assertEqual(utils.power_of_1000_text(11), "decillion")
