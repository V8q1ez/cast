__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar


class CCodeParserBitwiseOperations(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_bitwise_negation(self):
        input = []
        input.append('~a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.BITWISE_NOT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_bitwise_negation_with_space(self):
        input = []
        input.append('~ a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.BITWISE_NOT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_bitwise_and(self):
        input = []
        input.append('a&b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_AND, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_and_with_spaces(self):
        input = []
        input.append('a & b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_AND, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_or(self):
        input = []
        input.append('a|b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_OR, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_or_with_spaces(self):
        input = []
        input.append('a | b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_OR, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_xor(self):
        input = []
        input.append('a^b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_XOR, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_xor_with_spaces(self):
        input = []
        input.append('a ^ b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_XOR, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_left_shift(self):
        input = []
        input.append('a<<b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_LEFT_SHIFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_left_shift_with_spaces(self):
        input = []
        input.append('a << b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_LEFT_SHIFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_right_shift(self):
        input = []
        input.append('a>>b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_RIGHT_SHIFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_bitwise_right_shift_with_spaces(self):
        input = []
        input.append('a >> b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.BITWISE_RIGHT_SHIFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)