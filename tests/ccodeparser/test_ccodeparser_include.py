__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserInclude(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_include_quotes(self):
        context = CCodeParsingContext()
        input = []
        input.append('#include "hello.h"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.INCLUDE, actualOutput[0].type)
        self.assertEqual( Grammar.QUOTE, actualOutput[1].type)
        self.assertEqual( Grammar.STRING, actualOutput[2].type)
        self.assertEqual( 'hello.h', actualOutput[2].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_include_multi_broken_directive(self):
        context = CCodeParsingContext()
        input = []
        input.append('#in\\')
        input.append('clude')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.INCLUDE, actualOutput[0].type)

        self.assertEqual( Grammar.EOL, actualOutput[1].type)
