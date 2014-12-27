__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class compilerLogicalOperations(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_logical_negation(self):
        input = []
        input.append('!a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( NOT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_logical_negation_with_space(self):
        input = []
        input.append('! a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( NOT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_logical_and(self):
        input = []
        input.append('a&&b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( LOGICAL_END, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_logical_and_with_space(self):
        input = []
        input.append('a && b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( LOGICAL_END, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_logical_or(self):
        input = []
        input.append('a||b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( LOGICAL_OR, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_logical_or_with_space(self):
        input = []
        input.append('a || b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( LOGICAL_OR, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)