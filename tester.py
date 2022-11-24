#!/usr/bin/python3

import unittest
from Task1 import Add
from Task2 import Mul

class Calculator(unittest.TestCase):

    def test_add(self):
        x = 10
        y = 30
        sum = Add(x, y)
        self.assertEqual(sum, 5055)

    def test_mult(self):
        x = 10
        y = 20
        mult = Mul(x, y)
        self.assertEqual(mult, 2008545)

if __name__ == '__main__':
    unittest.main()
