__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class compilerTypedefStruct(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_typedef_struct_single_line(self):
        input = []
        input.append('typedef struct{ int a; }STRUCT_TYPE_NAME;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( TYPEDEF, actualOutput[0].type)
        self.assertEqual( STRUCT, actualOutput[1].type)
        self.assertEqual( BRACE_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'int', actualOutput[3].literalValue)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'a', actualOutput[4].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[5].type)
        self.assertEqual( BRACE_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'STRUCT_TYPE_NAME', actualOutput[7].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[8].type)

        self.assertEqual( EOL, actualOutput[9].type)
