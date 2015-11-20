__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserDefineMultiline(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_define_multi(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a b\\')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

    def test_define_multi_after_space(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a b \\')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

    def test_define_multi_simple_case(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a b \\')
        input.append('c')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'c', actualOutput[3].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_define_multi_broken_string(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "start \\')
        input.append(' finish"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'start  finish', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_multi_broken_literal(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a start\\')
        input.append('finish')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'startfinish', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_define_multi_broken_directive(self):
        context = CCodeParsingContext()
        input = []
        input.append('#de\\')
        input.append('fine a')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_define_multi_broken_variadic(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(..\\')
        input.append('.) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.VARIADIC_ARGS, actualOutput[3].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[6].type)