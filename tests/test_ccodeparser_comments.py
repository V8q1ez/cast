__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserComments(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self._context = CCodeParsingContext()
        self.tkz = CCodeParser(self._grammar)

    def test_comments_single_line_in_string(self):
        input = []
        input.append('"a//b"')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.QUOTE, actualOutput[0].type)
        self.assertEqual( Grammar.STRING, actualOutput[1].type)
        self.assertEqual( 'a//b', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_comments_single_line_in_include(self):
        input = []
        input.append('#include "//e"')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.INCLUDE, actualOutput[0].type)
        self.assertEqual( Grammar.QUOTE, actualOutput[1].type)
        self.assertEqual( Grammar.STRING, actualOutput[2].type)
        self.assertEqual( '//e', actualOutput[2].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_comments_single_line_with_end_of_multiline(self):
        input = []
        input.append('// */')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.SINGLE_LINE_COMMENT, actualOutput[0].type)
        self.assertEqual( ' */', actualOutput[0].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[1].type)

    def test_comments_multi_line_inserted_into_statement(self):
        input = []
        input.append('f = g/**//h;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'f', actualOutput[0].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'g', actualOutput[2].literalValue)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_START, actualOutput[3].type)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_LINE, actualOutput[4].type)
        self.assertEqual( '', actualOutput[4].literalValue)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_END, actualOutput[5].type)
        self.assertEqual( Grammar.DIVISION, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'h', actualOutput[7].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[8].type)

        self.assertEqual( Grammar.EOL, actualOutput[9].type)

    def test_comments_single_two_line(self):
        input = []
        input.append('//\\')
        input.append('i();')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.SINGLE_LINE_COMMENT, actualOutput[0].type)
        self.assertEqual( 'i();', actualOutput[0].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[1].type)

    def test_comments_single_two_line_more_complex(self):
        input = []
        input.append('/\\')
        input.append('/ j();')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.SINGLE_LINE_COMMENT, actualOutput[0].type)
        self.assertEqual( ' j();', actualOutput[0].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[1].type)

    def test_comments_multi_line_with_single_line(self):
        input = []
        input.append('/*//*/ l();')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.MULTI_LINE_COMMENT_START, actualOutput[0].type)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_LINE, actualOutput[1].type)
        self.assertEqual( '//', actualOutput[1].literalValue)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_END, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'l', actualOutput[3].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[4].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[5].type)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[6].type)

        self.assertEqual( Grammar.EOL, actualOutput[7].type)

    def test_comments_multi_line_with_single_line_spaces(self):
        input = []
        input.append('/* // */ l();')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.MULTI_LINE_COMMENT_START, actualOutput[0].type)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_LINE, actualOutput[1].type)
        self.assertEqual( ' // ', actualOutput[1].literalValue)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_END, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'l', actualOutput[3].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[4].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[5].type)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[6].type)

        self.assertEqual( Grammar.EOL, actualOutput[7].type)

    def test_comments_single_line_with_multiline_elements(self):
        input = []
        input.append('m = n//**/o')
        input.append(' +p;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'm', actualOutput[0].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'n', actualOutput[2].literalValue)
        self.assertEqual( Grammar.SINGLE_LINE_COMMENT, actualOutput[3].type)
        self.assertEqual( '**/o', actualOutput[3].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[4].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[5].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( 'p', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[7].type)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)

    def test_comments_single_line_with_multiline_elements_spaces(self):
        input = []
        input.append('m = n// **/o')
        input.append(' +p;')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'm', actualOutput[0].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'n', actualOutput[2].literalValue)
        self.assertEqual( Grammar.SINGLE_LINE_COMMENT, actualOutput[3].type)
        self.assertEqual( ' **/o', actualOutput[3].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[4].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[5].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[6].type)
        self.assertEqual( 'p', actualOutput[6].literalValue)
        self.assertEqual( Grammar.SEMICOLON, actualOutput[7].type)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)

    def test_comments_multi_line_complex(self):
        input = []
        input.append('/*****')
        input.append('* Function: a')
        input.append('******/')

        actualOutput = self.tkz.parseText(input, self._context)

        self.assertEqual( Grammar.MULTI_LINE_COMMENT_START, actualOutput[0].type)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_LINE, actualOutput[1].type)
        self.assertEqual( '****', actualOutput[1].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[2].type)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_LINE, actualOutput[3].type)
        self.assertEqual( '* Function: a', actualOutput[3].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[4].type)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_LINE, actualOutput[5].type)
        self.assertEqual( '*****', actualOutput[5].literalValue)
        self.assertEqual( Grammar.MULTI_LINE_COMMENT_END, actualOutput[6].type)

        self.assertEqual( Grammar.EOL, actualOutput[7].type)