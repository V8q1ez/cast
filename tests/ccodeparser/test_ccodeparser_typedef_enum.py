__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserTypedef(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self._context = CCodeParsingContext()
        self.tkz = CCodeParser(self._grammar)

    def test_typedef_enum_single_line(self):
        input = []
        input.append('typedef enum{ENUM_VALUE_1}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[5].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[6].type)

        self.assertEqual( Grammar.EOL, actualOutput[7].type)

    def test_typedef_enum_single_line_with_spaces(self):
        input = []
        input.append('typedef enum { ENUM_VALUE_1 } ENUM_TYPE_NAME ;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[5].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[6].type)

        self.assertEqual( Grammar.EOL, actualOutput[7].type)

    def test_typedef_enum_single_line_with_value(self):
        input = []
        input.append('typedef enum{ENUM_VALUE_1=2}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( '2', actualOutput[5].literalValue)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)

    def test_typedef_enum_single_line_with_value_spaces(self):
        input = []
        input.append('typedef enum{ ENUM_VALUE_1 = 2 }ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( '2', actualOutput[5].literalValue)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)

    def test_typedef_enum_multi_line(self):
        input = []
        input.append('typedef enum')
        input.append('{')
        input.append('    ENUM_VALUE_1,')
        input.append('    ENUM_VALUE_2')
        input.append('}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.EOL, actualOutput[2].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( Grammar.EOL, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[5].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[6].type)
        self.assertEqual( Grammar.EOL, actualOutput[7].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[8].type)
        self.assertEqual( 'ENUM_VALUE_2', actualOutput[8].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[9].type)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[10].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[11].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[11].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[12].type)

        self.assertEqual( Grammar.EOL, actualOutput[13].type)

    def test_typedef_enum_multi_line_with_values(self):
        input = []
        input.append('typedef enum')
        input.append('{')
        input.append('    ENUM_VALUE_1=1,')
        input.append('    ENUM_VALUE_2 = 2')
        input.append('}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.EOL, actualOutput[2].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( Grammar.EOL, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[5].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( '1', actualOutput[7].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[8].type)
        self.assertEqual( Grammar.EOL, actualOutput[9].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[10].type)
        self.assertEqual( 'ENUM_VALUE_2', actualOutput[10].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[11].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[12].type)
        self.assertEqual( '2', actualOutput[12].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[13].type)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[14].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[15].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[15].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[16].type)

        self.assertEqual( Grammar.EOL, actualOutput[17].type)

    def test_typedef_enum_single_line_with_type(self):
        input = []
        input.append('typedef enum TYPE{ENUM_VALUE_1}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.ENUM, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'TYPE', actualOutput[2].literalValue)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[4].literalValue)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[5].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[7].type)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)