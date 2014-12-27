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

    def test_define_str_with_parentheses(self):
        input = []
        input.append('#define a " ( ) "')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( ' ( ) ', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_assignment(self):
        input = []
        input.append('#define a " b=7"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( ' b=7', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_comma(self):
        input = []
        input.append('#define a "b,c"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'b,c', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_sharp(self):
        input = []
        input.append('#define a "b#c"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'b#c', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_semicolon(self):
        input = []
        input.append('#define a "b;c"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'b;c', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_struct(self):
        input = []
        input.append('#define a "struct"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'struct', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_static(self):
        input = []
        input.append('#define a "static"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'static', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_square_braces(self):
        input = []
        input.append('#define a " [ ] "')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( ' [ ] ', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_square_braces(self):
        input = []
        input.append('#define a "a:b"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'a:b', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_star_and_backslash(self):
        input = []
        input.append('#define a "a*b/c"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'a*b/c', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_percent(self):
        input = []
        input.append('#define a "5%"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( '5%', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_function_type_definition(self):
        input = []
        input.append('#define a "typedef void(*FOO_TYPE)(void);"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'typedef void(*FOO_TYPE)(void);', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_arithmetic_operations(self):
        input = []
        input.append('#define a "a=b+c-d"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'a=b+c-d', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_increments_decrements(self):
        input = []
        input.append('#define a "a= ++b - c++ + --d + e--"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'a= ++b - c++ + --d + e--', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_str_with_comparison_relational(self):
        input = []
        input.append('#define a "a==b c!=d e<f g>h"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'a==b c!=d e<f g>h', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)