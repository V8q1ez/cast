__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserVariables(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self._context = CCodeParsingContext()
        self.tkz = CCodeParser(self._grammar)

    def test_variables_simple(self):
        input = []
        input.append('int varName;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'int', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'varName', actualOutput[1].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[2].type)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)


    def test_variables_static(self):
        input = []
        input.append('static int varName;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual(Grammar. STATIC, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'int', actualOutput[1].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'varName', actualOutput[2].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_variables_simple_with_assignment(self):
        input = []
        input.append('int varName=100;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'int', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'varName', actualOutput[1].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( '100', actualOutput[3].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_variables_array_with_assignment_num(self):
        input = []
        input.append('int varName=[1,2];')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'int', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'varName', actualOutput[1].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[2].type)
        self.assertEqual( Grammar.SQUARE_BRACKET_LEFT, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( '1', actualOutput[4].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[5].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( '2', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SQUARE_BRACKET_RIGHT, actualOutput[7].type)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)

    def test_variables_array_with_assignment_num_spaces(self):
        input = []
        input.append('int varName = [ 1 , 2 ] ;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'int', actualOutput[0].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'varName', actualOutput[1].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[2].type)
        self.assertEqual( Grammar.SQUARE_BRACKET_LEFT, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( '1', actualOutput[4].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[5].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( '2', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SQUARE_BRACKET_RIGHT, actualOutput[7].type)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)
