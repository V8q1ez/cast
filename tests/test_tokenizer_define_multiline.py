__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorDefineMultiline(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_define_multi(self):
        input = []
        input.append('#define a b\\')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

    def test_define_multi_after_space(self):
        input = []
        input.append('#define a b \\')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

    def test_define_multi_simple_case(self):
        input = []
        input.append('#define a b \\')
        input.append('c')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'c', actualOutput[3].literalValue)

        self.assertEqual( EOL, actualOutput[4].type)

    def test_define_multi_broken_string(self):
        input = []
        input.append('#define a "start \\')
        input.append(' finish"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'start  finish', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_multi_broken_literal(self):
        input = []
        input.append('#define a start\\')
        input.append('finish')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'startfinish', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_define_multi_broken_directive(self):
        input = []
        input.append('#de\\')
        input.append('fine a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_define_multi_broken_variadic(self):
        input = []
        input.append('#define a(..\\')
        input.append('.) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[3].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

        self.assertEqual( EOL, actualOutput[6].type)