import pytest
import unittest

from SimpleCalc import SimpleCalc

class CalcTest(unittest.TestCase):
    #inheriting TestCase class from unittest

    calc = SimpleCalc()

    def test_add(self): # naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter recognises it as a testcase.
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)