__author__ = 'V8q1ez'

import unittest

from src.cinderella import *


class compilerCompoundAssignments(unittest.TestCase):
    def setUp(self):
       self.tkz = cinderella()

    def test_compound_addition(self):
        input = []
        input.append('a+=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( ADDITION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_addition_with_spaces(self):
        input = []
        input.append('a += b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( ADDITION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_subtraction(self):
        input = []
        input.append('a-=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( SUBTRACTION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_subtraction_with_spaces(self):
        input = []
        input.append('a -= b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( SUBTRACTION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_multiplication(self):
        input = []
        input.append('a*=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( MULTIPLICATION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_multiplication_with_spaces(self):
        input = []
        input.append('a *= b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( MULTIPLICATION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_division(self):
        input = []
        input.append('a/=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( DIVISION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_division_with_spaces(self):
        input = []
        input.append('a /= b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( DIVISION_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_modulo(self):
        input = []
        input.append('a%=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( MODULO_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_compound_modulo_with_spaces(self):
        input = []
        input.append('a %= b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( MODULO_ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)
