#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([2, 3.4]), 3.4)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer(["hello", "camilo"]), "hello")
        self.assertRaises(TypeError, max_integer, [1, "hello"])
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':

    unittest.main()
