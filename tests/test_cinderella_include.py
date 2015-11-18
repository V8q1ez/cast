__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class preprocessorInclude(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = cinderella(self._grammar)

    def test_include_quotes(self):
        input = []
        input.append('#include "hello.h"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.INCLUDE, actualOutput[0].type)
        self.assertEqual( Grammar.QUOTE, actualOutput[1].type)
        self.assertEqual( Grammar.STRING, actualOutput[2].type)
        self.assertEqual( 'hello.h', actualOutput[2].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_include_multi_broken_directive(self):
        input = []
        input.append('#in\\')
        input.append('clude')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.INCLUDE, actualOutput[0].type)

        self.assertEqual( Grammar.EOL, actualOutput[1].type)
