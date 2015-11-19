__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar


class CCodeParserLogicalOperations(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_logical_negation(self):
        input = []
        input.append('!a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.NOT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_logical_negation_with_space(self):
        input = []
        input.append('! a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.NOT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_logical_and(self):
        input = []
        input.append('a&&b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LOGICAL_END, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_logical_and_with_space(self):
        input = []
        input.append('a && b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LOGICAL_END, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_logical_or(self):
        input = []
        input.append('a||b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LOGICAL_OR, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_logical_or_with_space(self):
        input = []
        input.append('a || b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LOGICAL_OR, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)