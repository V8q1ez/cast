__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorDefineStrings(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_define_str_space_including(self):
        input = []
        input.append('#define a "before after"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'before after', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_escaped_quote(self):
        input = []
        input.append('#define a "before\\\"after"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'before\\\"after', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_escaped_quote_spaces(self):
        input = []
        input.append('#define a "before \\\" after"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'before \\\" after', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_escaped_n(self):
        input = []
        input.append('#define a "before\\nafter"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'before\\nafter', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_escaped_n_spaces(self):
        input = []
        input.append('#define a "before \\n after"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'before \\n after', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_enum(self):
        input = []
        input.append('#define a "enum"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'enum', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_enum_spaces(self):
        input = []
        input.append('#define a " enum "')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( ' enum ', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_braces(self):
        input = []
        input.append('#define a " { } "')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( ' { } ', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)