__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorInclude(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_include_quotes(self):
        input = []
        input.append('#include "hello.h"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( INCLUDE, actualOutput[0].type)
        self.assertEqual( QUOTE, actualOutput[1].type)
        self.assertEqual( STRING, actualOutput[2].type)
        self.assertEqual( 'hello.h', actualOutput[2].literalValue)
        self.assertEqual( QUOTE, actualOutput[3].type)

        self.assertEqual( EOL, actualOutput[4].type)
