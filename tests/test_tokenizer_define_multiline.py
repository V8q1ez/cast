__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorDefineMultiline(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_define_multi(self):
        input = '#define a b\\'

        actualOutput = self.tkz.parseLine(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( BACKSLASH_NEWLINE, actualOutput[3].type)

    def test_define_multi_after_space(self):
        input = '#define a b \\'

        actualOutput = self.tkz.parseLine(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( BACKSLASH_NEWLINE, actualOutput[3].type)

        self.assertEqual( EOL, actualOutput[4].type)
