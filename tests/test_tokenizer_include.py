__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorInclude(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_include_quotes(self):
        input = '#include "hello.h"'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( INCLUDE, actualOutput[0].type)
        self.assertEqual( QUOTE, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'hello.h', actualOutput[2].literalValue)
        self.assertEqual( QUOTE, actualOutput[3].type)
