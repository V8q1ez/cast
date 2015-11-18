__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerComparisonRelational(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = cinderella(self._grammar)

    def test_comparison_equal_to(self):
        input = []
        input.append('a==b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.EQUAL_TO, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_equal_to_with_spaces(self):
        input = []
        input.append('a == b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.EQUAL_TO, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_not_equal_to(self):
        input = []
        input.append('a!=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.NOT_EQUAL_TO, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_not_equal_to_with_spaces(self):
        input = []
        input.append('a != b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.NOT_EQUAL_TO, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_less_than(self):
        input = []
        input.append('a<b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LESS_THAN, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_less_than_with_spaces(self):
        input = []
        input.append('a < b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LESS_THAN, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_greater_than(self):
        input = []
        input.append('a>b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.GREATER_THAN, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_greater_than_with_spaces(self):
        input = []
        input.append('a > b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.GREATER_THAN, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_less_or_equal(self):
        input = []
        input.append('a<=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LESS_OR_EQUAL, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_less_or_equal_with_spaces(self):
        input = []
        input.append('a <= b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LESS_OR_EQUAL, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_less_or_equal_off_nominal(self):
        input = []
        input.append('a < = b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LESS_THAN, actualOutput[1].type)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'b', actualOutput[3].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_comparison_greater_or_equal(self):
        input = []
        input.append('a>=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.GREATER_OR_EQUAL, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_greater_or_equal_with_spaces(self):
        input = []
        input.append('a >= b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.GREATER_OR_EQUAL, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comparison_greater_or_equal_off_nominal(self):
        input = []
        input.append('a > = b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.GREATER_THAN, actualOutput[1].type)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'b', actualOutput[3].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)