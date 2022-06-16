import unittest
from MathExpTree import *


class MathTest(unittest.TestCase):

    def test_sin_func(self):
        i = MathExpTree('sin(0)+func(5)*(5-1)')
        i.convert()
        self.assertEqual(i.evaluate(func=lambda x: x * 42), 840.0)
        i.visualize(1)

    def test_add_minus(self):
        i = MathExpTree('2+1+(8-2)')
        i.convert()
        self.assertEqual(i.evaluate(), 9.0)
        i.visualize(2)

    def test_cos_pow(self):
        i = MathExpTree('cos(0)+func(5)+pow(2,2)')
        i.convert()
        self.assertEqual(i.evaluate(func=lambda x: x + 2), 12.0)
        i.visualize(3)

    def test_cos_func(self):
        i = MathExpTree('12-(cos((3-a)*b)+(func(c)+3))')
        i.convert()
        self.assertEqual(i.evaluate(a=3, b=5, c=7, func=lambda x: x / 2), 4.5)
        i.visualize(4)

    def test_func_add(self):
        i = MathExpTree('func1(1,2)+func2(3,4,5)')
        i.convert()
        def f1(x, y): return x + y
        def f2(x, y, z): return max(x, y, z)
        self.assertEqual(i.evaluate(func1=f1, func2=f2), 8.0)
        i.visualize(5)

    def test_mul(self):
        i = MathExpTree('(4+14-(2*3))/2')
        i.convert()
        self.assertEqual(i.evaluate(), 6.0)
        i.visualize(6)

    def test_pow_log(self):
        i = MathExpTree('pow(2,2)*log(9,3)')
        i.convert()
        i.visualize(7)
        self.assertEqual(i.evaluate(), 8.0)


if __name__ == '__main__':
    unittest.main()
