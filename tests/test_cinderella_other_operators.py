__author__ = 'V8q1ez'

import unittest

from src.cinderella import *


class compilerOtherOperators(unittest.TestCase):
    def setUp(self):
       self.tkz = cinderella()

    def test_other_ternary_conditional(self):
        input = []
        input.append('a?b:c')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( QUESTION_MARK, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( COLON, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'c', actualOutput[4].literalValue)
        self.assertEqual( EOL, actualOutput[5].type)

    def test_other_ternary_conditional_with_spaces(self):
        input = []
        input.append('a ? b : c')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( QUESTION_MARK, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( COLON, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'c', actualOutput[4].literalValue)
        self.assertEqual( EOL, actualOutput[5].type)
