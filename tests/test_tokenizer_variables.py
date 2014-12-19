__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class compilerVariables(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_variables_simple(self):
        input = []
        input.append('int varName;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'int', actualOutput[0].literalValue)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'varName', actualOutput[1].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[2].type)

        self.assertEqual( EOL, actualOutput[3].type)


    def test_variables_static(self):
        input = []
        input.append('static int varName;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( STATIC, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'int', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'varName', actualOutput[2].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[3].type)

        self.assertEqual( EOL, actualOutput[4].type)
