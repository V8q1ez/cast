__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class compilerTypedef(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

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