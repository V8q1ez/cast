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
        self.assertEqual( ' */', actualOutput[0].literalValue)

        self.assertEqual( EOL, actualOutput[1].type)

    def test_comments_multi_line_inserted_into_statement(self):
        input = []
        input.append('f = g/**//h;')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'f', actualOutput[0].literalValue)
        self.assertEqual( ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'g', actualOutput[2].literalValue)
        self.assertEqual( MULTI_LINE_COMMENT_START, actualOutput[3].type)
        self.assertEqual( MULTI_LINE_COMMENT_LINE, actualOutput[4].type)
        self.assertEqual( '', actualOutput[4].literalValue)
        self.assertEqual( MULTI_LINE_COMMENT_END, actualOutput[5].type)
        self.assertEqual( DIVISION, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'h', actualOutput[7].literalValue)
        self.assertEqual( SEMICOLON, actualOutput[8].type)

        self.assertEqual( EOL, actualOutput[9].type)

    def test_comments_single_two_line(self):
        input = []
        input.append('//\\')
        input.append('i();')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( SINGLE_LINE_COMMENT, actualOutput[0].type)
        self.assertEqual( 'i();', actualOutput[0].literalValue)

        self.assertEqual( EOL, actualOutput[1].type)

    def test_comments_single_two_line_more_complex(self):
        input = []
        input.append('/\\')
        input.append('/ j();')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( SINGLE_LINE_COMMENT, actualOutput[0].type)
        self.assertEqual( ' j();', actualOutput[0].literalValue)

        self.assertEqual( EOL, actualOutput[1].type)