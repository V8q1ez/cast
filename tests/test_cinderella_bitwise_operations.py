__author__ = 'V8q1ez'

import unittest

from src.cinderella import *


class compilerBitwiseOperations(unittest.TestCase):
    def setUp(self):
       self.tkz = cinderella()

    def test_bitwise_negation(self):
        input = []
        input.append('~a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( BITWISE_NOT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_bitwise_negation_with_space(self):
        input = []
        input.append('~ a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( BITWISE_NOT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_bitwise_and(self):
        input = []
        input.append('a&b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( BITWISE_AND, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_bitwise_and_with_spaces(self):
        input = []
        input.append('a & b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( BITWISE_AND, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_bitwise_or(self):
        input = []
        input.append('a|b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( BITWISE_OR, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_bitwise_or_with_spaces(self):
        input = []
        input.append('a | b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( BITWISE_OR, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)
