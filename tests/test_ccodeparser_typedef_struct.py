__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar


class CCodeParserTypedefStruct(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_typedef_struct_single_line(self):
        input = []
        input.append('typedef struct{int a;}STRUCT_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.STRUCT, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'int', actualOutput[3].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'a', actualOutput[4].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[5].type)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'STRUCT_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)

    def test_typedef_struct_single_line_with_spaces(self):
        input = []
        input.append(' typedef struct { int a ; } STRUCT_TYPE_NAME ; ')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.STRUCT, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'int', actualOutput[3].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'a', actualOutput[4].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[5].type)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'STRUCT_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)

    def test_typedef_struct_multi_line(self):
        input = []
        input.append('typedef struct')
        input.append('{')
        input.append('    int a;')
        input.append('    short int b;')
        input.append('}STRUCT_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.STRUCT, actualOutput[1].type)
        self.assertEqual( Grammar.EOL, actualOutput[2].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( Grammar.EOL, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'int', actualOutput[5].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( 'a', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[7].type)
        self.assertEqual( Grammar.EOL, actualOutput[8].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[9].type)
        self.assertEqual( 'short', actualOutput[9].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[10].type)
        self.assertEqual( 'int', actualOutput[10].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[11].type)
        self.assertEqual( 'b', actualOutput[11].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[12].type)
        self.assertEqual( Grammar.EOL, actualOutput[13].type)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[14].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[15].type)
        self.assertEqual( 'STRUCT_TYPE_NAME', actualOutput[15].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[16].type)

        self.assertEqual( Grammar.EOL, actualOutput[17].type)


    def test_typedef_struct_bit_fields(self):
        input = []
        input.append('typedef struct{int a:2;}STRUCT_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.TYPEDEF, actualOutput[0].type)
        self.assertEqual( Grammar.STRUCT, actualOutput[1].type)
        self.assertEqual( Grammar.BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'int', actualOutput[3].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'a', actualOutput[4].literalValue)
        self.assertEqual( Grammar.COLON, actualOutput[5].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( '2', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[7].type)
        self.assertEqual( Grammar.BRACE_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[9].type)
        self.assertEqual( 'STRUCT_TYPE_NAME', actualOutput[9].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[10].type)

        self.assertEqual( Grammar.EOL, actualOutput[11].type)
