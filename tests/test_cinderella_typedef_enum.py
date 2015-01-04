__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerTypedef(unittest.TestCase):
    def setUp(self):
       self.tkz = cinderella()

    def test_typedef_enum_single_line(self):
        input = []
        input.append('typedef enum{ENUM_VALUE_1}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( BRACE_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[5].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[6].type)

        self.assertEqual( EOL, actualOutput[7].type)

    def test_typedef_enum_single_line_with_spaces(self):
        input = []
        input.append('typedef enum { ENUM_VALUE_1 } ENUM_TYPE_NAME ;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( BRACE_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[5].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[6].type)

        self.assertEqual( EOL, actualOutput[7].type)

    def test_typedef_enum_single_line_with_value(self):
        input = []
        input.append('typedef enum{ENUM_VALUE_1=2}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( ASSIGNMENT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( '2', actualOutput[5].literalValue)
        self.assertEqual( BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[8].type)

        self.assertEqual( EOL, actualOutput[9].type)

    def test_typedef_enum_single_line_with_value_spaces(self):
        input = []
        input.append('typedef enum{ ENUM_VALUE_1 = 2 }ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[3].literalValue)
        self.assertEqual( ASSIGNMENT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( '2', actualOutput[5].literalValue)
        self.assertEqual( BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[8].type)

        self.assertEqual( EOL, actualOutput[9].type)

    def test_typedef_enum_multi_line(self):
        input = []
        input.append('typedef enum')
        input.append('{')
        input.append('    ENUM_VALUE_1,')
        input.append('    ENUM_VALUE_2')
        input.append('}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( EOL, actualOutput[2].type)
        self.assertEqual( BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( EOL, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[5].literalValue)
        self.assertEqual( COMMA, actualOutput[6].type)
        self.assertEqual( EOL, actualOutput[7].type)
        self.assertEqual( LITERAL, actualOutput[8].type)
        self.assertEqual( 'ENUM_VALUE_2', actualOutput[8].literalValue)
        self.assertEqual( EOL, actualOutput[9].type)
        self.assertEqual( BRACE_RIGHT, actualOutput[10].type)
        self.assertEqual( LITERAL, actualOutput[11].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[11].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[12].type)

        self.assertEqual( EOL, actualOutput[13].type)

    def test_typedef_enum_multi_line_with_values(self):
        input = []
        input.append('typedef enum')
        input.append('{')
        input.append('    ENUM_VALUE_1=1,')
        input.append('    ENUM_VALUE_2 = 2')
        input.append('}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( EOL, actualOutput[2].type)
        self.assertEqual( BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( EOL, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[5].literalValue)
        self.assertEqual( ASSIGNMENT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( '1', actualOutput[7].literalValue)
        self.assertEqual( COMMA, actualOutput[8].type)
        self.assertEqual( EOL, actualOutput[9].type)
        self.assertEqual( LITERAL, actualOutput[10].type)
        self.assertEqual( 'ENUM_VALUE_2', actualOutput[10].literalValue)
        self.assertEqual( ASSIGNMENT, actualOutput[11].type)
        self.assertEqual( LITERAL, actualOutput[12].type)
        self.assertEqual( '2', actualOutput[12].literalValue)
        self.assertEqual( EOL, actualOutput[13].type)
        self.assertEqual( BRACE_RIGHT, actualOutput[14].type)
        self.assertEqual( LITERAL, actualOutput[15].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[15].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[16].type)

        self.assertEqual( EOL, actualOutput[17].type)

    def test_typedef_enum_single_line_with_type(self):
        input = []
        input.append('typedef enum TYPE{ENUM_VALUE_1}ENUM_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( ENUM, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'TYPE', actualOutput[2].literalValue)
        self.assertEqual( BRACE_LEFT, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'ENUM_VALUE_1', actualOutput[4].literalValue)
        self.assertEqual( BRACE_RIGHT, actualOutput[5].type)
        self.assertEqual( LITERAL, actualOutput[6].type)
        self.assertEqual( 'ENUM_TYPE_NAME', actualOutput[6].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[7].type)

        self.assertEqual( EOL, actualOutput[8].type)