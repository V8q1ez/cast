__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerOtherOperators(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = cinderella(self._grammar)

    def test_other_ternary_conditional(self):
        input = []
        input.append('a?b:c')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.QUESTION_MARK, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( Grammar.COLON, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'c', actualOutput[4].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_other_ternary_conditional_with_spaces(self):
        input = []
        input.append('a ? b : c')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.QUESTION_MARK, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( Grammar.COLON, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'c', actualOutput[4].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_other_sizeof(self):
        input = []
        input.append('sizeof(a)')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.SIZEOF, actualOutput[0].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_other_sizeof_with_spaces(self):
        input = []
        input.append('sizeof ( a )')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.SIZEOF, actualOutput[0].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_other_alignof(self):
        input = []
        input.append('alignof(a)')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.ALIGNOF, actualOutput[0].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_other_alignof_with_spaces(self):
        input = []
        input.append('alignof ( a )')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.ALIGNOF, actualOutput[0].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)
