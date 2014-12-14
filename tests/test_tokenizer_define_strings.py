__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorDefineStrings(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_define_str_space_including(self):
        input = '#define a "before after"'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'before after', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)