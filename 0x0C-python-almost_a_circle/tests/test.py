#!/usr/local/bin/python3
"""Task 2 """
import unittest
from models.base import Base
from models.rectangle import Rectangle
import StringIO
import sys


class Testrectangle(unittest.TestCase):
    """ """

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        #self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        #self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_display(self):
        """ Task 5 """
        r1 = Rectangle(20, 5)
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        sys.stdout = sys.__stdout__
        self.assertEqual(r1.display(), capturedOutput.getvalue())

    if __name__ == "_main_":
        unittest.main()
