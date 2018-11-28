"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fraction` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (ValueError if not),
- method `value` returning float value of the fraction.
"""
from math import gcd

class Fraction(object):

    _nom = None
    _denom = None

    def __init__(self, nom, denom):
        self._nom = nom
        self._denom = denom

        if self._denom == 0:
            raise ValueError("The denominator cannot be 0")

        if self._denom < 0:
            self._nom = -1 * self._nom
            self._denom = -1 * self._denom

    def simplify(self):
        gc_divisor = gcd(self._nom, self._denom)
        self._nom = int(nom / gc_divisor)
        self._denom = int(denom / gc_divisor)
        return Fraction(self._nom, self._denom)


    def __str__(self):
        return "{0._nom}/{0._denom}".format(self)

    def __mul__(self, number):
        return Fraction(self._nom*number._nom, self._denom*number._denom)

    def __truediv__(self, number):
        return Fraction(self._nom*number._denom, self._denom*number._nom)

    def __add__(self, number):
        nom1 = self._nom*number._denom
        nom2 = number._nom*self._denom
        return Fraction(nom1 + nom2, self._denom*number._denom)

    def __sub__(self, number):
        nom1 = self._nom*number._denom
        nom2 = number._nom*self._denom
        return Fraction(nom1 - nom2, self._denom*number._denom)

    def __eq__(self, other):
        return self._nom == other._nom and self._denom == other._denom

    def value(self):
        return self._nom / self._denom

    @property
    def denom(self):
        return self._denom

    @denom.setter
    def denom(self, val):
        if val == 0:
            raise ValueError("The denominator cannot be 0")
        self._denom = val

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, val):
        self._nom = val