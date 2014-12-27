__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class compilerBitwiseOperations(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

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
