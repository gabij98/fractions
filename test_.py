from unittest import TestCase

from fraction import Fraction

class TestFraction(TestCase):

    def test_str(self):
        val = Fraction(1, 2)
        self.assertEqual('1/2', str(val))

    def test_sanitization(self):
        val = Fraction(3, -6)
        self.assertEqual(Fraction(-1, 2).__dict__, val.__dict__)

    def test_add(self):
        a = Fraction(1, 3)
        b = Fraction(3, 4)
        self.assertEqual(Fraction(13, 12), a + b)

    def test_sub(self):
        a = Fraction(1, 3)
        b = Fraction(1, 4)
        self.assertEqual(Fraction(1, 12), a - b)

    def test_mul(self):
        a = Fraction(1, 3)
        b = Fraction(3, 5)
        self.assertEqual(Fraction(1, 5), a * b)

    def test_div(self):
        a = Fraction(1, 3)
        b = Fraction(3, 4)
        self.assertEqual(Fraction(4, 9), a / b)

    def test_value(self):
        frac = Fraction(1, 2)
        self.assertEqual(0.5, frac.value())

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_non_integer(self):
        with self.assertRaises((ValueError, TypeError)):
            Fraction(1.5, 2)
        with self.assertRaises((ValueError, TypeError)):
            Fraction(1, 2.5)
