import unittest
import math


class MathTest(unittest.TestCase):
    def test_increase(self):
        self.assertEqual(math.increase(2), 3)
    def test_decrease(self):
        self.assertEqual(math.decrease(2), 1)

unittest.main()