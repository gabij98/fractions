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

    nom = None
    denom = None

    def __init__(self, nom, denom):
        self.nom = nom
        self.denom = denom

        if self.denom == 0:
            raise ValueError("The denominator cannot be 0")

        gc_divisor = gcd(self.nom, self.denom)
        self.nom = int(nom / gc_divisor)
        self.denom = int(denom / gc_divisor)

        if self.denom < 0:
            self.nom = -1 * self.nom
            self.denom = -1 * self.denom

    def __str__(self):
        return "{0.nom}/{0.denom}".format(self)

    def __mul__(self, number):
        return Fraction(self.nom*number.nom, self.denom*number.denom)

    def __truediv__(self, number):
        return Fraction(self.nom*number.denom, self.denom*number.nom)

    def __add__(self, number):
        nom1 = self.nom*number.denom
        nom2 = number.nom*self.denom
        return Fraction(nom1 + nom2, self.denom*number.denom)

    def __sub__(self, number):
        nom1 = self.nom*number.denom
        nom2 = number.nom*self.denom
        return Fraction(nom1 - nom2, self.denom*number.denom)

    def __eq__(self, other):
        return self.nom == other.nom and self.denom == other.denom

    def value(self):
        return self.nom / self.denom


