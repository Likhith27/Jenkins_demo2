#!/usr/bin/python3

import unittest
from Task1 import Add
from Task2 import Mul

class Calculator(unittest.TestCase):

    def test_add(self):
        x = 10
        y = 20
        sum = Add(x, y)
        self.assertEqual(sum, 30)

    def test_mult(self):
        x = 10
        y = 20
        mult = Mul(x, y)
        self.assertEqual(mult, 200)

if __name__ == '__main__':
    unittest.main()
