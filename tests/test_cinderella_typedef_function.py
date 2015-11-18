__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerTypedefFunction(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = cinderella(self._grammar)

    def test_typedef_simple_function(self):
        input = []
        input.append('typedef void(*FOO_TYPE)(void);')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.VOID, actualOutput[1].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.ASTERISK, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'FOO_TYPE', actualOutput[4].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[5].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[6].type)
        self.assertEqual( Grammar.VOID, actualOutput[7].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[9].type)

        self.assertEqual( Grammar.EOL, actualOutput[10].type)

    def test_typedef_simple_function_with_spaces(self):
        input = []
        input.append('typedef void ( * FOO_TYPE ) ( void ) ; ')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.VOID, actualOutput[1].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.ASTERISK, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'FOO_TYPE', actualOutput[4].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[5].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[6].type)
        self.assertEqual( Grammar.VOID, actualOutput[7].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[9].type)

        self.assertEqual( Grammar.EOL, actualOutput[10].type)