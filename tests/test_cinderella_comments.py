__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerComments(unittest.TestCase):
    def setUp(self):
       self.tkz = cinderella()

    def test_comments_single_line_in_string(self):
        input = []
        input.append('"a//b"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( QUOTE, actualOutput[0].type)
        self.assertEqual( STRING, actualOutput[1].type)
        self.assertEqual( 'a//b', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_comments_single_line_in_include(self):
        input = []
        input.append('#include "//e"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( INCLUDE, actualOutput[0].type)
        self.assertEqual( QUOTE, actualOutput[1].type)
        self.assertEqual( STRING, actualOutput[2].type)
        self.assertEqual( '//e', actualOutput[2].literalValue)
        self.assertEqual( QUOTE, actualOutput[3].type)

        self.assertEqual( EOL, actualOutput[4].type)

    def test_comments_single_line_with_end_of_multiline(self):
        input = []
        input.append('// */')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( SINGLE_LINE_COMMENT, actualOutput[0].type)
        self.assertEqual( ' */', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)